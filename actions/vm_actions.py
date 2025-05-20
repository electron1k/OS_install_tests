import subprocess

def check_machine(machine_name):
    proc = subprocess.check_output(['VBoxManage', 'list', 'vms'], text=True)
    # print(proc)
    if machine_name in proc:
        return True
    else:
        return False
    
def test_create_and_run_vm():
    proc = subprocess.call('./create_vm.sh',  shell=True)
    print("machine created")
    # start_vm = subprocess.call(['VBoxManage', 'startvm', 'OSnova'])


def start_vm(machine):
     start_vm = subprocess.call(['VBoxManage', 'startvm', f'{machine}'])