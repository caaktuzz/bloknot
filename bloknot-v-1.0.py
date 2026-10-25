# блокнот / version: 1.0 / 

import time
import datetime


заметки = { 1:{'num':1, 'dt': '2026-06-09','text': 'запись 1'},
            2:{'num':2, 'dt': '09.06.2026','text': 'запись 2'},
            3:{'num':3, 'dt': '09.06.2026','text': 'запись 3'}  }

напоминалки = { 1:{'num':1, 'dt': '09.06.2026','text': 'запись 1'},
                2:{'num':2, 'dt': '09.06.2026','text': 'запись 2'},
                3:{'num':3, 'dt': '09.06.2026','text': 'запись 3'} }
def menu(): # Главное меню
    print(" - - - Блокнот - - -")
    print('| [1] - Заметки     |\n| [2] - Списки дел  |\n| [3] - Выход       |\n - - - - - - - - - -')
    de = input('>> ')
    return de
    
def zametki():# Заметки
  while True:
    if len(list(заметки)) >= 3:
      print("Подблок №1")
      print('Последние заметки: \n', '#', заметки[list(заметки)[-1]]['num'],'/', заметки[list(заметки)[-1]]['dt'],'/', заметки[list(заметки)[-1]]['text']),time.sleep(0.1)
      print(' #', заметки[list(заметки)[-2]]['num'],'/', заметки[list(заметки)[-2]]['dt'],'/', заметки[list(заметки)[-2]]['text']),time.sleep(0.1)
      print(' #', заметки[list(заметки)[-3]]['num'],'/', заметки[list(заметки)[-3]]['dt'],'/', заметки[list(заметки)[-3]]['text']),time.sleep(0.1)
    elif len(list(заметки)) == 2: 
      print("Подблок №2")
      print('Последние заметки: \n', '#', заметки[list(заметки)[-1]]['num'],'/', заметки[list(заметки)[-1]]['dt'],'/', заметки[list(заметки)[-1]]['text']),time.sleep(0.1)
      print(' #', заметки[list(заметки)[-2]]['num'],'/', заметки[list(заметки)[-2]]['dt'],'/', заметки[list(заметки)[-2]]['text']),time.sleep(0.1)
    elif len(list(заметки)) == 1: 
      print("Подблок №3")
      print('Последние заметки: \n', '#', заметки[list(заметки)[-1]]['num'],'/', заметки[list(заметки)[-1]]['dt'],'/', заметки[list(заметки)[-1]]['text']),time.sleep(0.1)
    elif len(list(заметки)) <= 0: print("Список пуст.",),time.sleep(0.1)
    time.sleep(1)
    print('[1] - Новая заметка'),time.sleep(0.1)
    print('[2] - Весь список'),time.sleep(0.1)
    print('[3] - Назад'),time.sleep(0.1)

    de = input('>> ')
    if de == '1':
       new_record_title = input("Название: ")
       new_record = input("Содержание: ")
       number = list(заметки)[-1]+1 
       print(number)
       заметки[number] = {'num': number, 'dt': str(datetime.datetime.now())[:-7], 'text' : '>'+new_record_title +'< - '+ new_record}
    elif de == '2': return de
    elif de == '3': return de
      

def dela(): # Напоминалки
  while True:
    if len(list(напоминалки)) >= 3:
      #print("Подблок №1")
      print('Последние напоминалки: \n', '#', напоминалки[list(напоминалки)[-1]]['num'],'/', напоминалки[list(напоминалки)[-1]]['dt'],'/', напоминалки[list(напоминалки)[-1]]['text']),time.sleep(0.1)
      print(' #', напоминалки[list(напоминалки)[-2]]['num'],'/', напоминалки[list(напоминалки)[-2]]['dt'],'/', напоминалки[list(напоминалки)[-2]]['text'])
      print(' #', напоминалки[list(напоминалки)[-3]]['num'],'/', напоминалки[list(напоминалки)[-3]]['dt'],'/', напоминалки[list(напоминалки)[-3]]['text'])
    elif len(list(напоминалки)) == 2: 
      #print("Подблок №2")
      print('Последние напоминалки: \n', '#', напоминалки[list(напоминалки)[-1]]['num'],'/', напоминалки[list(напоминалки)[-1]]['dt'],'/', напоминалки[list(напоминалки)[-1]]['text']),time.sleep(0.1)
      print(' #', напоминалки[list(напоминалки)[-2]]['num'],'/', напоминалки[list(напоминалки)[-2]]['dt'],'/', напоминалки[list(напоминалки)[-2]]['text'])
    elif len(list(напоминалки)) == 1: 
      #print("Подблок №3")
      print('Последние напоминалки: \n', '#', напоминалки[list(напоминалки)[-1]]['num'],'/', напоминалки[list(напоминалки)[-1]]['dt'],'/', напоминалки[list(напоминалки)[-1]]['text']),time.sleep(0.1)
    elif len(list(напоминалки)) <= 0: print("Список пуст.",),time.sleep(0.1)
    
     

    print("[1] - Новое напоминание"),time.sleep(0.1)
    print("[2] - Весь список"),time.sleep(0.1)
    print("[3] - Назад"),time.sleep(0.5)
    de = input('>> ')

    if de == '1':
       new_record = input("Содержание: ")
       number = list(напоминалки)[-1]+1 
       print(number)
       напоминалки[number] = {'num': number, 'dt': str(datetime.datetime.now())[:-7], 'text' : '- '+ new_record}

    elif de == '2': 
      a = len(tuple(напоминалки)) # количсетво эелементов
      c = 0 # количество циклов
      while a > c:
       p = tuple(напоминалки)[c] # обновляемое имя ключа
       #if p not in напоминалки: 
       #  print('1212dd')
       print(' #', напоминалки[-p]['num'],'/', напоминалки[-p]['dt'],'/', напоминалки[-p]['text']),time.sleep(0.3)
       c += 1

      print('[1] - Выбрать запись \n[2] - Назад')
      de = input('>> ')
      if de == '1': 
        poisk = int(input('Введите номер записи: ')) -1
        print(poisk)
        if poisk in напоминалки: 
          print(' #', напоминалки[list(напоминалки)[poisk]]['num'],'/', напоминалки[list(напоминалки)[poisk]]['dt'],'/', напоминалки[list(напоминалки)[poisk]]['text'])
          print('[1] - Изменить \n[2] - Удалить \n[3] - Назад')
          de = input('>> ')
          if de == '1':
            print()
          elif de == '2': 
            print(напоминалки[poisk])
            poisk 
            del напоминалки[poisk]
            print(напоминалки)

        else: 
          print("такой нету"), time.sleep(1)
      time.sleep(1)


    elif de == '3': return de
    else: continue




while True:
  a = menu()
  if a == '1':
    a = zametki()
    if a == '2':
      print(заметки)
      time.sleep(1)
      continue
    elif  a == '3':
      continue
  elif a == '2':
     a = dela()
     if a == '2':
       print(напоминалки)
       time.sleep(1)
       continue
     elif a == '3':
        continue
  elif a == '3':
    exit
  else: continue

  break
  




print(заметки)
print(напоминалки)
print('stop')

time.sleep(3)
    