from Domain.Cheltuiala import to_string
from Logic.CRUD import add_cheltuiala, delete_cheltuiala, update_cheltuiala
from Logic.functionalitati import delete_all_cheltuieli_pt_apartament, max_cheltuiala_pt_tip_cheltuiala, adunare_valoare, \
                                  ord_cheltuieli_descrescator_dupa_suma, sume_lunare, do_undo, do_redo



def print_menu():
    print('1. Adăugare cheltuială')
    print('2. Ștergere cheltuială')
    print('3. Modificare cheltuială')
    print('4. Ștergerea tuturor cheltuielilor pentru un apartament dat')
    print('5. Adunarea unei valori la toate cheltuielile dintr-o dată citită')
    print('6. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială')
    print('7. Ordonarea cheltuielilor descrescător după sumă')
    print('8. Afișarea sumelor lunare pentru fiecare apartament')
    print('u. Undo')
    print('r.Redo')
    print('a. Afișarea listei de cheltuieli')
    print('x. Ieșire')

def ui_add_cheltuiala(list_of_cheltuieli, undo_list, redo_list):
    ID = input('Dați ID-ul: ')
    nr_apartament = int(input('Dați numărul apartamentului: '))
    suma = float(input('Dați suma: '))
    data = input('Dați data cheltuielii: ')
    tipul = input('Dați tipul de cheltuială: ')
    try:
        rezultat = add_cheltuiala(list_of_cheltuieli, ID, nr_apartament, suma, data, tipul, undo_list, redo_list)
        print(rezultat)
        print('Cheltuială adăugată!')
        return rezultat
    except ValueError as ve:
        print('Eroare: {}'.format(ve))
        return list_of_cheltuieli
    except:
        print('Unknown error')
    finally:
        pass


def ui_delete_cheltuiala(list_of_cheltuieli, undo_list, redo_list):
    ID = input('Dați ID-ul cheltuielii de șters: ')
    try:
        rezultat = delete_cheltuiala(list_of_cheltuieli, ID, undo_list, redo_list)
        print(rezultat)
        print('Cheltuială ștearsă!')
        return rezultat
    except ValueError as ve:
        print('Eroare: {}'.format(ve))
        return list_of_cheltuieli
    except:
        print('Unknown error')
    finally:
        pass

def ui_update_cheltuieli(list_of_cheltuieli, undo_list, redo_list):
    ID = input('Dati ID-ul cheltuielii de modificat: ')
    nr_apartament = int(input('Dați noul număr al apartamentului pentru care se efectuează cheltuiala: '))
    suma = float(input('Dați noua sumă: '))
    data = input('Dati noua data: ')
    tipul = input('Dați noul tip: ')
    try:
        rezultat = update_cheltuiala(list_of_cheltuieli, ID, nr_apartament, suma, data, tipul, undo_list, redo_list)
        print('Cheltuiala a fost actualizată!')
        print(rezultat)
        return rezultat
    except ValueError as ve:
        print('Eroare: {}'.format(ve))
        return list_of_cheltuieli
    except:
        print('Unknown error')
    finally:
        pass

def ui_delete_all_cheltuieli_pt_apartament(list_of_cheltuieli, undo_list, redo_list):
    nr_apartament = int(input('Dați numărul apartamentului pentru care se efectuează ștergerea cheltuielilor: '))
    try:
        rezultat = delete_all_cheltuieli_pt_apartament(list_of_cheltuieli, nr_apartament, undo_list, redo_list)
        print(rezultat)
        print('Cheltuielile au fost șterse!')
        return rezultat
    except ValueError as ve:
        print('Eroare: {}'.format(ve))
        return list_of_cheltuieli
    except:
        print('Unknown error')
    finally:
        pass


