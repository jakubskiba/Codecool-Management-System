from ui import print_menu

    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        This function doesn't return anything it only prints to console.
    """


def get_input():
    which_data = input()
    return which_data


def display_update_choice(user):

    attributes_list = [attr for attr in dir(user) if not attr.startswith('__')]
    print_menu('Which data to update? enter number', attributes_list, 'exit')