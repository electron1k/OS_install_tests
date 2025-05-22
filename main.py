import subprocess
import pathlib
import pyautogui
from pyautogui import ImageNotFoundException
import pywinctl
import time
from PIL import Image, ImageGrab, ImageChops
import asyncio

from actions.helps import move_cursor, write_to_report, report_finaliztion, create_report_file, show_report
from actions.testcase_actions import goto_next_screen, fill_field, fill_many, locate_element, locate_default_elements, test_screen, case_result
from actions.vm_actions import check_machine, test_create_and_run_vm, start_vm

# test_result = []
screen_test_template = {
    'test_name': 'Стартовый_экран',
    'elem_wait': 'reference_img/1_start_menu.png',
    'elems_needed': ['reference_img/elems/installer_logo.png', 
                     'reference_img/elems/btn_screen.png',
                     'reference_img/elems/btn_continue.png',
                     ],
    'warn':'reference_img/elems/warning.png'
    }

def template_test(template: dict):
    tname = template['test_name']
    elems = []
    asyncio.run(test_screen(template['elem_wait'], tname))
    for item in template['elems_needed']:
        loc = locate_element(item)
        print(loc)
        elems.append(locate_element(item))
    warn = locate_element(template['warn'])
    print(warn)
    # print(elems)

    tresult = case_result(elems, warn, tname)
    

    # if tresult[0] == True:
    #     write_to_report(tresult, tname)
    #     # goto_next_screen(1)
    # else:
    #     write_to_report(tresult, tname)
    #     print(f'{tresult[1]}. Reason {tresult[2]}')



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
    elems.append(locate_element('reference_img/elems/sign_licence.png'))
    warn = locate_element('reference_img/elems/warning.png')
    print(elems)

    tresult = case_result(elems, warn, tname)

    if tresult[0] == True:
        write_to_report(tresult, tname)
        goto_next_screen(1)

    else:
        write_to_report(tresult, tname)
        print(f'{tresult[1]}. Reason {tresult[2]}')


def test_network_screen():
    tname = test_network_screen.__name__
    elems = []
    pos = asyncio.run(test_screen('reference_img/computer_name.png', tname))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_network.png'))
    warn = locate_element('reference_img/elems/warning.png')
    fill_field(pos, 'AUTOTEST')
    print(elems)
    tresult = case_result(elems, warn, tname)

    if tresult[0] == True:
        write_to_report(tresult, tname)
        goto_next_screen(1)

    else:
        write_to_report(tresult, tname)
        print(f'{tresult[1]}. Reason {tresult[2]}')


def test_network_domain_screen():
    tname = test_network_domain_screen.__name__
    elems = []
    pos = asyncio.run(test_screen('reference_img/domain_name.png', tname))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_network.png'))
    warn = locate_element('reference_img/elems/warning.png')
    print(elems)

    tresult = case_result(elems, warn, tname)

    if tresult[0] == True:
        write_to_report(tresult, tname)
        goto_next_screen(1)

    else:
        write_to_report(tresult, tname)
        print(f'{tresult[1]}. Reason {tresult[2]}')
        


def test_user_fullname_screen():
    tname = test_user_fullname_screen.__name__
    elems = []
    pos = asyncio.run(test_screen('reference_img/user_name.png', tname))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_network.png'))
    warn = locate_element('reference_img/elems/warning.png')
    fill_field(pos, 'tester')
    print(elems)

    tresult = case_result(elems, warn, tname)
    
    if tresult[0] == True:
        write_to_report(tresult, tname)
        goto_next_screen(1)

    else:
        write_to_report(tresult, tname)
        print(f'{tresult[1]}. Reason {tresult[2]}')
        

def test_user_acc_screen():
    tname = test_user_acc_screen.__name__
    elems = []
    pos = asyncio.run(test_screen('reference_img/acc_name.png', tname))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_user.png'))
    warn = locate_element('reference_img/elems/warning.png')
    print(elems)

    tresult = case_result(elems, warn, tname)
    
    if tresult[0] == True:
        write_to_report(tresult, tname)
        goto_next_screen(1)

    else:
        write_to_report(tresult, tname)
        print(f'{tresult[1]}. Reason {tresult[2]}')
        

def test_user_password_screen():
    tname = test_user_password_screen.__name__
    elems = []
    pos = asyncio.run(test_screen('reference_img/new_user_pass.png', tname))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_user.png'))
    warn = locate_element('reference_img/elems/warning.png')
    fill_many(pos, 'q1w2e3r4')
    print(elems)

    tresult = case_result(elems, warn, tname)
    
    if tresult[0] == True:
        write_to_report(tresult, tname)
        goto_next_screen(1)

    else:
        write_to_report(tresult, tname)
        print(f'{tresult[1]}. Reason {tresult[2]}')
        

def test_timezone_screen():
    move_cursor()
    tname = test_timezone_screen.__name__
    elems = []
    asyncio.run(test_screen('reference_img/timezone.png', tname))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_timezone.png'))
    warn = locate_element('reference_img/elems/warning.png')
    print(elems)

    tresult = case_result(elems, warn, tname)
    
    if tresult[0] == True:
        write_to_report(tresult, tname)
        goto_next_screen(1)

    else:
        write_to_report(tresult, tname)
        print(f'{tresult[1]}. Reason {tresult[2]}')
        


def test_partition_right_screen():
    tname = test_partition_right_screen.__name__
    elems = []
    asyncio.run(test_screen('reference_img/method_part.png', tname))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_part_disk.png'))
    warn = locate_element('reference_img/elems/warning.png')
    print(elems)

    tresult = case_result(elems, warn, tname)
    
    if tresult[0] == True:
        write_to_report(tresult, tname)
        goto_next_screen(1)

    else:
        write_to_report(tresult, tname)
        print(f'{tresult[1]}. Reason {tresult[2]}')
        

