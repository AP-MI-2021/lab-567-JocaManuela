from Domain.Cheltuiala import create_cheltuiala
from Logic.CRUD import add_cheltuiala, delete_cheltuiala, update_cheltuiala
from Domain.Cheltuiala import to_string

def help():
    print('Pt.comanda de adăugare cheltuială:add, ID, nr_apartament, suma, data, tipul')
    print('Pt.comanda de ștergere cheltuială:delete, ID')
    print('Pt.comanda de modificare cheltuială:update, ID, noul nr_apartament, noua suma, noua data, noul tip')
    print('Pt.comanda de afișare listă de cheltuieli:showall')
    print('Pt.comanda de ieșire:exit (dupa exit nu se pune ";")')
    print('Introduceți comenzile separate prin ";", iar datele din aceeași comandă separate prin ",":')


def show_all(list_of_cheltuieli):
    try:
        for cheltuiala in list_of_cheltuieli:
            print(to_string(cheltuiala))
    except Exception:
        print("Eroare")


def run_command_line_console(list_of_cheltuieli):
    list_of_cheltuieli = []
    while True:
        help()
        command_line = input()
        command_line = command_line.split(';')
        for command in command_line:
            command = command.split(',')
            if command[0] == 'add':
                if len(command) == 6:
                    try:
                        ID = command[1]
                        nr_apartament = int(command[2])
                        suma = float(command[3])
                        data = command[4]
                        tipul = command[5]
                        cheltuiala = create_cheltuiala(ID, nr_apartament, suma, data, tipul)
                        list_of_cheltuieli = add_cheltuiala(list_of_cheltuieli, ID, nr_apartament, suma, data, tipul)
                    except ValueError as ve:
                        print("Eroare : {}".format(ve))
            elif command[0] == 'delete':
                if len(command) == 2:
                    ID = command[1]
                    list_of_cheltuieli = delete_cheltuiala(list_of_cheltuieli, ID)
            elif command[0] == 'update':
                if len(command) == 6:
                    try:
                        ID = command[1]
                        nr_apartament = int(command[2])
                        suma = float(command[3])
                        data = command[4]
                        tipul = command[5]
                        list_of_cheltuieli = update_cheltuiala(list_of_cheltuieli, ID, nr_apartament, suma, data, tipul)
                    except ValueError as ve:
                        print("Eroare : {}".format(ve))
            elif command[0] == 'showall':
                show_all(list_of_cheltuieli)
            elif command[0] == 'exit':
                break
            else:
                print('Opțiune invalidă!Reîncercați!')


