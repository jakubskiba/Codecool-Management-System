import views.ui


def print_mentor_details(mentor):
    """
    Function prints mentor details

    Args:
        mentor (Mentor): object represents single mentor

    Returns:
        None
    """

    ornament = 30 * '='
    print(ornament)
    print('Mentor id:', mentor.id)
    print('Full name:', mentor.name, mentor.surname)
    print('E-mail:', mentor.e_mail)
    print('Phone:', mentor.phone)
    print(ornament)


def print_students_list(codecool):
    title_list = ['id', 'Name', 'Surname']

    table = []
    for student in codecool.students_list:
        table.append([student.id_, student.name, student.surname])

    views.ui.print_table(table, title_list)


def print_mentor_menu():
    title = 'Mentor Menu'
    options = ['List students', 'Add assignments', 'Grade assignment', 'Check attendance', 'Edit student']

    views.ui.print_menu(title, options, 'Exit')


def get_choice():
    possible_choices = ['0', '1', '2', '3', '4', '5']
    choice = ''
    while choice not in possible_choices:
        choice = views.ui.get_inputs(['option:'], 'Choose option')[0]

    return choice
