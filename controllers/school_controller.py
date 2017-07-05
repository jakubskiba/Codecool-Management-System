from models.school_model import School
from models.user_model import User
from models.manager_model import Manager
from models.administrator_model import Administrator
from models.mentor_model import Mentor
from models.student_model import Student

from models.assignment_model import Assignment
from models.assignment_submission import AssignmentSubmission
from models.attendance_model import Attendance
from views.school_view import *


def loading_users(codecool):
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
                codecool.manager_list.append(user)
            elif filename == 'csv/administrator.csv':
                codecool.administrator_list.append(user)
            elif filename == 'csv/mentor.csv':
                codecool.mentor_list.append(user)
            elif filename == 'csv/student.csv':
                codecool.student_list.append(user)


def loading_assignments(codecool):
    


def start_controller():
    intro()
    codecool = School()
    loading_users(codecool)
    loading_assignments(codecool)
