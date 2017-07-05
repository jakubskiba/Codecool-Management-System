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


def start_controller():
    intro()
    codecool = School()
    load_users(codecool)
    load_assignments(codecool)
