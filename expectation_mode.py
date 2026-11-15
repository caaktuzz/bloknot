# блокнот / expectation / version: 1.3 / 15.11.2026 / caktuz

import os
import socket
import errno
from sys import exit as sys_exit, platform
import json
from time import sleep
from datetime import datetime
from plyer import notification  # pip install plyer

# pyinstaller convertation : pyinstaller --noconfirm --onefile --windowed --hidden-import "plyer.platforms.win.notification" "<директория>"
# флаг --hidden-import обязатяльно для того чтобы в компиляцию были включены все сторонние библиотеки

BASE_DIR = __file__.replace('expectation_mode.py', '')
data_path = BASE_DIR + 'bloknot_data.json'
logs_path = BASE_DIR + 'bloknot_logs.txt'
icon_path = BASE_DIR + 'sahur-logo.ico'

LOCK_PORT = 28711
lock_socket = None

def check_proc_clone():
  global lock_socket
  sct = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
  if platform == 'win32':
    try:
        sct.setsockopt(socket.SOL_SOCKET, socket.SO_EXCLUSIVEADDRUSE, 1)
    except (AttributeError, OSError): pass 

  try:
    sct.bind(("127.0.0.1", LOCK_PORT))
  except OSError as er:
      sct.close()
      if er.errno in (errno.EADDRINUSE,
          getattr(errno, "WSAEADDRINUSE", errno.EADDRINUSE)):
          print("Программа уже запущена! Выход.")
          sys_exit(1)
      raise   
  lock_socket = sct


general = { "заметки" : {},
            "напоминалки" : {},
            "pid": 0}
log_msg_num = 0

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
  except: 
     log_append(logs_path, "SOMETHING ERROR FROM _notfication")
     return False
 
def main() :
    check_proc_clone()
    print('start')
    log_write(logs_path, 'log file is created'); sleep(1)
    fired = set() 
    while True:
      try: 
          sleep(1)
          json_read()
          dt_now = datetime.now().replace(microsecond=0)
          for nap in general['напоминалки']:
              dt_end = datetime.strptime(general['напоминалки'][nap]['dt_end'], "%Y-%m-%d %H:%M:%S")
              print(f"\r {dt_now}  {general['напоминалки'][nap]}", end="", flush=True)
              if dt_end <= dt_now and nap not in fired:
                  log_append(logs_path, "есть уведомлениие")
                  _notification(general['напоминалки'][nap]['text'])
                  general['напоминалки'][nap]['status'] = 1
                  fired.add(nap)
      except KeyboardInterrupt: break
      #except: log_append(logs_path, "SOMETHING ERROR FROM main")

if __name__ == "__main__": 
    main()