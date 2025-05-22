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
    result = {'sname': element_src.split('/')[-1],
              'slink': element_src,
              'state': ''}
    try:
        element = pyautogui.locateOnScreen(element_src)
        # return element
        result['state'] = 'Found'
    except pyautogui.ImageNotFoundException:
        result['state'] = 'No'
        # return False
    finally:
        return result




def locate_default_elements():
    def_elems = []
    def_elems.append(locate_element('reference_img/elems/installer_logo.png'))
    def_elems.append(locate_element('reference_img/elems/btn_screen.png'))
    def_elems.append(locate_element('reference_img/elems/btn_continue.png'))
    print(def_elems)

    if 'No' not in def_elems:
        # return True
        return 'found'
    else: 
        return False
    

async def test_screen(r_image: str, sc_name):
    img_name = (r_image.split('/'))[-1]
    window = pywinctl.getActiveWindow()
    # pyautogui.moveTo(x=int(window.left)+50, y=int(window.top)+50)
    # pyautogui.click()
    # window.maximize()
    print(window)
    a = await finder(r_image)              # need normal name

    sc = ImageGrab.grab(bbox=(int(window.left), int(window.top), int(window.left) + int(window.width), int(window.top) + int(window.height)))
    sc.save(f'results/img/{sc_name}.png')
    # print(int(window.left), int(window.top), int(window.width), int(window.height))
    # sc = ImageGrab.grab(bbox=(int(window.left), int(window.top), int(window.left) + int(window.width), int(window.top) + int(window.height)))
    # sc = ImageGrab.grab(bbox=(int(window.left), int(window.top), 100, 100))

    
    # sc = ImageGrab.grab(bbox=(0, 0, 800, 600))

    #sc.save('temp2.jpg')
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



def case_result(elems, flag, test):
    print(f'CASE RESULT DATA {elems}----{flag}-----{test}')
    # [{'sname': 'installer_logo.png', 'slink': 'reference_img/elems/installer_logo.png', 'state': 'No'}, 
    #  {'sname': 'btn_screen.png', 'slink': 'reference_img/elems/btn_screen.png', 'state': 'No'},
    #   {'sname': 'btn_continue.png', 'slink': 'reference_img/elems/btn_continue.png', 'state': 'No'}]
    # {'sname': 'warning.png', 'slink': 'reference_img/elems/warning.png', 'state': 'No'}
    # Стартовый_экран  -----test
    data = dict()
    for item in elems:

        data.update({item['sname']: item['state']})
        
        return 

    # CASE RESULT DATA [False, 'found']

    # if 'False' not in elems and flag == 'No':
    #     print(f'{test} - passed')
    #     return [True, 'Passed',f'{elems[0]}']
    
    # elif flag == 'Found':
    #     print(f'{test} - not passed')
    #     print(f'Elements {elems}')
    #     return [True, 'Not passed', f'Elements {elems}']
    
    # elif 'False' in elems:
    #     print(f'{test} - not passed')
    #     print(f'Elements {elems}')
    #     return [True, 'Not passed', f'Elements {elems}']

    # else:
    #     print(f'{test} - Blocked')
    #     print(f'Warning {flag}')
    #     return [False, 'Blocked', f'Warning {flag}']