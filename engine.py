from win32gui import GetWindowText, GetForegroundWindow
from os import getenv, mkdir, path
from time import ctime, sleep

log_path = getenv('APPDATA') + '\\APHL_AWL'
log_file = log_path + '\\AWL.log'


def AWL():
    """Get active window title"""
    a = GetWindowText(GetForegroundWindow())
    return a


def log_exist():
    """Check file exist and create path directory."""
    if path.exists(log_file):
        pass
    else:
        mkdir(log_path)
    return


def AWL_log():
    """Write log file, if change window title. """
    tAWL = ''
    while True:
        if tAWL != str(AWL()):
            tAWL = str(AWL())
            f = file(log_file, 'a')
            f.write(ctime() + ': ' + AWL() + '\n')
            f.close()
        sleep(1)
    # noinspection PyUnreachableCode
    return


def AWL_exit():
    print 'Exit to',
    for i in range(1, 6):
        print 6 - i,
        sleep(1)
    return
