import os
import time


list_modules = ['gtts', 'pygame', 'speech_recognition', 'requests', 'mutagen', 'pyautogui', 'easygui']
list_pips = ["gtts", 'pygame', "speech_recognition", "requests", 'mutagen', 'pyautogui', 'easygui']
list_nti = []
install = False

for _ in list_modules:
    "Check work module"

    try:
        exec(f'import {_}')
    except ImportError:
        list_nti.append(_)
        install = True

if install == True:
    "Installing modules"

    print('|█                    |10%')
    time.sleep(0.01)
    print('|██                   |13%')
    time.sleep(0.01)
    print('|███                  |16%')
    time.sleep(0.01)
    print('|████                 |21%')
    time.sleep(0.01)
    print('|█████                |34%')
    time.sleep(0.01)
    print('|██████               |36%')
    time.sleep(0.01)
    print('|████████             |40%')
    time.sleep(0.01)
    print('|████████             |43%')
    time.sleep(0.01)
    print('|█████████            |45%')
    time.sleep(0.01)
    print('|███████████          |52%')
    time.sleep(0.01)
    print('|█████████████        |63%')
    time.sleep(0.01)
    print('|███████████████      |75%')
    time.sleep(0.01)
    print('|██████████████████   |87%')
    time.sleep(6)
    i = 0
    for _ in list_nti:
        i = i + 1
        pip_imp = list_modules.index(_)
        os.system(f'pip install {list_pips[int(pip_imp)]} --quiet --disable-pip-version-check')
        print(f'\nInstalled [{i} in {len(list_nti)}]. . .\n')
    time.sleep(3)
    print('|█████████████████████|100% /', end = '')
    time.sleep(0.2)
    print('\r|█████████████████████|100% -', end = '')
    time.sleep(0.2)
    print('\r|█████████████████████|100% \\', end = '')
    time.sleep(0.2)
    print('\r|█████████████████████|100% |', end = '')
    time.sleep(0.2)
    print('\r|█████████████████████|100% -', end = '')
    time.sleep(0.2)
    print('\r|█████████████████████|100% \\', end = '')
    time.sleep(0.2)
    print('\r|█████████████████████|Готово.\n', end = '')
    time.sleep(0.2)