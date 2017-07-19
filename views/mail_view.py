from views import ui
from math import ceil


def print_mail_menu():
    title = 'Mail menu'
    options = ['Inbox', 'Outbox', 'Write new message']
    ui.print_menu(title, options, 'Return to user menu')


def get_choice():
    possible_choices = ['0', '1', '2', '3']
    choice = ''
    while choice not in possible_choices:
        choice = ui.get_inputs(['option:'], 'Choose option')[0]

    return choice


def print_mail_list(mail_list):
    headers = ['idx', 'From', 'To', 'Date', 'Title']
    table = []
    for i in range(len(mail_list)):
        mail = mail_list[i]
        sender_full_name = mail.sender.name + ' ' + mail.sender.surname
        receiver_full_name = mail.receiver.name + ' ' + mail.receiver.surname
        table.append([i, sender_full_name, receiver_full_name, str(mail.date), str(mail.topic)])

    ui.print_table(table, headers)


def get_mail_idx(mail_list):
    idx = ui.get_inputs(['idx'], 'Provide idx')
    return idx[0]


def print_mail_verbosely(mail):
    SCREEN_WIDTH = 82

    headers = ['From', 'To', 'Date']
    headers = ['{:<24}'.format(header) for header in headers]
    sender_full_name = mail.sender.name + ' ' + mail.sender.surname
    receiver_full_name = mail.receiver.name + ' ' + mail.receiver.surname

    table = []
    table.append([sender_full_name, receiver_full_name, str(mail.date)])
    ui.print_table(table, headers)

    message = []
    lines_number = ceil(len(mail.message) / SCREEN_WIDTH)
    for i in range(lines_number):
        line_begin = i * SCREEN_WIDTH
        line_end = (i + 1) * SCREEN_WIDTH

        line = mail.message[line_begin:line_end]

        message.append([line])

    headers = ['Title: ' + mail.topic]
    table = []
    table.append(message)
    ui.print_table(message, headers)


def get_receiver():

    return ui.get_inputs(['id'], 'Provide id')[0]


def print_no_receiver_error():

    ui.print_error_message('No such user')


def get_mail_data():
    return ui.get_inputs(['Title:', 'Message:'], 'Provide title and message of mail')