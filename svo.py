# блокнот / version: 1.0 / 

import time
import datetime
now = datetime.datetime.now()
print(now)

заметки = { 1:{'num':1, 'dt': '2026-06-09','text': 'запись 1'},
            2:{'num':2, 'dt': '09.06.2026','text': 'запись 2'},
            3:{'num':3, 'dt': '09.06.2026','text': 'запись 3'}  }

напоминалки = { 1:{'num':1, 'dt': '09.06.2026','text': 'запись 1'},
                2:{'num':2, 'dt': '09.06.2026','text': 'запись 2'},
                3:{'num':3, 'dt': '09.06.2026','text': 'запись 3'}  }

def menu(): # Главное меню
    print('[1] - Заметки')
    print('[2] - Списки дел')
    de = input('>> ')
    return de
    
def zametki():# Заметки
    last_zametki = list(заметки)[-1],# list(заметки)[-2], list(заметки)[-3]
    print('Последние напоминалки: \n', last_zametki[0])
    print('[1] - Новая заметка')
    print('[2] - Назад')
    de = input('>> ')
    return de

def dela(): # Напоминалки
    if len(list(напоминалки)) >= 3: last_dela = напоминалки[list(напоминалки)[-1]], напоминалки[list(напоминалки)[-2]], напоминалки[list(напоминалки)[-3]]
    elif len(list(напоминалки)) == 2: last_dela = list(напоминалки)[-1], list(напоминалки)[-2]
    elif len(list(напоминалки)) == 1: last_dela = list(напоминалки)[-1]
    elif len(list(напоминалки)) <= 0: last_dela = "Список пуст."
    print(last_dela)
    print('Последние напоминалки: \n', напоминалки[last_dela[0]], напоминалки[last_dela[1]], напоминалки[last_dela[2]])
    print('[1] - Новое напоминание')
    print('[2] - Назад')
    de = input('>> ')
    return de

dela()

    