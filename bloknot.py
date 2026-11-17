# блокнот / version: 1.2 / 17.11.2026 / caktuz

from os import system, kill, path
import signal
import sys
import subprocess
import json
import time
from datetime import datetime

# paths setup
if getattr(sys, 'frozen', False):              # PyInstaller onefile
    BASE_DIR = path.dirname(sys.executable)    # папка с exe
else:
    BASE_DIR = path.dirname(path.abspath(__file__))

data_path = path.join(BASE_DIR, 'bloknot_data.json')
expectation_mode_path = path.join(BASE_DIR, 'expectation_mode.exe')
expectation_mode_path_py = path.join(BASE_DIR, 'expectation_mode.py')
logs_path = path.join(BASE_DIR, 'expectation_mode_logs.txt')
icon_path = path.join(BASE_DIR, 'sahur-logo.ico')

general = { "заметки" : {}, # dict for bloknot_data.json
            "напоминалки" : {},
            "pid": "" }

if sys.platform == 'win32': clearOutput = "cls" 
else: clearOutput = "clear"

def write() : # запись 
  with open(data_path, 'w', encoding='utf-8') as file:  
    json.dump(general, file, ensure_ascii=False, indent=2)
def read() : # чтение 
  try: 
    with open(data_path, 'r', encoding='utf-8') as file:
      data = json.load(file)
      general.clear()
      general.update(data)
  except FileNotFoundError: 
    print('файл "bloknot_data.json" не найден'); time.sleep(1)
    _write = write()

def _exit(): # Выход с сохранением
  update_write = write()
  print("данные сохранены"); time.sleep(1)
  exit()


def menu(): # Главное меню
    print(" - - - Блокнот - - -")
    print('| [1] - Заметки     |\n| [2] - Напоминалки |\n| [3] - Выход       |\n - - - - - - - - - -')
    de = input('>> ')
    return de
    
def zametki(): # Заметки
  while True:
    system(clearOutput)
    _read = read()
    print('Последние заметки:'); time.sleep(0.2)
    if len(general['заметки']) > 0:
      for nap in general['заметки']:
        print('#',general['заметки'][nap]['num'],'/',general['заметки'][nap]['dt'],'/',general['заметки'][nap]['title'][0:35]+'...')
        time.sleep(0.1)
    else: print("список пуст.",),time.sleep(0.1)

    print('[1] - Новая заметка');time.sleep(0.1)
    print('[2] - Весь список');time.sleep(0.1)
    print('[ ] - Назад');time.sleep(0.1)
    de = input('>> ')

    def note_record(flag, Num):
        if flag == True: print('[1] - Оставить старое')
        new_record_title = input("Название: ")
        if new_record_title == ' ': return
        if new_record_title == '1' and flag == False: print("это новая заметка!"); return 
        if new_record_title == '1' and flag == True: new_record_title = general['заметки'][Num]['title']

        if flag == True: print('[1] - Оставить старое')
        new_record = input("Содержание: ")
        if new_record == ' ': return
        if new_record == '1' and flag == False: print("это новая заметка!"); return 
        if new_record == '1' and flag == True: new_record = general['заметки'][Num]['text']

        if len(general['заметки']) > 0: 
          for num in general['заметки']: number = general['заметки'][num]['num'] + 1
        else: number = 1

        if flag == True:
          general['заметки'][Num]['title'] = new_record_title
          general['заметки'][Num]['text'] = new_record
          general['заметки'][Num]['dt'] = str(datetime.now())[:-7]
        else:
          general['заметки'][number] = {'num': number, 'dt': str(datetime.now())[:-7], 'title':new_record_title, 'text':new_record}

        update_write = write()

    if de == '1':
      note_record(False, None)

    elif de == '2': 
      for nap in general['заметки']:
        print('#',general['заметки'][nap]['num'],'/',general['заметки'][nap]['dt'],'/',general['заметки'][nap]['title'][0:30]+'...')
        time.sleep(0.1)
      
      print('[1] - Выбрать запись \n[2] - Удалить всё \n[3] - Назад')
      de = input('>> ')
      if de == '1': 
        poisk = input('Введите номер записи: ')
        if poisk in general['заметки']: 
          print('#',general['заметки'][poisk]['num'],'/',general['заметки'][poisk]['dt'],general['заметки'][poisk]['title'],'\n',general['заметки'][poisk]['text'])
          time.sleep(0.1)
          print('[1] - Изменить \n[2] - Удалить \n[ ] - Назад')
          de = input('>> ')

          if de == '1':
            note_record(True, poisk)

          elif de == '2':  
            print("[1] - Да, удалить заметку \n[2] - Нет, вернуться назад")
            confirmation = input("Подтверждение: ")
            if confirmation == '1': 
              del general['заметки'][poisk]
              update_write = write()

        else: print("такой нету"); time.sleep(1)

      elif de == '2':
        print("[1] - Да, удалить все заметки \n[2] - Нет, вернуться назад")
        confirmation = input("Подтверждение: ")
        if confirmation == '1': 
          general['заметки'].clear()
          update_write = write()
          print("заметки очищены"); time.sleep(1)
        else: continue

      elif de == 'exit' or de == ' ': continue
    elif de == 'exit' or de == ' ': return de
      

