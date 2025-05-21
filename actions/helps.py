import pyautogui
import pywinctl
from datetime import datetime



reps = str.maketrans({":": "-", " ": "-"})
stamp = str(datetime.now()).translate(reps).split('.')[0]

def move_cursor():
    window = pywinctl.getActiveWindow()
    pyautogui.moveTo(x=int(window.left)+50, y=int(window.top)+50)
    pyautogui.click()
    print('cursor_pos ', pyautogui.position())
    # window.maximize()
    print(window)

def write_to_report(data: list, tname: str):
    length = len(data)

    with open('results/reports/report.html', 'a') as file:
        file.write(f'<tr><td>{tname}</td><td>{data[1]}</td><td><td>ok</td><td><img src="../img/{tname}.png" width="400" height="325"></td></tr>\n')
        # file.write(f'{str(data)}')