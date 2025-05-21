if used python 3.7 need to modify pymoctl
remove underscore (_) in string 770

move_cursor is need to get right screens 


venv/lib64/python3.7/site-packages/pyscreeze/__init__.py

600    # if PILLOW_VERSION >= (9, 2, 0) and GNOMESCREENSHOT_EXISTS:
601    if PILLOW_VERSION >= (9, 2, 0):

venv/lib64/python3.7/site-packages/PIL/ImageGrab.py

67 # subprocess.call(["gnome-screenshot", "-f", filepath])
68 subprocess.call(["spectacle", "-b", "-o", filepath])

отключить всплывающие уведомления spectacle в KDE

