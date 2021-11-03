from Domain.Cheltuiala import create_cheltuiala, get_ID, get_nr_apartament, get_suma, get_data, get_tipul
from Logic.functionalitati import delete_all_cheltuieli_pt_apartament, adunare_valoare, max_cheltuiala_pt_tip_cheltuiala, \
                                   ord_cheltuieli_descrescator_dupa_suma, sume_lunare
from Logic.CRUD import add_cheltuiala



def test_delete_all_cheltuieli_pt_apartament():
    cheltuieli = []
    c1 = create_cheltuiala('1', 1, 100, '10.04.2021', 'intretinere')
    c2 = create_cheltuiala('2', 2, 200, '12.04.2021', 'intretinere')
    c3 = create_cheltuiala('3', 2, 300, '12.04.2021', 'intretinere')
    cheltuieli = add_cheltuiala(cheltuieli, get_ID(c1), get_nr_apartament(c1), get_suma(c1), get_data(c1),get_tipul(c1))
    cheltuieli = add_cheltuiala(cheltuieli, get_ID(c2), get_nr_apartament(c2), get_suma(c2), get_data(c2),get_tipul(c2))
    cheltuieli = add_cheltuiala(cheltuieli, get_ID(c3), get_nr_apartament(c3), get_suma(c3), get_data(c3),get_tipul(c3))
    cheltuieli = delete_all_cheltuieli_pt_apartament(cheltuieli, 2)
    assert cheltuieli == [c1]


def test_adunare_valoare():
    cheltuieli = []
    c1 = create_cheltuiala('1', 1, 100, '10.04.2021', 'intretinere')
    c2 = create_cheltuiala('2', 2, 200, '12.04.2021', 'intretinere')
    c3 = create_cheltuiala('3', 2, 300, '12.04.2021', 'canal')
    cheltuieli = add_cheltuiala(cheltuieli, get_ID(c1), get_nr_apartament(c1), get_suma(c1), get_data(c1), get_tipul(c1))
    cheltuieli = add_cheltuiala(cheltuieli, get_ID(c2), get_nr_apartament(c2), get_suma(c2), get_data(c2), get_tipul(c2))
    cheltuieli = add_cheltuiala(cheltuieli, get_ID(c3), get_nr_apartament(c3), get_suma(c3), get_data(c3), get_tipul(c3))
    cheltuieli = adunare_valoare(cheltuieli, '12.04.2021', 5)
    c4 = create_cheltuiala('2', 2, 205, '12.04.2021', 'intretinere')
    c5 = create_cheltuiala('3', 2, 305, '12.04.2021', 'canal')
    assert cheltuieli == [c1, c4, c5]


def test_max_cheltuiala_pt_tip_cheltuiala():
    cheltuieli = []
    c1 = create_cheltuiala('1', 1, 100, '10.04.2021', 'intretinere')
    c2 = create_cheltuiala('2', 2, 200, '12.04.2021', 'intretinere')
    c3 = create_cheltuiala('3', 2, 300, '12.04.2021', 'canal')
    cheltuieli = add_cheltuiala(cheltuieli, get_ID(c1), get_nr_apartament(c1), get_suma(c1), get_data(c1),get_tipul(c1))
    cheltuieli = add_cheltuiala(cheltuieli, get_ID(c2), get_nr_apartament(c2), get_suma(c2), get_data(c2),get_tipul(c2))
    cheltuieli = add_cheltuiala(cheltuieli, get_ID(c3), get_nr_apartament(c3), get_suma(c3), get_data(c3),get_tipul(c3))
    chelt_max = max_cheltuiala_pt_tip_cheltuiala(cheltuieli)
    assert chelt_max == {'intretinere': c2, 'canal': c3}

def test_ord_cheltuieli_descrescator_dupa_suma():
    cheltuieli = []
    c1 = create_cheltuiala('1', 1, 100, '10.04.2021', 'intretinere')
    c2 = create_cheltuiala('2', 2, 200, '12.04.2021', 'intretinere')
    cheltuieli = add_cheltuiala(cheltuieli, get_ID(c1), get_nr_apartament(c1), get_suma(c1), get_data(c1), get_tipul(c1))
    cheltuieli = add_cheltuiala(cheltuieli, get_ID(c2), get_nr_apartament(c2), get_suma(c2), get_data(c2), get_tipul(c2))
    cheltuieli = ord_cheltuieli_descrescator_dupa_suma(cheltuieli)
    assert cheltuieli == [c2, c1]

def test_sume_lunare():
    cheltuieli = []
    c1 = create_cheltuiala('1', 1, 100, '10.04.2019', 'intretinere')
    c2 = create_cheltuiala('2', 2, 200, '12.04.2019', 'intretinere')
    c3 = create_cheltuiala('3', 1, 100, '10.04.2019', 'canal')
    c4 = create_cheltuiala('4', 2, 100, '12.05.2019', 'canal')
    cheltuieli = add_cheltuiala(cheltuieli, get_ID(c1), get_nr_apartament(c1), get_suma(c1), get_data(c1), get_tipul(c1))
    cheltuieli = add_cheltuiala(cheltuieli, get_ID(c2), get_nr_apartament(c2), get_suma(c2), get_data(c2), get_tipul(c2))
    cheltuieli = add_cheltuiala(cheltuieli, get_ID(c3), get_nr_apartament(c3), get_suma(c3), get_data(c3), get_tipul(c3))
    cheltuieli = add_cheltuiala(cheltuieli, get_ID(c4), get_nr_apartament(c4), get_suma(c4), get_data(c4), get_tipul(c4))
    result = sume_lunare(cheltuieli)
    assert result == {1: [['ianuarie', 0], ['februarie', 0], ['martie', 0], ['aprilie', 200], ['mai', 0], ['iunie', 0],
                          ['iulie', 0], ['august', 0], ['septembrie', 0], ['octombrie', 0], ['noiembrie', 0],
                          ['decembrie', 0]], 2: [['ianuarie', 0], ['februarie', 0], ['martie', 0], ['aprilie', 200],
                                                 ['mai', 100], ['iunie', 0], ['iulie', 0], ['august', 0],
                                                 ['septembrie', 0], ['octombrie', 0], ['noiembrie', 0], ['decembrie', 0]]}