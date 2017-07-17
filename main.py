from controllers import school_controller
import sys
import os
import traceback
import datetime


def main():
    school_controller.start_controller()


if __name__ == '__main__':
    try:
        main()

    except BaseException:
        exc_type, exc_value, exc_traceback = sys.exc_info()

        filename = str(datetime.datetime.now())
        filename = filename.split('.')[0]
        file_path = 'log/' + filename + '.log'

        log_file = open(file_path, 'w')

        log_file.write('Traceback (most recent call last):\n')
        traceback.print_tb(exc_traceback, file=log_file)
        log_file.write(str(exc_type.__name__) + ': ')
        log_file.write(str(exc_value))