def test_partition_device_screen():
    tname = test_partition_device_screen.__name__
    elems = []
    asyncio.run(test_screen('reference_img/hdd_device2.png', tname))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_part_disk.png'))
    warn = locate_element('reference_img/elems/warning.png')
    print(elems)

    tresult = case_result(elems, warn, tname)
    
    if tresult[0] == True:
        write_to_report(tresult, tname)
        goto_next_screen(1)

    else:
        write_to_report(tresult, tname)
        print(f'{tresult[1]}. Reason {tresult[2]}')
        


def test_partition_schema_screen():
    tname = test_partition_schema_screen.__name__
    move_cursor()
    elems = []
    asyncio.run(test_screen('reference_img/part_schem.png', tname))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_part_disk.png'))
    warn = locate_element('reference_img/elems/warning.png')
    print(elems)

    tresult = case_result(elems, warn, tname)
    
    if tresult[0] == True:
        write_to_report(tresult, tname)
        goto_next_screen(1)

    else:
        write_to_report(tresult, tname)
        print(f'{tresult[1]}. Reason {tresult[2]}')


def test_partition_final_screen():
    tname = test_partition_final_screen.__name__
    move_cursor()
    elems = []
    asyncio.run(test_screen('reference_img/finish_part.png', tname))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_part_disk.png'))
    warn = locate_element('reference_img/elems/warning.png')
    print(elems)

    tresult = case_result(elems, warn, tname)
    
    if tresult[0] == True:
        write_to_report(tresult, tname)
        goto_next_screen(1)

    else:
        write_to_report(tresult, tname)
        print(f'{tresult[1]}. Reason {tresult[2]}')

def test_partition_confirm_screen():
    tname = test_partition_confirm_screen.__name__
    move_cursor()
    elems = []
    asyncio.run(test_screen('reference_img/write_changes.png', tname))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_part_disk.png'))
    warn = locate_element('reference_img/elems/warning.png')
    pyautogui.press('Down')
    print(elems)

    tresult = case_result(elems, warn, tname)
    
    if tresult[0] == True:
        write_to_report(tresult, tname)
        goto_next_screen(1)

    else:
        write_to_report(tresult, tname)
        print(f'{tresult[1]}. Reason {tresult[2]}')

def test_protect_level_screen():
    tname = test_protect_level_screen.__name__
    move_cursor()
    elems = []
    asyncio.run(test_screen('reference_img/protect_level.png', tname))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_protect.png'))
    warn = locate_element('reference_img/elems/warning.png')
    print(elems)

    tresult = case_result(elems, warn, tname)
    
    if tresult[0] == True:
        write_to_report(tresult, tname)
        goto_next_screen(1)

    else:
        write_to_report(tresult, tname)
        print(f'{tresult[1]}. Reason {tresult[2]}')

# Here are long proc of installing base system. Not sample case!!!!! 

def test_kernel_screen():
    tname = test_kernel_screen.__name__
    move_cursor()
    elems = []
    asyncio.run(test_screen('reference_img/kernel.png', tname))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/base_system.png'))
    warn = locate_element('reference_img/elems/warning.png')
    print(elems)

    tresult = case_result(elems, warn, tname)
    
    if tresult[0] == True:
        write_to_report(tresult, tname)
        goto_next_screen(1)

    else:
        write_to_report(tresult, tname)
        print(f'{tresult[1]}. Reason {tresult[2]}')


def test_os_role_screen():# neeed redact
    tname = test_os_role_screen.__name__
    move_cursor()
    elems = []
    asyncio.run(test_screen('reference_img/choose_role.png', tname))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_role.png'))
    warn = locate_element('reference_img/elems/warning.png')
    print(elems)

    tresult = case_result(elems, warn, tname)
    
    if tresult[0] == True:
        write_to_report(tresult, tname)
        goto_next_screen(1)

    else:
        write_to_report(tresult, tname)
        print(f'{tresult[1]}. Reason {tresult[2]}')

def test_package_source_screen():# neeed redact
    tname = test_package_source_screen.__name__
    move_cursor()
    elems = []
    asyncio.run(test_screen('reference_img/scan_source.png', tname))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_package.png'))
    warn = locate_element('reference_img/elems/warning.png')
    print(elems)

    tresult = case_result(elems, warn, tname)
    
    if tresult[0] == True:
        write_to_report(tresult, tname)
        goto_next_screen(1)

    else:
        write_to_report(tresult, tname)
        print(f'{tresult[1]}. Reason {tresult[2]}')


def test_programms_screen():# neeed redact
    tname = test_programms_screen.__name__
    move_cursor()
    elems = []
    asyncio.run(test_screen('reference_img/choose_progs.png', tname))
    elems.append(locate_default_elements())
    elems.append(locate_element('reference_img/elems/sign_programms.png'))
    warn = locate_element('reference_img/elems/warning.png')
    print(elems)
    for _ in range(10):
        pyautogui.press("Down")
    pyautogui.press("Space")
    
    tresult = case_result(elems, warn, tname)
    
    if tresult[0] == True:
        write_to_report(tresult, tname)
        goto_next_screen(1)

    else:
        write_to_report(tresult, tname)
        print(f'{tresult[1]}. Reason {tresult[2]}')

if __name__ == "__main__":
    # create and start vm
    if check_machine('OSnova'):
        start_vm('OSnova')
    else:
        test_create_and_run_vm()
        start_vm('OSnova')


    template_test(screen_test_template)
    show_report()
    # test_start_menu()
    # test_licence_screen()
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
    # test_partition_confirm_screen()
