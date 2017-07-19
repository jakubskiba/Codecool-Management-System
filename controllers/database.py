from datetime import datetime
from models import user_model
from models import manager_model
from models import administrator_model
from models import mentor_model
from models import student_model
from models import assignment_model
from models import assignment_submission_model
from models import attendance_model
from models import mail_model


def make_data_backup():
    """
    Make backup of all csv files

    Returns:
        None
    """

    csv_files = ['administrator', 'assignment', 'assignment_submission', 'attendance', 'manager', 'mentor', 'student']
    current_date = datetime.today()
    prefix = str(current_date).split(' ')[0]

    for csv_file in csv_files:
        with open('csv/' + csv_file + '.csv') as datafile:
            content = datafile.read()
        with open('csv/backup/' + csv_file + '-' + prefix + '.csv', 'w') as datafile:
            datafile.write(content)


def get_user_by_id(codecool, id_):
    """
    Searches user by id

    Args:
        codecool (obj): School object - aggregate all users and assignments
        id_ (int)

    Returns:
        User (obj)
    """

    users = codecool.managers_list + codecool.administrators_list + codecool.mentors_list + codecool.students_list
    for user in users:
        if user.id_ == id_:
            return user


def get_assignment_by_id(codecool, id_):
    """
    Searches assignment by id

    Args:
        codecool (obj): School object - aggregate all users and assignments
        id_ (int)

    Returns:
        Assignment (obj)
    """

    for assignment in codecool.assignments_list:
        if assignment.assignment_id == id_:
            return assignment


def load_users(codecool):
    """
    Reads data from csv file to user classes

    Args:
        codecool (obj): School object - aggregate all users and assignments

    Returns:
        None
    """

    files_dict = {'csv/manager.csv': manager_model.Manager, 'csv/administrator.csv': administrator_model.Administrator,
                  'csv/mentor.csv': mentor_model.Mentor, 'csv/student.csv': student_model.Student}
    for filename in files_dict:
        with open(filename) as datafile:
            content = datafile.readlines()

        content = [line.strip() for line in content]
        content = [line.split('|') for line in content]

        for line in content:
            user = files_dict[filename](line[0], line[1], line[2], line[3], line[4], line[5], int(line[6]))

            if filename == 'csv/manager.csv':
                codecool.managers_list.append(user)
            elif filename == 'csv/administrator.csv':
                codecool.administrators_list.append(user)
            elif filename == 'csv/mentor.csv':
                codecool.mentors_list.append(user)
            elif filename == 'csv/student.csv':
                codecool.students_list.append(user)


def load_assignments(codecool):
    """
    Reads data from csv file to assignment classes

    Args:
        codecool (obj): School object - aggregate all users and assignments

    Returns:
        None
    """

    with open('csv/assignment.csv') as datafile:
        content = datafile.readlines()

    content = [line.strip() for line in content]
    content = [line.split('|') for line in content]
    content = [[line[0], line[1].split('-'), line[2]] for line in content]

    for line in content:
        deadline = datetime(int(line[1][0]), int(line[1][1]), int(line[1][2]))
        assignment = assignment_model.Assignment(line[0], deadline, int(line[2]))
        codecool.assignments_list.append(assignment)


def load_attendance(codecool):
    """
    Reads data from csv file to attendance classes

    Args:
        codecool (obj): School object - aggregate all users and assignments

    Returns:
        None
    """

    with open('csv/attendance.csv') as datafile:
        content = datafile.readlines()

    content = [line.strip() for line in content]
    content = [line.split('|') for line in content]
    content = [[line[0].split('-'), float(line[1]), int(line[2])] for line in content]

    for line in content:
        date = datetime(int(line[0][0]), int(line[0][1]), int(line[0][2]))
        student = get_user_by_id(codecool, line[2])

        attendance = attendance_model.Attendance(date, line[1], student)
        student.attendance_list.append(attendance)


def load_assignment_submission(codecool):
    """
    Reads data from csv file to assignment submission classes

    Args:
        codecool (obj): School object - aggregate all users and assignments

    Returns:
        None
    """

    with open('csv/assignment_submission.csv') as datafile:
        content = datafile.readlines()

    content = [line.strip() for line in content]
    content = [line.split('|') for line in content]

    for line in content:
        student = get_user_by_id(codecool, int(line[0]))

        submission_date = line[1].split('-')
        submission_date = datetime(int(submission_date[0]), int(submission_date[1]), int(submission_date[2]))

        assignment = get_assignment_by_id(codecool, int(line[3]))

        assignment_submission = assignment_submission_model.AssignmentSubmission(student, submission_date, line[2],
                                                                                 assignment)
        assignment_submission.grade = int(line[4])

        student.assignment_submissions.append(assignment_submission)


