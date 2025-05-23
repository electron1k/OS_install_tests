tests = [
    {
    'test_name': 'Стартовый_экран',
    'elem_wait': 'reference_img/1_start_menu.png',
    'elems_needed': ['reference_img/elems/installer_logo.png', 
                     'reference_img/elems/btn_screen.png',
                     'reference_img/elems/btn_continue.png',
                     ],
    'warn':'reference_img/elems/warning.png',
    'field_location_ref': [],
    'fill_field': ''
    },

    {
    'test_name': 'Лицензия',
    'elem_wait': 'reference_img/2_3_sc_licence.png',
    'elems_needed': ['reference_img/elems/installer_logo.png', 
                     'reference_img/elems/btn_screen.png',
                     'reference_img/elems/btn_continue.png',
                     ],
    'warn':'reference_img/elems/warning.png',
    'field_location_ref': [],
    'fill_field': ''
    },

    {
    'test_name': 'Настройка_сети-Имя_компьютера',
    'elem_wait': 'reference_img/computer_name.png',
    'elems_needed': ['reference_img/elems/installer_logo.png', 
                     'reference_img/elems/btn_screen.png',
                     'reference_img/elems/btn_continue.png',
                     ],
    'warn':'reference_img/elems/warning.png',
    'field_location_ref': ['reference_img/computer_name.png'],
    'fill_field': '-AUTOTEST'
    },


    {
    'test_name': 'Настройка_сети-Имя_домена',
    'elem_wait': 'reference_img/domain_name.png',
    'elems_needed': ['reference_img/elems/installer_logo.png', 
                     'reference_img/elems/btn_screen.png',
                     'reference_img/elems/btn_continue.png',
                     ],
    'warn':'reference_img/elems/warning.png',
    'field_location_ref': [],
    'fill_field': ''
    },

    {
    'test_name': 'Настройка_учетных_записей-Полное_имя',
    'elem_wait': 'reference_img/user_name.png',
    'elems_needed': ['reference_img/elems/installer_logo.png', 
                     'reference_img/elems/btn_screen.png',
                     'reference_img/elems/btn_continue.png',
                     ],
    'warn':'reference_img/elems/warning.png',
    'field_location_ref': ['reference_img/user_name.png'],
    'fill_field': 'tester'
    },

    {
    'test_name': 'Настройка_учетных_записей-Имя_учетной_записи',
    'elem_wait': 'reference_img/acc_name.png',
    'elems_needed': ['reference_img/elems/installer_logo.png', 
                     'reference_img/elems/btn_screen.png',
                     'reference_img/elems/btn_continue.png',
                     ],
    'warn':'reference_img/elems/warning.png',
    'field_location_ref': ['reference_img/user_name.png'],
    'fill_field': ''
    },


    {
    'test_name': 'Настройка_учетных_записей-Пароль',
    'elem_wait': 'reference_img/new_user_pass.png',
    'elems_needed': ['reference_img/elems/installer_logo.png', 
                     'reference_img/elems/btn_screen.png',
                     'reference_img/elems/btn_continue.png',
                     ],
    'warn':'reference_img/elems/warning.png',
    'field_location_ref': ['reference_img/new_user_pass.png', 'reference_img/confirm_user_pass.png'],
    'fill_field': 'q1w2e3r4'
    },


    {
    'test_name': 'Настройка_времени',
    'elem_wait': 'reference_img/timezone.png',
    'elems_needed': ['reference_img/elems/installer_logo.png', 
                     'reference_img/elems/btn_screen.png',
                     'reference_img/elems/btn_continue.png',
                     ],
    'warn':'reference_img/elems/warning.png',
    'field_location_ref': [],
    'fill_field': ''
    },

    {
    'test_name': 'Метод_разметки_дисков',
    'elem_wait': 'reference_img/method_part.png',
    'elems_needed': ['reference_img/elems/installer_logo.png', 
                     'reference_img/elems/btn_screen.png',
                     'reference_img/elems/btn_continue.png',
                     ],
    'warn':'reference_img/elems/warning.png',
    'field_location_ref': [],
    'fill_field': ''
    },

    {
    'test_name': 'Выбор_диска',
    'elem_wait': 'reference_img/hdd_device2.png',
    'elems_needed': ['reference_img/elems/installer_logo.png', 
                     'reference_img/elems/btn_screen.png',
                     'reference_img/elems/btn_continue.png',
                     ],
    'warn':'reference_img/elems/warning.png',
    'field_location_ref': [],
    'fill_field': ''
    }

]