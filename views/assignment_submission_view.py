from views import ui


def grades(sub):
    '''prepares string to be printed as grade'''
    if not sub.grade:
        grade_to_print = 'ungraded yet'
    else:
        grade_to_print = str(sub.grade)

    return grade_to_print


def is_on_time(sub):
    '''prepares string informs about delay or beeing on time'''
    if sub.assignment.deadline >= sub.date_of_submission:
        return 'on time'
    else:
        return 'delayed'


def print_submission(id_, sub):
    '''prints Assignment submission'''

    print('Submission id:', id_)
    print('Assignment id: {}/{}'.format(sub.assignment.assignment_id, sub.assignment.deadline))
    print('{}: {} / {}'.format(sub.student.name, sub.content, sub.date_of_submission))
    print(is_on_time(sub).rjust(30))
    print('Grade: {}'.format(grades(sub)).rjust(30))


def get_number():
    ''' number is string'''
    num = input()
    return num


def print_what_to_do():
    ui.print_menu('Would you like to submit assignment?', ['Show submission'], 'exit')
