import os
from os.path import abspath, join, split
import subprocess
import sys
import time

from behave.__main__ import main as behave_main

PROJECT = 'filedepot'


def run(project):
    print('Starting django testserver')
    django_process = subprocess.Popen(
        ['python',
         '{0}/manage.py'.format(project),
         'testserver',
         '--noinput'],
        stdout=open('/dev/null', 'w'),
        stderr=open('/dev/null', 'w'))
    time.sleep(2)

    print('Starting Xvfb')
    xvfb_process = subprocess.Popen(
        ['Xvfb', ':99', '-ac', '-screen', '0', '1024x768x8'])
    os.environ["DISPLAY"] = ":99"

    try:
        behave_main()  # This calls sys.exit() under all circumstances
    finally:
        print('Stopping django testserver')
        django_process.terminate()
        print('Stopping Xvfb')
        xvfb_process.terminate()


if __name__ == '__main__':
    project_dir = split(abspath(__file__))[0]
    sys.path.insert(0, join(project_dir, PROJECT))
    run(PROJECT)
