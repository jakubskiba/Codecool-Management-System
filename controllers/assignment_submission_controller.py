from models import assignment_submission_model
from views import assignment_submission_view


def start_controller(assignment_submission):
    """
    Switches between options

    Args:
        assignment_submission (obj)

    Returns:
        None
    """

    print_what_to_do()
    num = get_number()
    if num == '1':
        assignment_submission_view.print_submission(assignment_submission)