def dela(): # Напоминалки
  while True:
    system(clearOutput)
    _read = read()
    print('Последние напоминалки:'); time.sleep(0.2)
    if len(general["напоминалки"]) > 0:
      for nap in general['напоминалки']:
        print('#', general['напоминалки'][nap]['num'],'/',general['напоминалки'][nap]['dt'],'/',general['напоминалки'][nap]['text'][0:30]+'...',general['напоминалки'][nap]['status'])
        time.sleep(0.1)
    else: print("список пуст."); time.sleep(0.1)
     
    print("[1] - Новое напоминание"); time.sleep(0.1)
    print("[2] - Весь список"); time.sleep(0.1)
    print("[3] - Режим фонового ожидания"); time.sleep(0.1)
    print("[ ] - Назад"); time.sleep(0.1)
    de = input('>> ')

    def nap_record(flag, Num):
      while True:
        if flag == True: print('[1] - Оставить старое')
        new_record = input("Содержание: ")
        if new_record == ' ': break
        if new_record == '1' and flag == False: print("это новая напоминалка!"); continue 
        if new_record == '1' and flag == True: new_record = general['напоминалки'][Num]['text']

        if flag == True: print('[1] - Оставить старое')
        new_record_dt_end = input("Время оповещения (ГГГГ-ММ-ДД ЧЧ:ММ:СС): ")
        try:
            datetime.strptime(new_record_dt_end, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("неверный формат"); continue
        if new_record_dt_end == '1' and flag == False: print("это новая напоминалка!"); continue 
        if new_record_dt_end == '1' and flag == True: new_record_dt_end = general['напоминалки'][Num]['dt_end']

        if len(general['напоминалки']) > 0: 
          for num in general['напоминалки']: number = general['напоминалки'][num]['num'] + 1
        else: number = 1

        if flag == True: 
          general['напоминалки'][Num]['dt']=str(datetime.now())[:-7]
          general['напоминалки'][Num]['dt_end']=new_record_dt_end
          general['напоминалки'][Num]['text']=new_record
          general['напоминалки'][Num]['status']="[не выполнено]"
        else:
          general['напоминалки'][number] = {'num':int(number), 
                                            'dt':str(datetime.now())[:-7],
                                            'dt_end':new_record_dt_end, 
                                            'text':new_record, 
                                            'status':"[не выполнено]"}
        update_write = write()
        break

    if de == '1':
      nap_record(False, None)

    elif de == '2': 
      for nap in general['напоминалки']:
        print('#',general['напоминалки'][nap]['num'],'/',general['напоминалки'][nap]['dt'],'/',general['напоминалки'][nap]['text'][0:30]+'...', general['напоминалки'][nap]['status'])
        time.sleep(0.1)

      print('[1] - Выбрать запись \n[2] - Удалить всё \n[ ] - Назад')
      de = input('>> ')

      if de == '1': 
        poisk = input('Введите номер записи: ')
        if poisk in general['напоминалки']: 
          print('#',general['напоминалки'][poisk]['num'],'/',general['напоминалки'][poisk]['dt'],'/',general['напоминалки'][poisk]['status'],'\n',general['напоминалки'][poisk]['text'][0:30])
          time.sleep(0.1)
          print('[1] - Сменить статус \n[2] - Изменить \n[3] - Удалить \n[ ] - Назад')
          de = input('>> ')
          if de == '1':
            if general['напоминалки'][poisk]['status'] == "[выполнено]": general['напоминалки'][poisk]['status'] = "[не выполнено]"
            else: general['напоминалки'][poisk]['status'] = "[выполнено]"
            write()
            print("готово"); time.sleep(1)
          elif de == '2':
            nap_record(True, poisk)
          elif de == '3': 
            print("[1] - Да, удалить напоминалку \n[2] - Нет, вернуться назад")
            confirmation = input("Подтверждение: ")
            if confirmation == '1': 
              del general['напоминалки'][poisk]
              update_write = write()

        else: print("такой нету"); time.sleep(1)
      elif de == '2':
        print("[1] - Да, удалить все напоминалки \n[2] - Нет, вернуться назад")
        confirmation = input("Подтверждение: ")
        if confirmation == '1': 
          general['напоминалки'].clear()
          update_write = write()
          print("напоминалки очищены"); time.sleep(1)
        else: continue

      elif de == 'exit' or de == ' ': continue
      
    elif de == '3': 
        print('Режим ожидания запустит безоконную программу "expectation_mode.exe" в фоне.\nОна служит таймером и при наступлении указанного в напоминалке времени, отправит уведомление')
        print('Также вы можете самостоятельно закинуть ярлык этой проги в папку автозагрузки и при повторном включении пк, она будет запускаться автоматически')
        print("[1] - Включить")
        print("[2] - Выключить")
        de = input(">> ")
        if de == '1':
            #print("пока недоступно. запустите программу в ручную"); time.sleep(2)
            try: 
              proc = subprocess.Popen([expectation_mode_path]) # для не скомпилированного напоминалкина используй переменную "expectation_mode_path_py"
              print("запущено успешно"); time.sleep(1)
              general["pid"] = proc.pid
              update_write = write()
            except FileNotFoundError: print('файл "expectation_mode.exe" не найден'); time.sleep(1)
            
        elif de == '2':
          #print("пока недоступно. остановите программу в ручную"); time.sleep(2)
          _read = read()
          if sys.platform == 'win32':
              stop_try = system(f"taskkill /F /T /PID {general['pid']}") 
              time.sleep(2)
              if stop_try == 0: 
                print("остановили успешно"); time.sleep(1)
          else: # for unix 
              kill(int(general['pid']), signal.SIGTERM) 

          continue
          #try: subprocess.run(["taskkill", "/F", "/PID", str(pid)], check=True)
          #except: print("ошибка на моменте остановки"); time.sleep(3)

    elif de == '3' or de == ' ': return de



def main():
  while True:
    try:
      system(clearOutput)
      _read = read()

      a = menu()

      if a == '1':
        a = zametki()
        if  a == '3' or a == ' ': continue

      elif a == '2':
        a = dela()
        if a == '3' or a == ' ': continue

      elif a == '3' or a == ' ': _exit()

      else: continue

    except KeyboardInterrupt: 
      _exit()

if __name__ == '__main__': 
    main()
  




#print(general)
#print('stop'), time.sleep(1)
    