from views.ui import print_menu

'''module reliable for communication between student and assignment submission model'''

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

def which_assignment_to_submit():
    '''asks for an id of assignment and returns it as string'''
    
    id_ = input('Enter an id of Assignment you\'d like to submit: ')
    return id_
