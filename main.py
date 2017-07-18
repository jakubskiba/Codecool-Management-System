from controllers import school_controller
import utilities

def main():
    school_controller.start_controller()


if __name__ == '__main__':
    try:
        main()

    except BaseException:
        utilities.handle_exception()
