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
    users = codecool.managers_list + codecool.administrators_list + codecool.mentors_list + codecool.students_list
    for user in users:
        if user.id_ == id_:
            return user


def get_assignment_by_id(codecool, id_):
    for assignment in codecool.assignments_list:
        if assignment.assignment_id == id_:
            return assignment


def load_users(codecool):
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


def load_files(codecool):
    load_users(codecool)
    load_assignments(codecool)
    load_attendance(codecool)
    load_assignment_submission(codecool)


def log_in(codecool):
    login = get_login()
    password = get_password()

    users = codecool.managers_list + codecool.administrators_list + codecool.mentors_list + codecool.students_list
    for user in users:
        if user.login == login and user.password == password:
            return user


def start_controller():
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

    print_exit_message()
