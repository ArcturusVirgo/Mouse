import inspect
import logging
import os
import subprocess
import time


def get_code(name):
    text = subprocess.getoutput('tasklist')
    text_list = text.split('\n')

    for line in text_list:
        if line.split() and f'{name}.exe' == line.split()[0]:
            code = line.split()[-3]
            return code
    return -1

import os
os.system()
while True:
    print(get_code('Notepad'))
    time.sleep(1)
