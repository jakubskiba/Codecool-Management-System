from views import ui


def print_mail_menu():
    title = 'Mail menu'
    options = ['Inbox', 'Outbox', 'Write new message']
    ui.print_menu(title, options, 'Return to user menu')


def get_choice():
    possible_choices = ['0', '1', '2']
    choice = ''
    while choice not in possible_choices:
        choice = ui.get_inputs(['option:'], 'Choose option')[0]

    return choice


def print_mail_list(mail_list):
    headers = ['From', 'Date', 'Title']
    table = []
    for mail in mail_list:
        full_name = mail.sender.name + ' ' + mail.sender.surname
        table.append([full_name, str(mail.date), str(mail.topic)])
    ui.print_table(table, headers)
