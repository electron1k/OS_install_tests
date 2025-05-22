import pyautogui
import pywinctl
from datetime import datetime
import subprocess
from jinja2 import Environment, FileSystemLoader, Template, select_autoescape

env = Environment(
    loader=FileSystemLoader('results/reports/'),
    autoescape=select_autoescape(['html'])
)

report_dicts= []

reps = str.maketrans({":": "-", " ": "-"})
stamp = str(datetime.now()).translate(reps).split('.')[0]

def move_cursor():
    window = pywinctl.getActiveWindow()
    pyautogui.moveTo(x=int(window.left)+50, y=int(window.top)+50)
    pyautogui.click()
    print('cursor_pos ', pyautogui.position())
    # window.maximize()
    print(window)

def create_report_file():
    with open('results/reports/report.html', 'a') as file:
        file.write('''<html>
  <head>
    <title></title>
    <meta content="">
    <style></style>
  </head>
  <body>
    <h2>Installation testing results</h2>
        <table border="1">
            <thead>
                <tr>
                    <th>Название теста</th><th>Результат теста</th><th>Стандартные элементы</th><th>Скриншот</th>
                </tr>
            </thead>
            <tbody>''')
        


def write_to_report(data: list, tname: str):
    print(f'DATA TO REPORT {data}')
    temp = {'name': tname,
    'status': data[1],
    'default': data[2],
    'screen': f'../img/{tname}.png'}
    report_dicts.append(temp)
    print(temp)
    print(f'Global report dicts {report_dicts}')
    with open('results/reports/report.html', 'a') as file:
        file.write(f'<tr><td>{tname}</td><td>{data[1]}</td><td>{data[2]}</td><td><img src="../img/{tname}.png" width="400" height="325"></td></tr>\n')
        # file.write(f'{str(data)}')


def report_finaliztion():
    with open('results/reports/report.html', 'a') as file:
        file.write(f'''
            </tbody>
        </table>
    </body>
</html>''')
        ren = subprocess.call(['mv', 'results/reports/report.html', f'results/reports/report_{stamp}.html'])
    

def show_report():
    env = Environment(
        loader=FileSystemLoader('results/reports/templates'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('j_report.html')

    fin_report = template.render(report_dicts=report_dicts)
    # print(fin_report)
    with open(f'results/reports/j_report_{stamp}.html', 'a') as file:
        file.write(str(fin_report))
