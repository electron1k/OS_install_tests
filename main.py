import subprocess
import pathlib
import pyautogui
from pyautogui import ImageNotFoundException
import pywinctl
import time
from PIL import Image, ImageGrab, ImageChops
import asyncio

from functions import goto_next_screen, check_machine, fill_field, fill_many, locate_element, locate_default_elements

test_result = []
# r_image = 'reference_img/start_menu.png'
script_path = path_for_save = pathlib.Path().resolve() # maybe don't need

def test_create_and_run_vm():
    proc = subprocess.call('./create_vm.sh',  shell=True)
    print("machine created")
    # start_vm = subprocess.call(['VBoxManage', 'startvm', 'OSnova'])


def start_vm(machine):
     start_vm = subprocess.call(['VBoxManage', 'startvm', f'{machine}'])


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
    a = await finder(r_image)              # need normal name

    sc = ImageGrab.grab()
    sc.save(f'results/img/{img_name}')
    # sc = ImageGrab.grab(bbox=(558, 231, 601, 801))
    # sc.save('temp2.jpg')
    test_result.append(f'{img_name} - ok')
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
        except ImageNotFoundException:
            continue
   

def test_start_menu():
    asyncio.run(test_screen('reference_img/1_start_menu.png'))
    print('Screen test - passed')
    goto_next_screen(1)

def test_licence_screen():
    elems = []
    asyncio.run(test_screen('reference_img/2_3_sc_licence.png'))
    elems.append(locate_default_elements())
    warn = locate_element('reference_img/elems/warning.png')
    print(elems)

    if 'False' not in elems and warn == False:
        print('Licence screen - passed')
        goto_next_screen(1)

    else:
        print('Licence screen - not passed')
        goto_next_screen(1)


def test_network_screen():
    elems = []
    pos = asyncio.run(test_screen('reference_img/computer_name.png'))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_network.png'))
    warn = locate_element('reference_img/elems/warning.png')
    fill_field(pos, 'AUTOTEST')
    print(elems)

    if 'False' not in elems and warn == False:
        print('Network screen - passed')
        goto_next_screen(1)

    else:
        print('Network screen - not passed')
        goto_next_screen(1)

def test_network_domain_screen():
    elems = []
    pos = asyncio.run(test_screen('reference_img/domain_name.png'))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_network.png'))
    warn = locate_element('reference_img/elems/warning.png')
    # fill_field(pos, 'AUTOTEST')
    print(elems)

    if 'False' not in elems and warn == False:
        print('Network domain screen - passed')
        goto_next_screen(1)

    else:
        print('Network domain screen - not passed')
        goto_next_screen(1)


def test_user_fullname_screen():
    elems = []
    pos = asyncio.run(test_screen('reference_img/user_name.png'))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_network.png'))
    warn = locate_element('reference_img/elems/warning.png')
    fill_field(pos, 'tester')
    print(elems)

    if 'False' not in elems and warn == False:
        print('Network user full name screen - passed')
        goto_next_screen(1)

    else:
        print('Network user full name screen - not passed')
        goto_next_screen(1)

def test_user_acc_screen():
    good_elems = []
    pos = asyncio.run(test_screen('reference_img/acc_name.png'))
    good_elems.append(locate_element('reference_img/elems/installer_logo.png'))
    good_elems.append(locate_element('reference_img/elems/btn_screen.png'))
    good_elems.append(locate_element('reference_img/elems/btn_continue.png'))
    good_elems.append(locate_element('reference_img/elems/sign_user.png'))
    warn = locate_element('reference_img/elems/warning.png')
    # fill_field(pos, 'tester')
    print(good_elems)

    if 'False' not in good_elems and warn == False:
        print('Network user account screen - passed')
        goto_next_screen(1)

    else:
        print('Network user account screen - not passed')
        goto_next_screen(1)

def test_user_password_screen():
    good_elems = []
    pos = asyncio.run(test_screen('reference_img/new_user_pass.png'))
    good_elems.append(locate_element('reference_img/elems/installer_logo.png'))
    good_elems.append(locate_element('reference_img/elems/btn_screen.png'))
    good_elems.append(locate_element('reference_img/elems/btn_continue.png'))
    good_elems.append(locate_element('reference_img/elems/sign_user.png'))
    warn = locate_element('reference_img/elems/warning.png')
    fill_many(pos, 'q1w2e3r4')
    print(good_elems)

    if 'False' not in good_elems and warn == False:
        print('User password screen - passed')
        goto_next_screen(2)

    else:
        print('User password screen - not passed')
        goto_next_screen(2)

def test_timezone_screen():
    good_elems = []
    pos = asyncio.run(test_screen('reference_img/timezone.png'))
    good_elems.append(locate_element('reference_img/elems/installer_logo.png'))
    good_elems.append(locate_element('reference_img/elems/btn_screen.png'))
    good_elems.append(locate_element('reference_img/elems/btn_continue.png'))
    good_elems.append(locate_element('reference_img/elems/sign_timezone.png'))
    warn = locate_element('reference_img/elems/warning.png')
    fill_many(pos, 'q1w2e3r4')
    print(good_elems)

    if 'False' not in good_elems and warn == False:
        print('Network user account screen - passed')
        goto_next_screen(1)

    else:
        print('Network user account screen - not passed')
        goto_next_screen(1)






if __name__ == "__main__":
    # create and start vm
    if check_machine('OSnova'):
        start_vm('OSnova')
    else:
        test_create_and_run_vm()
        start_vm('OSnova')

    test_start_menu()
    test_licence_screen()
    test_network_screen()
    test_network_domain_screen()
    test_user_fullname_screen()
    test_user_acc_screen()
    test_user_password_screen()
    


