import pyautogui
import time
import pywinctl
from PIL import Image, ImageGrab, ImageChops
import asyncio


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
    

async def test_screen(r_image: str):
    img_name = (r_image.split('/'))[-1]
    window = pywinctl.getActiveWindow()
    # pyautogui.moveTo(x=int(window.left)+50, y=int(window.top)+50)
    # pyautogui.click()
    # window.maximize()
    print(window)
    a = await finder(r_image)              # need normal name

    sc = ImageGrab.grab()
    sc.save(f'results/img/{img_name}')
    # sc = ImageGrab.grab(bbox=(int(window.left), int(window.top), int(window.width), int(window.height)))
    sc = ImageGrab.grab(bbox=(0, 0, 800, 600))

    sc.save('temp2.jpg')
    # test_result.append(f'{img_name} - ok')
    # print(start_menu)
    # subprocess.call(['VBoxManage', 'controlvm', 'OSnova', 'poweroff'])
    return a
    
async def finder(r_image: str):
    print('start find image')
    flag = True
    while flag:
        try:
            start_menu = pyautogui.locateOnScreen(r_image) # 'reference_img/start_menu.png'
            print(start_menu)
            flag = False
            return start_menu
        except pyautogui.ImageNotFoundException:
            continue