def ui_adunare_valoare(list_of_cheltuieli, undo_list, redo_list):
    data = input('Dați data pentru care se va face adunarea: ')
    valoare = float(input('Dați valoarea care trebuie adăugată: '))
    try:
        rezultat = adunare_valoare(list_of_cheltuieli, data, valoare, undo_list, redo_list)
        print(rezultat)
        print('Adăugare efectuată cu succes!')
        return rezultat
    except ValueError as ve:
        print('Eroare: {}'.format(ve))
        return list_of_cheltuieli
    except:
        print('Unknown error')
    finally:
        pass


def ui_max_cheltuiala_pt_tip_cheltuiala(list_of_cheltuieli):
    rezultat = max_cheltuiala_pt_tip_cheltuiala(list_of_cheltuieli)
    print(rezultat)
    return rezultat

def ui_ord_cheltuieli_descrescator_dupa_suma(list_of_cheltuieli, undo_list, redo_list):
    rezultat = ord_cheltuieli_descrescator_dupa_suma(list_of_cheltuieli, undo_list, redo_list)
    print(rezultat)
    return rezultat

def ui_sume_lunare(list_of_cheltuieli):
    rezultat = sume_lunare(list_of_cheltuieli)
    print(rezultat)
    return rezultat

def ui_undo(list_of_cheltuieli, undo_list, redo_list):
    undo_result = do_undo(undo_list, redo_list, list_of_cheltuieli)
    if undo_result is not None:
        print('Undo efectuat cu succes!')
        return undo_result
    print('Nu se poate face undo!')
    return list_of_cheltuieli


def ui_redo(list_of_cheltuieli, undo_list, redo_list):
    redo_result = do_redo(undo_list, redo_list, list_of_cheltuieli)
    if redo_result is not None:
        print('Redo efectuat cu succes!')
        return redo_result
    print('Nu se poate face redo!')
    return list_of_cheltuieli

def ui_show_all(list_of_cheltuieli):
    try:
        for cheltuiala in list_of_cheltuieli:
            print(to_string(cheltuiala))
    except Exception:
        print("Eroare")



def run_console(list_of_cheltuieli, undo_list, redo_list):
    lista = []
    while True:
        print_menu()
        op = input('Opțiune: ')
        if op == '1':
            list_of_cheltuieli = ui_add_cheltuiala(list_of_cheltuieli, undo_list, redo_list)
            lista.append(list_of_cheltuieli)
        elif op == '2':
            list_of_cheltuieli = ui_delete_cheltuiala(list_of_cheltuieli, undo_list, redo_list)
            lista.append(list_of_cheltuieli)
        elif op == '3':
            list_of_cheltuieli = ui_update_cheltuieli(list_of_cheltuieli, undo_list, redo_list)
            lista.append(list_of_cheltuieli)
        elif op == '4':
            list_of_cheltuieli = ui_delete_all_cheltuieli_pt_apartament(list_of_cheltuieli, undo_list, redo_list)
            lista.append(list_of_cheltuieli)
        elif op == '5':
            list_of_cheltuieli = ui_adunare_valoare(list_of_cheltuieli, undo_list, redo_list)
            lista.append(list_of_cheltuieli)
        elif op == '6':
            list_of_cheltuieli = ui_max_cheltuiala_pt_tip_cheltuiala(list_of_cheltuieli)
            lista.append(list_of_cheltuieli)
        elif op == '7':
            list_of_cheltuieli = ui_ord_cheltuieli_descrescator_dupa_suma(list_of_cheltuieli, undo_list, redo_list)
            lista.append(list_of_cheltuieli)
        elif op == '8':
            list_of_cheltuieli = ui_sume_lunare(list_of_cheltuieli)
        elif op == 'u':
            list_of_cheltuieli = ui_undo(list_of_cheltuieli, undo_list, redo_list)
        elif op == 'r':
            list_of_cheltuieli = ui_redo(list_of_cheltuieli, undo_list, redo_list)
        elif op == 'a':
            ui_show_all(list_of_cheltuieli)
        elif op == 'x':
            break
        else:
            print('Opțiune invalidă')
    return list_of_cheltuieli
