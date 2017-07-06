from models.student_model import Student
from models.school_model import School
from views.student_view import print_student_menu, get_choice, print_all_submissions, get_submission_number
# from views.assignment_submission_view import print_submission


def start_controller(student, school):
    choice = ''
    while choice != '0':
        print_student_menu()
        choice = get_choice()

        if choice == '1':
            submit_assignment()
        elif choice == '2':
            get_assignment_submissions(student)


def get_assignment_submissions(student):
    choice = ''
    print_all_submissions(student.assignment_submissions) 
    while choice != '0':
        print_all_submissions(student.assignment_submissions)
        submission_number = get_submission_number(student.assignment_submissions)


def submit_assignment():
    pass
