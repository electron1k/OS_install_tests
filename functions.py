import pyautogui
import time
import subprocess



#Actions in test-case

def goto_next_screen(tabs: int):
    for _ in range(tabs):
        pyautogui.press('Tab')
    time.sleep(0.5)
    pyautogui.press('Enter')

def fill_field(elem, text):
    pyautogui.click(x=(int(elem.left) + 100), y=(int(elem.top) + 100), button='left')
    pyautogui.write(text)
    time.sleep(1)

def fill_many(elem, text):
    pyautogui.click(x=(int(elem.left) + 100), y=(int(elem.top) + 100), button='left')
    pyautogui.write(text)
    time.sleep(0.2)
    pyautogui.press('Tab')
    time.sleep(0.2)
    pyautogui.press('Tab')
    time.sleep(0.2)
    pyautogui.write(text)
    time.sleep(1)

def locate_element(element_src: str):
    try:
        element = pyautogui.locateOnScreen(element_src)
        return element
    except pyautogui.ImageNotFoundException:
        return False

def locate_default_elements():
    def_elems = []
    def_elems.append(locate_element('reference_img/elems/installer_logo.png'))
    def_elems.append(locate_element('reference_img/elems/btn_screen.png'))
    def_elems.append(locate_element('reference_img/elems/btn_continue.png'))

    if 'False' not in def_elems:
        return True
    else: 
        return False

#Actions with machine

def check_machine(machine_name):
    proc = subprocess.check_output(['VBoxManage', 'list', 'vms'], text=True)
    # print(proc)
    if machine_name in proc:
        return True
    else:
        return False

# check_machine()
# tabs = 2
# for _ in range(tabs):
#     print('ok')

# while True:
#     pyautogui.screenshot()
#     time.sleep(5)