from copy import deepcopy

from Domain.Cheltuiala import create_cheltuiala, get_ID, get_nr_apartament, get_suma, get_data, get_tipul


def get_cheltuiala_by_ID(list_of_cheltuieli, ID):
    """
    Gaseste o cheltuiala dupa ID-ul acesteia.
    :param list_of_cheltuieli: cheltuielile
    :param ID: ID-ul cheltuielii cautate
    :return:- cheltuiala cautata, daca exista
            -None, daca nu exista
    """
    for cheltuiala in list_of_cheltuieli:
        if get_ID(cheltuiala) == ID:
            return cheltuiala
    return None

def get_cheltuiala_by_nr_apartament(list_of_cheltuieli, nr_apartament):
    """
    Gaseste o cheltuiala dupa numarul apartamentului pentru care se efectueaza aceasta.
    :param list_of_cheltuieli: cheltuielile
    :param nr_apartament: numarul apartamentului pentru care se efectueaza cheltuiala
    :return:- cheltuiala cautata, daca exista
            -None, daca nu exista
    """
    for cheltuiala in list_of_cheltuieli:
        if get_nr_apartament(cheltuiala) == nr_apartament:
            return cheltuiala
    return None

def add_cheltuiala(list_of_cheltuieli, ID, nr_apartament, suma, data, tipul, undo_list=None, redo_list=None):
    """
    Adauga o cheltuiala.
    :param list_of_cheltuieli: cheltuielile
    :param ID: ID-ul cheltuielii
    :param nr_apartament: numarul apartamentului pentru cheltuiala data
    :param suma: suma cheltuielii
    :param data: data in care se face cheltuiala
    :param tipul: tipul cheltuielii
    :param undo_list:
    :param redo_list:
    :return: toate cheltuielile
    """
    if suma < 0:
        raise ValueError('Suma trebuie sa fie un numar pozitiv!')
    if get_cheltuiala_by_ID(list_of_cheltuieli, ID) is not None:
        raise ValueError('Exista deja o cheltuiala cu ID-ul introdus {}'.format(ID))
    if undo_list is not None and redo_list is not None:
        undo_list.append(list_of_cheltuieli)
        redo_list.clear()
    else:
        cheltuiala = create_cheltuiala(ID, nr_apartament, suma, data, tipul)
        result = list_of_cheltuieli + [cheltuiala]
        return result

def delete_cheltuiala(list_of_cheltuieli, ID, undo_list=None, redo_list=None):
    """
    Sterge o cheltuiala dupa ID-ul acesteia.
    :param list_of_cheltuieli: cheltuielile
    :param ID: ID-ul cheltuielii care trebuie stearsa
    :param undo_list:
    :param redo_list:
    :return: o noua lista cu cheluielile ramase
    """
    if get_cheltuiala_by_ID(list_of_cheltuieli, ID) is None:
        raise ValueError('ID-ul dat nu exista!')
    if undo_list is not None and redo_list is not None:
        undo_list.append(list_of_cheltuieli)
        redo_list.clear()
    return [cheltuiala for cheltuiala in list_of_cheltuieli if get_ID(cheltuiala) != ID]

def update_cheltuiala(list_of_cheltuieli, ID, nr_apartament, suma, data, tipul, undo_list=None, redo_list=None):
    """
    Modifica o cheltuiala dupa ID-ul acesteia.
    :param list_of_cheltuieli: cheltuielile
    :param ID: ID-ul cheltuielii care se modifica
    :param nr_apartament: noul numar al apartamentului pentru care se efectueaza cheltuiala
    :param suma: noua suma a cheltuielii
    :param data: noua data in care se efectueaza cheltuiala
    :param tipul: noul tip al  cheltuielii
    :param undo_list:
    :param redo_list:
    :return: o lista cu noile cheltuieli
    """
    if get_cheltuiala_by_ID(list_of_cheltuieli, ID) is None:
        raise ValueError('ID-ul dat nu exista!')
    if suma < 0:
        raise ValueError('Suma trebuie sa fie un numar pozitiv!')
    if undo_list is not None and redo_list is not None:
        undo_list.append(list_of_cheltuieli)
        redo_list.clear()
    new_cheltuieli = []
    for cheltuiala in list_of_cheltuieli:
        if get_ID(cheltuiala) != ID:
            new_cheltuieli.append(cheltuiala)
        else:
            new_cheltuiala = create_cheltuiala(
                get_ID(cheltuiala),
                nr_apartament if nr_apartament != ''
                else get_nr_apartament(cheltuiala),
                suma if suma != ''
                else get_suma(cheltuiala),
                data if data != ''
                else get_data(cheltuiala),
                tipul if tipul != ''
                else get_tipul(cheltuiala)
            )
            new_cheltuieli.append(new_cheltuiala)
    return new_cheltuieli
