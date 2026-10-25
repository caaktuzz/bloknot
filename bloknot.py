# блокнот / version: 1.1 / 22.08.2026 / caktuz

import os
import sys
import subprocess
import json
import time
import datetime


general = { "заметки" : {},
            "напоминалки" : {},
            "pid": "" }

def write() : # запись 
  with open('data/bloknot_data.json', 'w', encoding='utf-8') as file:  
    json.dump(general, file, ensure_ascii=False, indent=2)
def read() : # чтение 
  try: 
    with open('data/bloknot_data.json', 'r', encoding='utf-8') as file:
      data = json.load(file)
      general.clear()
      general.update(data)
  except FileNotFoundError: 
    print('файл "bloknot_data.json" не найден'), time.sleep(1)
    _write = write()

def _exit():
  update_write = write()
  print("данные сохранены"), time.sleep(1)
  sys.exit()


def menu(): # Главное меню
    print(" - - - Блокнот - - -")
    print('| [1] - Заметки     |\n| [2] - Списки дел  |\n| [3] - Выход       |\n - - - - - - - - - -')
    de = input('>> ')
    return de
    
def zametki():# Заметки
  while True:
    os.system('cls')
    _read = read()
    print('Последние заметки:'), time.sleep(0.2)
    if len(general['заметки']) > 0:
      for nap in general['заметки']:
        print('#',general['заметки'][nap]['num'],'/',general['заметки'][nap]['dt'],'/',general['заметки'][nap]['title'][0:30]+'...'),time.sleep(0.1)
    else: print("список пуст.",),time.sleep(0.1)

    print('[1] - Новая заметка'),time.sleep(0.1)
    print('[2] - Весь список'),time.sleep(0.1)
    print('[3] - Назад'),time.sleep(0.1)
    de = input('>> ')

    if de == '1':
       new_record_title = input("Название: ")
       if new_record_title == ' ': continue
       new_record = input("Содержание: ")
       if new_record_title == ' ': continue
       if len(general['заметки']) > 0: 
         for num in general['заметки']: number = general['заметки'][num]['num'] + 1
       else: number = 1
       general['заметки'][number] = {'num': number, 'dt': str(datetime.datetime.now())[:-7], 'title':new_record_title, 'text':new_record}
       update_write = write()

    elif de == '2': 
      for nap in general['заметки']:
        print('#',general['заметки'][nap]['num'],'/',general['заметки'][nap]['dt'],'/',general['заметки'][nap]['title'][0:30]+'...'),time.sleep(0.1)
      
      print('[1] - Выбрать запись \n[2] - Удалить всё \n[3] - Назад')
      de = input('>> ')
      if de == '1': 
        poisk = input('Введите номер записи: ')
        if poisk in general['заметки']: 
          print('#',general['заметки'][poisk]['num'],'/',general['заметки'][poisk]['dt'],general['заметки'][nap]['title'],'\n',general['заметки'][poisk]['text']),time.sleep(0.1)
          print('[1] - Изменить \n[2] - Удалить \n[3] - Назад')
          de = input('>> ')
          if de == '1':
            print("функция пока недоступна"), time.sleep(1)
          elif de == '2': 
            del general['заметки'][poisk]
            update_write = write()
        else: print("такой нету"), time.sleep(1)

      elif de == '2':
        print("[1] - Да, удалить все заметки \n[2] - Нет, вернуться назад")
        confirmation = input("Подтверждение: ")
        if confirmation == '1': 
          general['заметки'].clear()
          update_write = write()
          print("заметки очищены"), time.sleep(1)
        else: continue

      elif de == '3' or de == ' ': continue
    elif de == '3' or de == ' ': return de
      