def load_mails(codecool):
    """

    """

    with open('csv/mails.csv') as datafile:
        content = datafile.readlines()

    content = [line.strip() for line in content]
    content = [line.split('|') for line in content]
    content = [[line[0].split('-'), int(line[1]), int(line[2]), line[3], line[4]] for line in content]

    for line in content:
        mail_date = line[0]
        mail_date = datetime(int(mail_date[0]), int(mail_date[1]), int(mail_date[2]))

        sender = get_user_by_id(codecool, line[1])
        receiver = get_user_by_id(codecool, line[2])

        topic = line[3]
        message = line[4]

        mail = mail_model.Mail(mail_date, sender, receiver, topic, message)
        codecool.mails.append(mail)


def get_last_user_id(codecool):
    """
    Searches for user with highest id

    Args:
        codecool (obj): School object - aggregate all users and assignments

    Returns:
        id_ (int)
    """

    last_id = 0
    users = codecool.managers_list + codecool.administrators_list + codecool.mentors_list + codecool.students_list
    for user in users:
        if user.id_ > last_id:
            last_id = user.id_

    return last_id


def get_last_assignment_id(codecool):
    """
    Searches for assignment with highest id

    Args:
        codecool (obj): School object - aggregate all users and assignments

    Return:
        id_ (int)
    """

    last_id = 0
    for assignment in codecool.assignments_list:
        if assignment.assignment_id > last_id:
            last_id = assignment.assignment_id

    return last_id


def load_files(codecool):
    """
    Fill school object lists with data from csv

    Args:
        codecool (obj): School object - aggregate all users and assignments

    Returns:
        None
    """
    load_users(codecool)
    load_assignments(codecool)
    load_attendance(codecool)
    load_assignment_submission(codecool)
    load_mails(codecool)
    user_model.User.last_id = get_last_user_id(codecool)
    assignment_model.Assignment.last_id = get_last_assignment_id(codecool)
    make_data_backup()


def save_users(codecool):
    """
    Saves data from each user object to csv file

    Args:
        codecool (obj): School object - aggregate all users and assignments

    Returns:
        None
    """

    files_dict = {'csv/manager.csv': codecool.managers_list, 'csv/administrator.csv': codecool.administrators_list,
                  'csv/mentor.csv': codecool.mentors_list, 'csv/student.csv': codecool.students_list}

    for filename in files_dict:
        data_to_save = []
        for user in files_dict[filename]:
            data_to_save.append([user.name, user.surname, user.login,
                                user.password, user.email, user.phone, str(user.id_)])

        data_to_save = ['|'.join(line) for line in data_to_save]
        data_to_save = '\n'.join(data_to_save)
        with open(filename, 'w') as datafile:
            datafile.write(data_to_save)


def save_assignments(codecool):
    """
    Saves data from each assignment object in assignments_list to csv file

    Args:
        codecool (obj): School object - aggregate all users and assignments

    Returns:
        None
    """

    data_to_save = []
    for assignment in codecool.assignments_list:
        deadline = [str(assignment.deadline.year), str(assignment.deadline.month), str(assignment.deadline.day)]
        deadline = '-'.join(deadline)
        data_to_save.append([assignment.content, deadline, str(assignment.assignment_id)])

    data_to_save = ['|'.join(line) for line in data_to_save]
    data_to_save = '\n'.join(data_to_save)

    with open('csv/assignment.csv', 'w') as datafile:
        datafile.write(data_to_save)


def save_attendance(codecool):
    """
    Saves data from each attendance object in each student object to csv file

    Args:
        codecool (obj): School object - aggregate all users and assignments

    Returns:
        None
    """

    data_to_save = []
    for student in codecool.students_list:
        for attendance in student.attendance_list:
            date = [str(attendance.date.year), str(attendance.date.month), str(attendance.date.day)]
            date = '-'.join(date)
            data_to_save.append([date, str(attendance.attendance_state), str(student.id_)])

    data_to_save = ['|'.join(line) for line in data_to_save]
    data_to_save = '\n'.join(data_to_save)

    with open('csv/attendance.csv', 'w') as datafile:
        datafile.write(data_to_save)


def save_assignment_submission(codecool):
    """
    Saves data from each object in assignment stubmissions list to csv file

    Args:
        codecool (obj): School object - aggregate all users and assignments

    Returns:
        None
    """

    data_to_save = []
    for student in codecool.students_list:
        for submission in student.assignment_submissions:
            date = [str(submission.date_of_submission.year),
                    str(submission.date_of_submission.month), str(submission.date_of_submission.day)]
            date = '-'.join(date)
            data_to_save.append([str(student.id_), date, submission.content,
                                str(submission.assignment.assignment_id), str(submission.grade)])

    data_to_save = ['|'.join(line) for line in data_to_save]
    data_to_save = '\n'.join(data_to_save)

    with open('csv/assignment_submission.csv', 'w') as datafile:
        datafile.write(data_to_save)


def save_files(codecool):
    """
    Saves data to files

    Args:
        codecool (obj): School object - aggregate all users and assignments

    Returns:
        None
    """

    save_users(codecool)
    save_assignments(codecool)
    save_attendance(codecool)
    save_assignment_submission(codecool)
