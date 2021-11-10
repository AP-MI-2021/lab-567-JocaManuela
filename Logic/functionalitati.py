from Domain.Cheltuiala import create_cheltuiala, get_ID, get_nr_apartament, get_suma, get_data, get_tipul
from Logic.CRUD import get_cheltuiala_by_nr_apartament


def delete_all_cheltuieli_pt_apartament(list_of_cheltuieli, nr_apartament, undo_list=None, redo_list=None):
    '''
    Functia sterge toate cheltuielile pentru un apartament dat.
    :param list_of_cheltuieli: lista de cheltuieli
    :param nr_apartament: numarul de apartament pentru care se efectueaza stergerea cheltuielilor
    :param undo_list:
    :param redo_list:
    :return: o noua lista cu cheltuielile ramase
    '''

    if get_cheltuiala_by_nr_apartament(list_of_cheltuieli, nr_apartament) is None:
        raise ValueError('Numarul apartamentului dat nu exista!')
    if undo_list is not None and redo_list is not None:
        undo_list.append(list_of_cheltuieli)
        redo_list.clear()
    new_cheltuiala = []
    for cheltuiala in list_of_cheltuieli:
        if get_nr_apartament(cheltuiala) != nr_apartament:
            new_cheltuiala.append(cheltuiala)
    return new_cheltuiala

def adunare_valoare(list_of_cheltuieli, data, valoare, undo_list=None, redo_list=None):
    """
    Aduna o valoare data la toate cheltuielile dintr-o data citita.
    :param list_of_cheltuieli: lista de cheltuieli
    :param data: data pentru care se face adunarea
    :param valoare: valoarea care se aduna
    :param undo_list:
    :param redo_list:
    :return: o noua lista cu cheltuielile noi
    """
    if valoare < 0:
        raise ValueError('Valoarea de adunat trebuie sa fie un numar pozitiv!')
    if undo_list is not None and redo_list is not None:
        undo_list.append(list_of_cheltuieli)
        redo_list.clear()
    new_list = []
    for cheltuiala in list_of_cheltuieli:
        if get_data(cheltuiala) == data:
            new_cheltuiala = create_cheltuiala(
               get_ID(cheltuiala),
               get_nr_apartament(cheltuiala),
               get_suma(cheltuiala) + valoare,
               get_data(cheltuiala),
               get_tipul(cheltuiala)
            )
            new_list.append(new_cheltuiala)
        else:
            new_list.append(cheltuiala)
    return new_list

def max_cheltuiala_pt_tip_cheltuiala(list_of_cheltuieli):
    """
    Determina cea mai mare cheltuiala pentru fiecare tip de cheltuiala.
    :param list_of_cheltuieli: lista de cheltuieli
    :return: un dictionar cu prop. ceruta
    """
    tip_cheltuieli = {}
    for cheltuiala in list_of_cheltuieli:
        tip = get_tipul(cheltuiala)
        suma = get_suma(cheltuiala)
        if tip in tip_cheltuieli:
            if get_suma(tip_cheltuieli[tip]) < suma:
                tip_cheltuieli[tip] = cheltuiala
        else:
            tip_cheltuieli[tip] = cheltuiala
    return tip_cheltuieli

def ord_cheltuieli_descrescator_dupa_suma(list_of_cheltuieli, undo_list=None, redo_list=None):
    """
    Ordoneaza cheltuielile descrescator dupa suma lor.
    :param list_of_cheltuieli: lista de cheltuieli
    :param undo_list:
    :param redo_list:
    :return: o lista cu cheltuielile ordonate descrescator dupa suma
    """
    if undo_list is not None and redo_list is not None:
        undo_list.append(list_of_cheltuieli)
        redo_list.clear()
    return sorted(list_of_cheltuieli, key=lambda cheltuiala: get_suma(cheltuiala), reverse=True)

def sume_lunare(list_of_cheltuieli):
    """
    Functia afiseaza sumele lunare pentru fiecare apartament.
    """
    rezultat = {}
    for cheltuiala in list_of_cheltuieli:
        nr_apartament = get_nr_apartament(cheltuiala)
        rezultat[nr_apartament] = luni_apartament(list_of_cheltuieli, nr_apartament)
    return rezultat

def luni_apartament(list_of_cheltuieli, nr_apartament):
    '''
    Functia afiseaza toate cheltuielile.
    '''
    lista = [['ianuarie', 0], ['februarie', 0], ['martie', 0],['aprilie', 0], ['mai', 0], ['iunie', 0], ['iulie', 0],
             ['august', 0], ['septembrie', 0], ['octombrie', 0], ['noiembrie', 0], ['decembrie', 0]]
    for cheltuiala in list_of_cheltuieli:
        data = get_data(cheltuiala)
        luna = data.split('.')[1]
        if nr_apartament == get_nr_apartament(cheltuiala):
            if luna == '01':
                suma = float(get_suma(cheltuiala))
                lista[0][1] = lista[0][1] + suma
            elif luna == '02':
                suma = float(get_suma(cheltuiala))
                lista[1][1] = lista[1][1] + suma
            elif luna == '03':
                suma = float(get_suma(cheltuiala))
                lista[2][1] = lista[2][1] + suma
            elif luna == '04':
                suma = float(get_suma(cheltuiala))
                lista[3][1] = lista[3][1] + suma
            elif luna == '05':
                suma = float(get_suma(cheltuiala))
                lista[4][1] = lista[4][1] + suma
            elif luna == '06':
                suma = float(get_suma(cheltuiala))
                lista[5][1] = lista[5][1] + suma
            elif luna == '07':
                suma = float(get_suma(cheltuiala))
                lista[6][1] = lista[6][1] + suma
            elif luna == '08':
                suma = float(get_suma(cheltuiala))
                lista[7][1] = lista[7][1] + suma
            elif luna == '09':
                suma = float(get_suma(cheltuiala))
                lista[8][1] = lista[8][1] + suma
            elif luna == '10':
                suma = float(get_suma(cheltuiala))
                lista[9][1] = lista[9][1] + suma
            elif luna == '11':
                suma = float(get_suma(cheltuiala))
                lista[10][1] = lista[10][1] + suma
            elif luna == '12':
                suma = float(get_suma(cheltuiala))
                lista[11][1] = lista[11][1] + suma
    return lista

def do_undo(undo_list, redo_list, current_list):
    """
    Șterge ultima operațiune făcută
    :param undo_list: lista dupa stergere
    :param redo_list: lista dinaintea stergerii
    :param current_list: lista curenta
    :return: lista dupa ce a avut loc undo
    """
    if len(undo_list) > 0:
        redo_list.append(current_list)
        return undo_list.pop()
    return current_list


def do_redo(undo_list, redo_list, current_list):
    """
    Revine la operațiunea dinaintea ștergerii
    :param undo_list: lista dupa stergere
    :param redo_list: lista dinaintea stergerii
    :param current_list: lista curenta
    :return:
    """
    if len(redo_list) > 0:
        undo_list.append(current_list)
        return redo_list.pop()
    return current_list




