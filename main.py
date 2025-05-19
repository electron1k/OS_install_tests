import subprocess
import pathlib
import pyautogui
from pyautogui import ImageNotFoundException
import pywinctl
import time
from PIL import Image, ImageGrab, ImageChops
import asyncio

test_result = []
# r_image = 'reference_img/start_menu.png'
script_path = path_for_save = pathlib.Path().resolve() # maybe don't need

def test_create_and_run_vm():
    # proc = subprocess.call('./create_vm.sh',  shell=True)
    print("machine created")
    start_vm = subprocess.call(['VBoxManage', 'startvm', 'OSnova'])
    # result = subprocess.check_output(['VBoxManage', 'list', 'runningvms'], shell=False, stdout=subprocess.PIPE)
    result = subprocess.check_output(['VBoxManage', 'list', 'runningvms'], shell=False)
    print(result)
    # assert result == 0

# def capture_image():
#     window = pywinctl.getActiveWindow()
#     window.maximize()
#     print(window)
#     # time.sleep(5)
#     flag = True
#     while flag:
#         try:
#             print(f'flag {flag}')
#             print('works try')
#             start_menu = pyautogui.locateOnScreen('reference_img/start_menu.png')
#             print(start_menu)
#             flag = False
            
#         except ImageNotFoundException:
#             # print(f'flag {flag}')
#             # print("Not found reference image")
#             # # print(start_menu)
#             # counter += 1
#             continue
#         else:
#             # print(f'flag {flag}')
#             # print('works else')
#             flag = False
        
    # sc = ImageGrab.grab()
    # sc.save('results/img/test_start_menu.jpg')
    # sc = ImageGrab.grab(bbox=(558, 231, 601, 801))
    # sc.save('temp2.jpg')
    # # print(start_menu)
    # subprocess.call(['VBoxManage', 'controlvm', 'OSnova', 'poweroff'])

async def finder(r_image: str):
    print('start find image')
    flag = True
    while flag:
        try:
            start_menu = pyautogui.locateOnScreen(r_image) # 'reference_img/start_menu.png'
            print(start_menu)
            flag = False
            return True
        except ImageNotFoundException:
            continue
    


async def test_screen(r_image: str):
    img_name = (r_image.split('/'))[-1]
    window = pywinctl.getActiveWindow()
    # window.maximize()
    print(window)
    a = await finder(r_image)

    sc = ImageGrab.grab()
    sc.save(f'results/img/{img_name}')
    # sc = ImageGrab.grab(bbox=(558, 231, 601, 801))
    # sc.save('temp2.jpg')
    test_result.append(f'{img_name} - ok')
    # print(start_menu)
    # subprocess.call(['VBoxManage', 'controlvm', 'OSnova', 'poweroff'])
    
async def finder(r_image: str):
    print('start find image')
    flag = True
    while flag:
        try:
            start_menu = pyautogui.locateOnScreen(r_image) # 'reference_img/start_menu.png'
            print(start_menu)
            flag = False
            return start_menu
        except ImageNotFoundException:
            continue
   
def goto_next_screen():
    pyautogui.press('Tab')
    time.sleep(0.5)
    pyautogui.press('Enter')



if __name__ == "__main__":

    test_create_and_run_vm()
    asyncio.run(test_screen('reference_img/start_menu.png'))
    goto_next_screen()
    # print(asyncio.run(finder('reference_img/logo_st_sc.png')))
    print(test_result)

    #start vm
    # ensure start_menu ok
    # press enter
    # ensure license + logo
    # press Tab -> activate button Продолжить and press enter - many times(goto_next_screen)
    # ensure Network - machine name 
    # input AUTOTEST in machine name field
