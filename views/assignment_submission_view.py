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


def print_submission(sub):
    '''prints Assignment submission'''
    print('Assignment id: {}/{}'.format(sub.assignment.assignment_id, sub.assignment.deadline))
    print('{}: {} / {}'.format(sub.student.name, sub.content, sub.date_of_submission))
    print(is_on_time(sub).rjust(30))
    print('Grade: {}'.format(grades(sub)).rjust(30))