def dela(): # Напоминалки
  while True:
    os.system('cls')
    _read = read()
    print('Последние напоминалки:'), time.sleep(0.2)
    if len(general["напоминалки"]) > 0:
      for nap in general['напоминалки']:
        print('#', general['напоминалки'][nap]['num'],'/',general['напоминалки'][nap]['dt'],'/',general['напоминалки'][nap]['text'][0:30]+'...'),time.sleep(0.1)
    else: print("список пуст."); time.sleep(0.1)
     
    print("[1] - Новое напоминание"); time.sleep(0.1)
    print("[2] - Весь список"); time.sleep(0.1)
    print("[3] - Назад"); time.sleep(0.1)
    print("[4] - Режим фонового ожидания"); time.sleep(0.1)
    de = input('>> ')

    if de == '1':
       new_record = input("Содержание: ")
       new_record_dt_end = input("Время оповещения (ГГГГ-ММ-ДД ЧЧ:ММ:СС): ")
       if new_record == ' ': continue
       if len(general['напоминалки']) > 0: 
         for num in general['напоминалки']: number = general['напоминалки'][num]['num'] + 1
       else: number = 1
       general['напоминалки'][number] = {'num': number, 'dt': str(datetime.datetime.now())[:-7],'dt_end':new_record_dt_end, 'text' : new_record}
       update_write = write()

    elif de == '2': 
      for nap in general['напоминалки']:
        print('#',general['напоминалки'][nap]['num'],'/',general['напоминалки'][nap]['dt'],'/',general['напоминалки'][nap]['text'][0:30]+'...'),time.sleep(0.1)

      print('[1] - Выбрать запись \n[2] - Удалить всё \n[3] - Назад')
      de = input('>> ')

      if de == '1': 
        poisk = input('Введите номер записи: ')
        if poisk in general['напоминалки']: 
          print('#',general['напоминалки'][poisk]['num'],'/',general['напоминалки'][poisk]['dt'],'\n',general['напоминалки'][poisk]['text'][0:30]),time.sleep(0.1)
          print('[1] - Изменить \n[2] - Удалить \n[3] - Назад')
          de = input('>> ')
          if de == '1':
            print("функция пока недоступна"), time.sleep(1)
          elif de == '2': 
            del general['напоминалки'][poisk]
            update_write = write()

        else: print("такой нету"), time.sleep(1)
      elif de == '2':
        print("[1] - Да, удалить все напоминалки \n[2] - Нет, вернуться назад")
        confirmation = input("Подтверждение: ")
        if confirmation == '1': 
          general['напоминалки'].clear()
          update_write = write()
          print("напоминалки очищены"), time.sleep(1)
        else: continue

      elif de == '3' or de == ' ': continue
      
    elif de == '4': 
        print('Режим ожидания запустит безоконную программу "expectation_mode.exe" в фоне.\nОна служит таймером и при наступлении указанного в напоминалке времени, отправит уведомление')
        print('Также вы можете самостоятельно закинуть ярлык этой проги в папку автозагрузки и при повторном включении пк, она будет запускаться автоматически')
        print("[1] - Включить")
        print("[2] - Выключить")
        de = input(">> ")
        if de == '1':
            print("пока недоступно. запустите программу в ручную"), time.sleep(2)
            continue
            try: 
              proc = subprocess.Popen(r"D:\.Profile\Desktop\hackerskie_codi\Python\projects\output\expectation_mode.exe")
              print("запущено успешно"), time.sleep(1)
              general["pid"] = proc.pid
              update_write = write()
            except FileNotFoundError: print('файл "expectation_mode.exe" не найден'), time.sleep(1)
            
        elif de == '2':
          print("пока недоступно. запустите программу в ручную"), time.sleep(2)
          continue
          _read = read()
          #proc.terminate()
          try: os.system(f"taskkill /F /T /PID {general["pid"]}") 
          except: print("ошибка на моменте остановки"), time.sleep(3)

    elif de == '3' or de == ' ': return de




while True:
  os.system('cls')
  _read = read()

  a = menu()

  if a == '1':
      a = zametki()
      if  a == '3' or a == ' ': continue

  elif a == '2':
      a = dela()
      if a == '3' or a == ' ': continue

  elif a == '3' or a == ' ': safe_exit = _exit()

  else: continue

  break
  




print(general)
print('stop'), time.sleep(1)
    