import views.ui


def print_students_list(codecool):
    title_list = ['id', 'Name', 'Surname', 'Phone', 'Email']

    table = []
    for student in codecool.students_list:
        table.append([student.id_, student.name, student.surname, student.phone, student.email])

    views.ui.print_table(table, title_list)


def print_administrator_menu():
    title = 'Administrator Menu'
    options = ['List students']
    views.ui.print_menu(title, options, 'Exit')


def get_choice():
    possible_choices = ['0', '1']
    choice = ''
    while choice not in possible_choices:
        choice = views.ui.get_inputs(['option:'], 'Choose option')[0]

    return choice
