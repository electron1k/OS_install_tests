import subprocess
import pathlib
import pyautogui
from pyautogui import ImageNotFoundException
import pywinctl
import time
from PIL import Image, ImageGrab, ImageChops
import asyncio

from actions.helps import move_cursor, write_to_report
from actions.testcase_actions import goto_next_screen, fill_field, fill_many, locate_element, locate_default_elements, test_screen, case_result
from actions.vm_actions import check_machine, test_create_and_run_vm, start_vm

# test_result = []


def test_start_menu():
    tname = test_start_menu.__name__
    elems = []
    asyncio.run(test_screen('reference_img/1_start_menu.png', tname))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/start_logo.png'))
    warn = locate_element('reference_img/elems/warning.png')
    print(elems)

    tresult = case_result(elems, warn, tname)

    if tresult[0] == True:
        write_to_report(tresult, tname)
        goto_next_screen(1)

    else:
        write_to_report(tresult, tname)
        print(f'{tresult[1]}. Reason {tresult[2]}')
    

def test_licence_screen():
    tname = test_licence_screen.__name__
    elems = []
    asyncio.run(test_screen('reference_img/2_3_sc_licence.png', tname))
    move_cursor()
    elems.append(locate_default_elements())
    warn = locate_element('reference_img/elems/warning.png')
    print(elems)

    tresult = case_result(elems, warn, tname)

    if tresult[0] == True:
        write_to_report(tresult, tname)
        goto_next_screen(1)

    else:
        write_to_report(tresult)
        print(f'{tresult[1]}. Reason {tresult[2]}')


def test_network_screen():
    elems = []
    pos = asyncio.run(test_screen('reference_img/computer_name.png'), test_network_screen.__name__)
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
    pos = asyncio.run(test_screen('reference_img/domain_name.png', test_network_domain_screen.__name__))
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
    test_name = test_user_fullname_screen.__name__
    elems = []
    pos = asyncio.run(test_screen('reference_img/user_name.png', test_name))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_network.png'))
    warn = locate_element('reference_img/elems/warning.png')
    fill_field(pos, 'tester')
    print(elems)

    if 'False' not in elems and warn == False:
        print('Network user full name screen - passed')
        goto_next_screen(1)

    elif warn == False:
        print('User account screen - not passed')
        print(f'Elements {elems}')
        goto_next_screen(1)

    else:
        print('User account screen - Blocked')
        print(f'Warning {warn}')
        

def test_user_acc_screen():
    test_name = test_user_acc_screen.__name__
    elems = []
    pos = asyncio.run(test_screen('reference_img/acc_name.png', test_name))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_user.png'))
    warn = locate_element('reference_img/elems/warning.png')
    # fill_field(pos, 'tester')
    print(elems)

    if 'False' not in elems and warn == False:
        print('User account screen - passed')
        goto_next_screen(1)

    elif warn == False:
        print('User account screen - not passed')
        print(f'Elements {elems}')
        goto_next_screen(1)

    else:
        print('User account screen - Blocked')
        print(f'Warning {warn}')
        

def test_user_password_screen():
    test_name = test_user_password_screen.__name__
    elems = []
    pos = asyncio.run(test_screen('reference_img/new_user_pass.png', test_name))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_user.png'))
    warn = locate_element('reference_img/elems/warning.png')
    fill_many(pos, 'q1w2e3r4')
    print(elems)

    if 'False' not in elems and warn == False:
        print('User password screen - passed')
        goto_next_screen(2)

    elif warn == False:
        print('User password screen - not passed')
        print(f'Elements {elems}')
        goto_next_screen(2)

    else:
        print('User password screen - Blocked')
        print(f'Warning {warn}')
        

def test_timezone_screen():
    move_cursor()
    elems = []
    asyncio.run(test_screen('reference_img/timezone.png', test_timezone_screen.__name__))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_timezone.png'))
    warn = locate_element('reference_img/elems/warning.png')
    print(elems)

    if 'False' not in elems and warn == False:
        print('Timezone screen - passed')
        goto_next_screen(1)

    elif warn == False:
        print('Timezone screen - not passed')
        print(f'Elements {elems}')
        goto_next_screen(1)

    else:
        print('Timezone screen screen - Blocked')
        print(f'Warning {warn}')
        


def test_partition_right_screen():
    elems = []
    asyncio.run(test_screen('reference_img/method_part.png', test_partition_right_screen.__name__))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_part_disk.png'))
    warn = locate_element('reference_img/elems/warning.png')
    print(elems)

    if 'False' not in elems and warn == False:
        print('Partition right screen - passed')
        goto_next_screen(1)

    elif warn == False:
        print('Partition right screen - not passed')
        print(f'Elements {elems}')
        goto_next_screen(1)

    else:
        print('Partition right screen - Blocked')
        print(f'Warning {warn}')
        

def test_partition_device_screen():
    elems = []
    asyncio.run(test_screen('reference_img/hdd_device2.png', test_partition_device_screen.__name__))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_part_disk.png'))
    warn = locate_element('reference_img/elems/warning.png')
    print(elems)

    if 'False' not in elems and warn == False:
        print('Partition device screen - passed')
        goto_next_screen(1)

    elif warn == False:
        print('Partition device screen - not passed')
        print(f'Elements {elems}')
        goto_next_screen(1)

    else:
        print('Partition device screen - Blocked')
        print(f'Warning {warn}')
        


def test_partition_schema_screen():
    move_cursor()
    elems = []
    asyncio.run(test_screen('reference_img/part_schem.png', test_partition_schema_screen.__name__))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_part_disk.png'))
    warn = locate_element('reference_img/elems/warning.png')
    print(elems)

    if 'False' not in elems and warn == False:
        print('Partition schema screen - passed')
        goto_next_screen(1)

    elif warn == False:
        print('Partition schema screen - not passed')
        print(f'Elements {elems}')
        goto_next_screen(1)

    else:
        print('Partition final screen - Blocked')
        print(f'Warning {warn}')


def test_partition_final_screen():
    move_cursor()
    elems = []
    asyncio.run(test_screen('reference_img/finish_part.png', test_partition_final_screen.__name__))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_part_disk.png'))
    warn = locate_element('reference_img/elems/warning.png')
    print(elems)

    if 'False' not in elems and warn == False:
        print('Partition final screen - passed')
        goto_next_screen(1)

    elif warn == False:
        print('Partition final screen - not passed')
        print(f'Elements {elems}')
        goto_next_screen(1)

    else:
        print('Partition final screen - Blocked')
        print(f'Warning {warn}')


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
    # test_partition_final_screen()