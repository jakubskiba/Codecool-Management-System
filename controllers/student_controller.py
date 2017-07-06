from views.student_view import *
from models.assignment_submission_model import AssignmentSubmission
from datetime import datetime


def start_controller(school, student):
    """
    Switches between options

    Args:
        school (obj): school object - aggregate all users and assignments
        student (obj): Student object

    Returns:
        None
    """

    choice = ''
    while choice != '0':
        print_student_menu()
        choice = get_choice()

        if choice == '1':
            submit_assignment(school, student)
        elif choice == '2':
            list_assignments(school)
        elif choice == '3':
            get_assignment_submissions(student)


def get_assignment_submissions(student):
    """
    Prints all assignment submissions

    Args:
        school (obj): school object - aggregate all users and assignments

    Returns:
        None
    """

    print_all_submissions(student.assignment_submissions)


def list_assignments(school):
    """
    Prints all assignments

    Args:
        school (obj): school object - aggregate all users and assignments

    Returns:
        None
    """

    print_all_assignments(school.assignments_list)


def submit_assignment(school, student):
    """
    Appends assignment submission list by new create objest

    Args:
        school (obj): school object - aggregate all users and assignments
        student (obj): Student object

    Returns:
        None
    """
    assignments_ids = [str(ass.assignment_id) for ass in school.assignments_list]

    chosen_assignment_id = ''
    while chosen_assignment_id not in assignments_ids:
        print_all_assignments(school.assignments_list)
        chosen_assignment_id = get_assignment_id()
    chosen_assignment_id = int(chosen_assignment_id)

    for assignment in school.assignments_list:
        if chosen_assignment_id == assignment.assignment_id:
            chosen_assignment = assignment

    content = get_assignment_submission_content()

    submission_date = datetime.now()

    assignment_submission = AssignmentSubmission(student, submission_date, content, chosen_assignment)
    student.assignment_submissions.append(assignment_submission)
