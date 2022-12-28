import os
import sys
import errno
import io
import atexit
import argparse
from pathlib import Path
from art import text2art
from signal import signal, SIGINT, SIGTERM
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium_chromedriver_patch.patcher import *


sys.tracebacklimit = 0

parser = argparse.ArgumentParser(description='Chrome Selenium Webdriver Undetected Patcher')
parser.add_argument('driverpath', help='Path to selenium chrome webdriver')
parser.add_argument('-s', action='store_true', help='Silent mode')
args = parser.parse_args()

is_silent = args.s

if is_silent:
    def handler(stdout):
        saved_stdout = stdout
        sys.stdout = io.StringIO()

        def inner():
            sys.stdout = saved_stdout

        return inner

    receiver = handler(sys.stdout)
    signal(SIGINT, receiver)
    signal(SIGTERM, receiver)
    atexit.register(receiver)

print(text2art('selenium_chromedriver_patch'))

path = Path(args.driverpath).resolve()

try:
    if not path.exists() or not path.is_file():
        raise FileNotFoundError
    options = Options()
    options.headless = True
    Chrome(service=Service(executable_path=str(path)), options=options)
    if is_binary_patched(path):
        raise PermissionError
    if not patch(path):
        raise EOFError
except AttributeError as e:
    raise IOError(errno.EINVAL, 'File is not Chrome Webdriver executable', str(path)) from None
except PermissionError as e:
    raise IOError(errno.EPERM, 'Executable already patched', str(path)) from None
except FileNotFoundError as e:
    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT), str(path)) from None
except EOFError as e:
    raise IOError(errno.ENOEXEC, 'Executable has no proper MARKER to patch', str(path)) from None
else:
    print(f'Executable: {path} Patched!.')
