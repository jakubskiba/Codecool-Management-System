def print_assignment_details(assignment):
    """
    Function prints assignment details

    Args:
        assignment (Assignment): object represents single assignment added by mentor

    Returns:
        None
    """

    ornament = 30 * '='
    print(ornament)
    print('Assignment id:', assignment.assignment_id)
    print('Deadline:', assignment.deadline)
    print('Assignment:', assignment.content)
    print(ornament)
