# блокнот / expectation / version: 1.3 / 15.11.2026 / caktuz

import os
import socket
import errno
import sys
import json
from time import sleep
from datetime import datetime
from plyer import notification  # pip install plyer

# pyinstaller convertation : pyinstaller --noconfirm --onefile --windowed --hidden-import "plyer.platforms.win.notification" "<директория>"
# флаг --hidden-import обязатяльно для того чтобы в компиляцию были включены все сторонние библиотеки

if getattr(sys, 'frozen', False):                 # PyInstaller onefile
    BASE_DIR = os.path.dirname(sys.executable)    # папка с exe
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))


data_path = os.path.join(BASE_DIR, 'bloknot_data.json')
logs_path = os.path.join(BASE_DIR, 'expectation_mode_logs.txt')
icon_path = os.path.join(BASE_DIR, 'sahur-logo.ico')


LOCK_PORT = 28711
lock_socket = None

general = { "заметки" : {},
            "напоминалки" : {},
            "pid": 0}
log_msg_num = 0

def _is_addrinuse(er: OSError) -> bool:
    """EADDRINUSE на Linux/macOS/Windows + страховка по winerror."""
    # errno.EADDRINUSE: 98 Linux, 48 macOS, 100 Windows — уже покрывает все три ОС
    if er.errno == errno.EADDRINUSE:
        return True
    # На Windows у OSError есть .winerror; на POSIX атрибута нет → getattr вернёт None
    return getattr(er, 'winerror', None) == 10048  # WSAEADDRINUSE

def check_proc_clone() -> None:
  global lock_socket
  sct = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
  if sys.platform == 'win32':
    try:
        sct.setsockopt(socket.SOL_SOCKET, socket.SO_EXCLUSIVEADDRUSE, 1)
    except (AttributeError, OSError): pass 

  try:
    sct.bind(("127.0.0.1", LOCK_PORT))
  except OSError as er:
      sct.close()
      if _is_addrinuse(er):
          print("Программа уже запущена! Выход.")
          log_append(logs_path, "Программа уже запущена")
          log_append(logs_path, "EXIT")
          sys.exit(1)
      raise   
  lock_socket = sct


def log_write(filepath, data):
  with open(filepath, 'w', encoding='utf-8') as logFile:
     logFile.write(data+' '+str(datetime.now())[:-7]+' \n\n')
def log_append(filepath, data):
  try:
    global log_msg_num
    with open(filepath, 'a', encoding='utf-8') as logFile:
       log_msg_num += 1
       logFile.write(str(log_msg_num)+' | '+data+' | '+str(datetime.now())[:-7]+' \n')
  except FileNotFoundError: 
    log_append(logs_path, "FILE NOT FOUND ERROR FROM log_append")
    json_write()
    return False

def json_write() : # запись 
  with open(data_path, 'w', encoding='utf-8') as file:  
    json.dump(general, file, ensure_ascii=False, indent=2)
def json_read() : # чтение 
  try: 
    with open(data_path, 'r', encoding='utf-8') as file:
      data = json.load(file)
      general.clear()
      general.update(data)
  except (FileNotFoundError, json.JSONDecodeError) as e:
    log_append(logs_path, f"READ ERROR: {e}")
    return False
  except FileNotFoundError: 
    log_append(logs_path, "FILE NOT FOUND ERROR FROM json_read")
    json_write()
    return False


def _notification(nap):
  try: 
    notification.notify(
      title= "Напоминалка",
      message=nap,
      app_name='bloknot',
      app_icon=icon_path,
      timeout=1 ) 
  except Exception:
     log_append(logs_path, "SOMETHING ERROR FROM _notfication")
     return False
 
def main() :
    check_proc_clone()
    #print('start')
    log_write(logs_path, 'log file is created'); sleep(0.5)
    fired = set() 
    while True:
      try: 
          sleep(1)
          json_read()
          dt_now = datetime.now().replace(microsecond=0)
          for nap in general['напоминалки']:
              try:
                dt_end = datetime.strptime(general['напоминалки'][nap]['dt_end'], "%Y-%m-%d %H:%M:%S")
              except (ValueError, TypeError):
                log_append(logs_path, f"BAD dt_end for {nap}")
                continue

              #print(f"\r {dt_now}  {general['напоминалки'][nap]}", end="", flush=True)

              if nap in fired: # если дату изменили - уберёт из множества отработанных
                if dt_end > dt_now:
                  fired.remove(nap) 
                  print(nap, "удалён из списка отработанных") 
                 
              if dt_end <= dt_now and nap not in fired:
                if general['напоминалки'][nap]['status'] != "[выполнено]": 
                  if len(fired) < 1000:
                      _notification(general['напоминалки'][nap]['text'])
                      log_append(logs_path, "есть уведомлениие")
                      fired.add(nap)
              
      except KeyboardInterrupt: 
        log_append(logs_path, "EXIT")
        return 0
      except ValueError:
        log_append(logs_path, "ValueError ERROR FROM main")
      except: log_append(logs_path, "SOMETHING ERROR FROM main")

if __name__ == "__main__": 
    main()