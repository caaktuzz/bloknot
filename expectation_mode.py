# блокнот / expectation / version: 1.1 / 22.08.2026 / caktuz

import os
import sys
import json
import time
import datetime
from plyer import notification  # pip install plyer

# pyinstaller convertation : pyinstaller --noconfirm --onefile --windowed --hidden-import "plyer.platforms.win.notification" "<директория>"
# флаг --hidden-import обязатяльно для того чтобы в компиляцию были включены все сторонние библиотеки

general = { "заметки" : {},
            "напоминалки" : {} }


def write() : # запись 
  with open('bloknot_data.json', 'w', encoding='utf-8') as file:  
    json.dump(general, file, ensure_ascii=False, indent=2)
def read() : # чтение 
  try: 
    with open('bloknot_data.json', 'r', encoding='utf-8') as file:
      data = json.load(file)
      general.clear()
      general.update(data)
  except FileNotFoundError: 
    print('файл "bloknot_data.json" не найден'), time.sleep(1)
    _write = write()

def _notification(nap):
  notification.notify(
    title= "Напоминалка",
    message=general['напоминалки'][nap]['text'],
    app_name='bloknot',
    app_icon=r'sahur-logo.ico',
    timeout=100 ) 


def main() :
    while True:
      try: 
          _read = read()
          dt_now = str(datetime.datetime.now())[:-7]
          time.sleep(1)
          for nap in general['напоминалки']:
              #print(f"\r {dt_now}  {general['напоминалки'][nap]}", end="", flush=True)
              if general['напоминалки'][nap]['dt_end'] == dt_now:
                  _notification(nap)
                  break
              time.sleep(0.1)
      except KeyboardInterrupt: break

_main = main()