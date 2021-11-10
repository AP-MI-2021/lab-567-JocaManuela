from UI.console import run_console
from UI.command_line_console import run_command_line_console
from Tests.run_all_tests import run_all_tests


def print_optiuni():
   print('1. Utilizati interfata cu optiuni')
   print('2. Utilizati interfata cu comenzi pe aceeasi linie')
   print('x. Iesire.')

def main():
    run_all_tests()
    list_of_cheltuieli = []
    print_optiuni()
    op = input('Alegeti interfata dorita:')
    while True:
        if op == '1':
            run_console(list_of_cheltuieli)
        elif op == '2':
            run_command_line_console(list_of_cheltuieli)
        elif op == 'x':
            break
        else:
            print('Opțiune invalidă')


main()