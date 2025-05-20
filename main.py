import subprocess
import pathlib
import pyautogui
from pyautogui import ImageNotFoundException
import pywinctl
import time
from PIL import Image, ImageGrab, ImageChops
import asyncio

# from functions import goto_next_screen, check_machine, fill_field, fill_many, locate_element, locate_default_elements, move_cursor
from actions.helps import move_cursor
from actions.testcase_actions import goto_next_screen, fill_field, fill_many, locate_element, locate_default_elements, test_screen
from actions.vm_actions import check_machine, test_create_and_run_vm, start_vm

test_result = []
# r_image = 'reference_img/start_menu.png'
script_path = path_for_save = pathlib.Path().resolve() # maybe don't need

# def test_create_and_run_vm():
#     proc = subprocess.call('./create_vm.sh',  shell=True)
#     print("machine created")
#     # start_vm = subprocess.call(['VBoxManage', 'startvm', 'OSnova'])


# def start_vm(machine):
#      start_vm = subprocess.call(['VBoxManage', 'startvm', f'{machine}'])


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
    


# async def test_screen(r_image: str):
#     img_name = (r_image.split('/'))[-1]
#     window = pywinctl.getActiveWindow()
#     # pyautogui.moveTo(x=int(window.left)+50, y=int(window.top)+50)
#     # pyautogui.click()
#     # window.maximize()
#     print(window)
#     a = await finder(r_image)              # need normal name

#     sc = ImageGrab.grab()
#     sc.save(f'results/img/{img_name}')
#     # sc = ImageGrab.grab(bbox=(558, 231, 601, 801))
#     # sc.save('temp2.jpg')
#     test_result.append(f'{img_name} - ok')
#     # print(start_menu)
#     # subprocess.call(['VBoxManage', 'controlvm', 'OSnova', 'poweroff'])
#     return a
    
# async def finder(r_image: str):
#     print('start find image')
#     flag = True
#     while flag:
#         try:
#             start_menu = pyautogui.locateOnScreen(r_image) # 'reference_img/start_menu.png'
#             print(start_menu)
#             flag = False
#             return start_menu
#         except ImageNotFoundException:
#             continue
   

def test_start_menu():
    asyncio.run(test_screen('reference_img/1_start_menu.png'))
    print('Screen test - passed')
    goto_next_screen(1)

def test_licence_screen():
    elems = []
    asyncio.run(test_screen('reference_img/2_3_sc_licence.png'))
    move_cursor()
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
        

def test_user_acc_screen():
    elems = []
    pos = asyncio.run(test_screen('reference_img/acc_name.png'))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_user.png'))
    warn = locate_element('reference_img/elems/warning.png')
    # fill_field(pos, 'tester')
    print(elems)

    if 'False' not in elems and warn == False:
        print('Network user account screen - passed')
        goto_next_screen(1)

    else:
        print('Network user account screen - not passed')
        

def test_user_password_screen():
    elems = []
    pos = asyncio.run(test_screen('reference_img/new_user_pass.png'))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_user.png'))
    warn = locate_element('reference_img/elems/warning.png')
    fill_many(pos, 'q1w2e3r4')
    print(elems)

    if 'False' not in elems and warn == False:
        print('User password screen - passed')
        goto_next_screen(2)

    else:
        print('User password screen - not passed')
        

def test_timezone_screen():
    move_cursor()
    elems = []
    asyncio.run(test_screen('reference_img/timezone.png'))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_timezone.png'))
    warn = locate_element('reference_img/elems/warning.png')
    print(elems)

    if 'False' not in elems and warn == False:
        print('Timezone screen - passed')
        goto_next_screen(1)

    else:
        print('Timezone screen - not passed')
        


def test_partition_right_screen():
    elems = []
    asyncio.run(test_screen('reference_img/method_part.png'))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_part_disk.png'))
    warn = locate_element('reference_img/elems/warning.png')
    print(elems)

    if 'False' not in elems and warn == False:
        print('Partition right screen - passed')
        goto_next_screen(1)

    else:
        print('Partition right - not passed')
        

def test_partition_device_screen():
    elems = []
    asyncio.run(test_screen('reference_img/hdd_device2.png'))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_part_disk.png'))
    warn = locate_element('reference_img/elems/warning.png')
    print(elems)

    if 'False' not in elems and warn == False:
        print('Partition device screen - passed')
        goto_next_screen(1)

    else:
        print('Partition device screen - not passed')
        


def test_partition_schema_screen():
    move_cursor()
    elems = []
    asyncio.run(test_screen('reference_img/part_schem.png'))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_part_disk.png'))
    warn = locate_element('reference_img/elems/warning.png')
    print(elems)

    if 'False' not in elems and warn == False:
        print('Partition schema screen - passed')
        goto_next_screen(1)

    else:
        print('Partition schema screen - not passed')
        


if __name__ == "__main__":
    # create and start vm
    if check_machine('OSnova'):
        start_vm('OSnova')
    else:
        test_create_and_run_vm()
        start_vm('OSnova')

    test_start_menu()
    test_licence_screen()
    # test_network_screen()
    # test_network_domain_screen()
    # test_user_fullname_screen()
    # test_user_acc_screen()
    # test_user_password_screen()
    # test_timezone_screen()
    # test_partition_right_screen()
    # test_partition_device_screen()
    # test_partition_schema_screen()
