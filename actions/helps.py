import pyautogui
import pywinctl

def move_cursor():
    window = pywinctl.getActiveWindow()
    pyautogui.moveTo(x=int(window.left)+50, y=int(window.top)+50)
    pyautogui.click()
    print('cursor_pos ', pyautogui.position())
    # window.maximize()
    print(window)