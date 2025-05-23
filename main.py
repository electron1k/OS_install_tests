import subprocess
import pathlib
import pyautogui
from pyautogui import ImageNotFoundException
import pywinctl
import time
from PIL import Image, ImageGrab, ImageChops
import asyncio

from actions.helps import move_cursor, write_to_report, report_finaliztion, create_report_file, show_report
from actions.testcase_actions import goto_next_screen, fill_field, fill_many, locate_element, test_screen, case_result
from actions.vm_actions import check_machine, test_create_and_run_vm, start_vm

# test_result = []
# screen_test_template = {
#     'test_name': 'Стартовый_экран',
#     'elem_wait': 'reference_img/1_start_menu.png',
#     'elems_needed': ['reference_img/elems/installer_logo.png', 
#                      'reference_img/elems/btn_screen.png',
#                      'reference_img/elems/btn_continue.png',
#                      ],
#     'warn':'reference_img/elems/warning.png'
#     }

from testcase_template.template import (screen_test_template, 
                                        screen_licence, 
                                        screen_network, 
                                        screen_network_domain, 
                                        screen_acc, 
                                        screen_username,
                                        screen_user_password,
                                        screen_timezone,
                                        screen_partition_right,
                                        screen_partition_device)

from testcase_template.test import tests

def template_test(template: dict):
    tname = template['test_name']
    elems = []
    
    asyncio.run(test_screen(template['elem_wait'], tname))

    move_cursor()
    for item in template['elems_needed']:
        elems.append(locate_element(item))

    warn = locate_element(template['warn'])
    tresult = case_result(elems, warn, tname)

    if template['fill_field'] != '':
        for img in template['field_location_ref']:
            print(img)
            ref = locate_element(img)
            print(ref)
            fill_field(ref['obj'], template['fill_field'])


    write_to_report(tresult)



if __name__ == "__main__":
    # create and start vm
    if check_machine('OSnova'):
        start_vm('OSnova')
    else:
        test_create_and_run_vm()
        start_vm('OSnova')

    for item in tests:
        
        if item['test_name'] == 'Настройка_учетных_записей-Пароль':
            template_test(item)
            goto_next_screen(2)

        else:
            template_test(item)
            goto_next_screen(1)

    # template_test(screen_test_template)
    # goto_next_screen(1)
    # template_test(screen_licence)
    # goto_next_screen(1)
    # template_test(screen_network)
    # goto_next_screen(1)
    # template_test(screen_network_domain)
    # goto_next_screen(1)
    # template_test(screen_username)
    # goto_next_screen(1)
    # template_test(screen_acc)
    # goto_next_screen(1)
    # template_test(screen_user_password)
    # goto_next_screen(2)
    # template_test(screen_timezone)
    # goto_next_screen(1)
    # template_test(screen_partition_right)
    # goto_next_screen(1)
    # template_test(screen_partition_device)
    # goto_next_screen(1)
    show_report()

