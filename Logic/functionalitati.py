from Domain.Cheltuiala import create_cheltuiala, get_nr_apartament, get_suma, get_data, get_tipul


def delete_all_cheltuieli_pt_apartament(list_of_cheltuieli, nr_apartament):
    '''
    Functia sterge toate cheltuielile pentru un apartament dat
    :param list_of_cheltuieli: lista de cheltuieli
    :param nr_apartament: numarul de apartament pentru care se efectueaza stergerea cheltuielilor
    :return: o noua lista cu cheltuielile ramase
    '''
    new_cheltuiala = []
    for cheltuiala in list_of_cheltuieli:
        if get_nr_apartament(cheltuiala) != nr_apartament:
            new_cheltuiala.append(cheltuiala)
    return new_cheltuiala

def adunare_valoare(list_of_cheltuieli, data, valoare):
    """
    Adauga o valoare data la suma unor cheltuieli dintr-o data citita.
    :param list_of_cheltuieli: lista de cheltuieli
    :param data: data pentru care se face adaugarea
    :param valoare: valoarea care se adauga
    :return: o noua lista cu cheltuielile noi
    """
    if valoare < 0:
        raise ValueError('Valoarea de adunat trebuie sa fie un numar pozitiv!')
    new_list = []
    for cheltuiala in list_of_cheltuieli:
        if get_data(cheltuiala) == data:
            new_cheltuiala = create_cheltuiala(
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

def ord_cheltuieli_descrescator_dupa_suma(list_of_cheltuieli):
    """
    Ordoneaza cheltuielile descrescator dupa suma lor.
    :param list_of_cheltuieli: lista de cheltuieli
    :return: o lista cu cheltuielile ordonate descrescator dupa suma
    """
    return sorted(list_of_cheltuieli, key=lambda cheltuiala: get_suma(cheltuiala), reverse=True)