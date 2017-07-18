import os

from views import user_view
from views import student_view
from models import assignment_submission_model
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
        os.system('clear')
        views.user_view.display_user_info(student)
        student_view.print_student_menu()
        choice = student_view.get_choice()

        if choice == '1':
            submit_assignment(school, student)
        elif choice == '2':
            list_assignments(school)
        elif choice == '3':
            get_assignment_submissions(student)

        input('Press enter')


def get_assignment_submissions(student):
    """
    Prints all assignment submissions

    Args:
        school (obj): school object - aggregate all users and assignments

    Returns:
        None
    """

    student_view.print_all_submissions(student.assignment_submissions)


def list_assignments(school):
    """
    Prints all assignments

    Args:
        school (obj): school object - aggregate all users and assignments

    Returns:
        None
    """

    student_view.print_all_assignments(school.assignments_list)


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

    student_view.print_all_assignments(school.assignments_list)
    chosen_assignment_id = student_view.get_assignment_id()

    if chosen_assignment_id in assignments_ids:

        chosen_assignment_id = int(chosen_assignment_id)

        for assignment in school.assignments_list:
            if chosen_assignment_id == assignment.assignment_id:
                chosen_assignment = assignment

        content = student_view.get_assignment_submission_content()

        submission_date = datetime.now()

        assignment_submission = assignment_submission_model.AssignmentSubmission(student, submission_date, content, chosen_assignment)
        student.assignment_submissions.append(assignment_submission)

    else:
        views.ui.print_error_message('No such assignment')