def create_cheltuiala(nr_apartament, suma, data, tipul):
    """
    Creează o nouă cheltuială.
    :param nr_apartament:int, numărul apartamentului cheltuielii
    :param suma:float, suma cheltuielii
    :param data:data în care se face cheltuiala
    :param tipul:str,tipul cheltuielii
    :return: o cheltuială
    """
    #cheltuiala = [nr_apartament, suma, data, tipul]
    #return cheltuiala

    return {
        'nr_apartament': nr_apartament,
        'suma': suma,
        'data': data,
        'tipul': tipul
    }



def get_nr_apartament(cheltuiala):
    """
    Returnează numărul apartamentului pentru o cheltuială.
    :param cheltuiala: cheltuială
    :return: numărul apartamentului pentru cheltuială
    """
    #return cheltuiala[0]
    return cheltuiala['nr_apartament']

def set_nr_apartament(cheltuiala, nr_apartament):
    """
    Setează numărul apartamentului pentru o cheltuială.
    :param cheltuiala: cheltuiala de modificat
    :return: noul număr al apartamentului pentru cheltuială
    """
    cheltuiala['nr_apartament'] = nr_apartament


def get_suma(cheltuiala):
    """
    Returnează suma aferentă cheltuielii.
    :param cheltuiala: cheltuială
    :return: suma cheltuielii
    """
    #return cheltuiala[1]
    return cheltuiala['suma']

def set_suma(cheltuiala, suma):
    """
    Setează suma aferentă cheltuielii.
    :param cheltuiala: cheltuiala de modificat
    :return: noua sumă a cheltuielii
    """
    cheltuiala['suma'] = suma


def get_data(cheltuiala):
    """
    Returnează data în care s-a efectuat cheltuiala.
    :param cheltuiala: cheltuială
    :return: data în care s-a efectuat cheltuiala
    """
    #return cheltuiala[2]
    return cheltuiala['data']

def set_data(cheltuiala, data):
    """
    Setează data în care s-a efectuat cheltuiala.
    :param cheltuiala: cheltuiala de modificat
    :return: noua dată în care s-a efectuat cheltuiala
    """
    cheltuiala['data'] = data


def get_tipul(cheltuiala):
    """
    Returnează tipul cheltuielii.
    :param cheltuiala: cheltuială
    :return: tipul cheltuielii
     """
    #return cheltuiala[3]
    return cheltuiala['tipul']

def set_tipul(cheltuiala, tipul):
    """
    Setează tipul cheltuielii.
    :param cheltuiala: cheltuiala de modificat
    :return: noul tip de cheltuială
    """
    cheltuiala['tipul'] = tipul


def to_string(cheltuiala):
    return f'nr_apartament={get_nr_apartament(cheltuiala)}, suma={get_suma(cheltuiala)}, data={get_data(cheltuiala)}, tipul={get_tipul(cheltuiala)} '