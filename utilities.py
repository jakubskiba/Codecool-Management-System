import sys
import os
import traceback
import datetime

def handle_exception():
    """
    Writes error to log
    """

    exc_type, exc_value, exc_traceback = sys.exc_info()

    filename = str(datetime.datetime.now())
    filename = filename.split('.')[0]
    file_path = 'log/' + filename + '.log'

    log_file = open(file_path, 'w')

    log_file.write('Traceback (most recent call last):\n')
    traceback.print_tb(exc_traceback, file=log_file)
    log_file.write(str(exc_type.__name__) + ': ')
    log_file.write(str(exc_value))

    os.system('clear')
    print('Program fails and must be shut down.\nError log written to ' + file_path)
