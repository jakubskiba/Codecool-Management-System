from datetime import datetime
from models.school_model import School
from models.user_model import User
from models.manager_model import Manager
from models.administrator_model import Administrator
from models.mentor_model import Mentor
from models.student_model import Student

from models.assignment_model import Assignment
from models.assignment_submission_model import AssignmentSubmission
from models.attendance_model import Attendance
from views.school_view import *
import controllers.manager_controller
import controllers.administrator_controller
import controllers.mentor_controller
import controllers.student_controller


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

    files_dict = {'csv/manager.csv': Manager, 'csv/administrator.csv': Administrator,
                  'csv/mentor.csv': Mentor, 'csv/student.csv': Student}
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
        assignment = Assignment(line[0], deadline, int(line[2]))
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

        attendance = Attendance(date, line[1], student)
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

        assignment_submission = AssignmentSubmission(student, submission_date, line[2], assignment)
        assignment_submission.grade = int(line[4])

        student.assignment_submissions.append(assignment_submission)


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
    User.last_id = get_last_user_id(codecool)
    Assignment.last_id = get_last_assignment_id(codecool)


def log_in(codecool):
    """
    Checks is login and password belong to one same user

    Args:
        codecool (obj): School object - aggregate all users and assignments

    Returns:
        User (obj)
    """

    login = get_login()
    password = get_password()

    users = codecool.managers_list + codecool.administrators_list + codecool.mentors_list + codecool.students_list
    for user in users:
        if user.login == login and user.password == password:
            return user


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


def start_controller():
    """
    Signs in user, then calls appropriate controller

    Returns:
        None
    """
    intro()
    codecool = School()
    load_files(codecool)

    user = log_in(codecool)
    if type(user) is Manager:
        controllers.manager_controller.start_controller(codecool, user)
    elif type(user) is Administrator:
        controllers.administrator_controller.start_controller(codecool, user)
    elif type(user) is Mentor:
        controllers.mentor_controller.start_controller(codecool, user)
    elif type(user) is Student:
        controllers.student_controller.start_controller(codecool, user)
    else:
        print('There is no such user in system!')

    save_files(codecool)
    print_exit_message()
