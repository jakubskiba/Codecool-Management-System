from models import attendance_model


def print_attendance_oneline(attendance):
    print(attendance.date, attendance.attendance_state, attendance.student)


def print_attendance_table(attendance):
    form = '|{:<10}|{:<10}|\n'

    date = ''
    date += form.format('day', attendance.date.day)
    date += form.format('month', attendance.date.month)
    date += form.format('year', attendance.date.year)

    student = form.format('student', attendance.student.name)

    if attendance.attendance_state == 0:
        state = 'absent'
    elif attendance.attendance_state == 0.5:
        state = 'late'
    elif attendance.attendance_state == 1:
        state = 'present'
    state = form.format('state', state)

    table = date + student + state

    print(table)
