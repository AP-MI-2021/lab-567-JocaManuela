from copy import deepcopy

from Domain.Cheltuiala import create_cheltuiala, get_nr_apartament


def get_cheltuiala_by_nr_apartament(list_of_cheltuieli, nr_apartament):
    """
    Gaseste o cheltuiala dupa numarul apartamentului pentru care se efectueaza aceasta
    :param list_of_cheltuieli: cheltuielile
    :param nr_apartament: numarul apartamentului pentru care se efectueaza cheltuiala
    :return:- cheltuiala cautata, daca exista
            -None, daca nu exista
    """
    for cheltuiala in list_of_cheltuieli:
        if get_nr_apartament(cheltuiala) == nr_apartament:
            return cheltuiala
    return None

def add_cheltuiala(list_of_cheltuieli, nr_apartament, suma, data, tipul):
    """
    Adauga o cheltuiala
    :param list_of_cheltuieli: cheltuielile
    :param nr_apartament: numarul apartamentului pentru noua cheltuiala
    :param suma: suma noii cheltuieli
    :param data: data in care se face noua cheltuiala
    :param tipul: tipul noii cheltuieli
    :return: toate cheltuielile
    """
    cheltuiala = create_cheltuiala(nr_apartament, suma, data, tipul)
    result = list_of_cheltuieli + [cheltuiala]
    return result


def delete_cheltuiala(list_of_cheltuieli, nr_apartament):
    """
    Sterge o cheltuiala dupa numarul de apartament pentru care se efectueaza.
    :param list_of_cheltuieli: cheltuielile
    :param nr_apartament: numarul de apartament pentru care se efectueaza stergerea cheltuielii
    :return: o noua lista cu cheluielile ramase
    """
    return [cheltuiala for cheltuiala in list_of_cheltuieli if get_nr_apartament(cheltuiala) != nr_apartament]

def update_cheltuiala(list_of_cheltuieli, nr_apartament, suma, data, tipul):
    """
    Modifica o cheltuiala dupa numarul de apartament pentru care se efectueaza aceasta.
    :param list_of_cheltuieli: cheltuielile
    :param nr_apartament: numarul apartamentului pentru cheltuiala data
    :param suma: suma cheltuielii
    :param data: data in care s-a facut cheltuiala
    :param tipul: tipul cheltuielii
    :return: o lista cu noile cheltuieli
    """
    new_cheltuieli = []
    for cheltuiala in list_of_cheltuieli:
        if get_nr_apartament(cheltuiala) == nr_apartament:
            new_cheltuiala = create_cheltuiala(nr_apartament, suma, data, tipul)
            new_cheltuieli.append(new_cheltuiala)

        else:
            new_cheltuieli.append(cheltuiala)

    return new_cheltuieli
