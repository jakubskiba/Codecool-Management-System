from views import mail_view
from views import user_view
import os


def start_controller(codecool, user):
    choice = ''
    while choice != '0':
        os.system('clear')
        user_view.display_user_info(user)
        mail_view.print_mail_menu()
        choice = mail_view.get_choice()

        if choice == '1':
            inbox = get_inbox(codecool, user)
            mail_view.print_mail_list(inbox)

        elif choice == '2':
            pass

        if choice != '0':
            input('Press enter')


def get_inbox(codecool, user):
    inbox = []
    for mail in codecool.mails:
        if mail.receiver == user:
            inbox.append(mail)

    return inbox
