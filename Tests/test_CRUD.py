from Domain.Cheltuiala import create_cheltuiala, get_ID, get_nr_apartament, get_suma, get_data, get_tipul
from Logic.CRUD import add_cheltuiala, delete_cheltuiala, update_cheltuiala, get_cheltuiala_by_ID, get_cheltuiala_by_nr_apartament


def test_get_cheltuiala_by_ID():
    cheltuieli = []
    c1 = create_cheltuiala('1', 2, 12, '12.12.2020', 'canal')
    c2 = create_cheltuiala('2', 5, 110, '10.05.2021', 'intretinere')
    cheltuieli = add_cheltuiala(cheltuieli, get_ID(c1), get_nr_apartament(c1), get_suma(c1), get_data(c1), get_tipul(c1))
    cheltuieli = add_cheltuiala(cheltuieli, get_ID(c2), get_nr_apartament(c2), get_suma(c2), get_data(c2), get_tipul(c2))

    assert get_cheltuiala_by_ID(cheltuieli, '1') is not None
    assert get_cheltuiala_by_ID(cheltuieli, '2') is not None
    assert get_cheltuiala_by_ID(cheltuieli, '3') is None

def test_get_cheltuiala_by_nr_apartament():
    cheltuieli = []
    c1 = create_cheltuiala('1', 2, 12, '12.12.2020', 'canal')
    c2 = create_cheltuiala('2', 5, 110, '10.05.2021', 'intretinere')
    cheltuieli = add_cheltuiala(cheltuieli, get_ID(c1), get_nr_apartament(c1), get_suma(c1), get_data(c1), get_tipul(c1))
    cheltuieli = add_cheltuiala(cheltuieli, get_ID(c2), get_nr_apartament(c2), get_suma(c2), get_data(c2), get_tipul(c2))

    assert get_cheltuiala_by_nr_apartament(cheltuieli, 2) is not None
    assert get_cheltuiala_by_nr_apartament(cheltuieli, 5) is not None
    assert get_cheltuiala_by_nr_apartament(cheltuieli, 8) is None

def test_add_cheltuiala():
    cheltuieli = []
    c1 = create_cheltuiala('1', 1, 12, '12.12.2020', 'canal')
    cheltuieli = add_cheltuiala(cheltuieli, get_ID(c1), get_nr_apartament(c1), get_suma(c1), get_data(c1), get_tipul(c1))
    assert cheltuieli == [c1]
    c2 = create_cheltuiala('2', 5, 110, '10.05.2021', 'intretinere')
    cheltuieli = add_cheltuiala(cheltuieli, get_ID(c2),  get_nr_apartament(c2), get_suma(c2), get_data(c2), get_tipul(c2))
    assert cheltuieli == [c1, c2]


def test_delete_cheltuiala():
    c1 = create_cheltuiala('1', 1, 100, '10.05.2021', 'intretinere')
    c2 = create_cheltuiala('2', 5, 110, '10.05.2021', 'canal')
    c3 = create_cheltuiala('3', 13, 200, '10.05.2021', 'intretinere')
    cheltuieli = []
    cheltuieli = add_cheltuiala(cheltuieli, get_ID(c1), get_nr_apartament(c1), get_suma(c1), get_data(c1), get_tipul(c1))
    cheltuieli = add_cheltuiala(cheltuieli, get_ID(c2), get_nr_apartament(c2), get_suma(c2), get_data(c2), get_tipul(c2))
    cheltuieli = add_cheltuiala(cheltuieli, get_ID(c3), get_nr_apartament(c3), get_suma(c3), get_data(c3), get_tipul(c3))
    cheltuieli = delete_cheltuiala(cheltuieli, get_ID(c2))
    assert cheltuieli == [c1, c3]


def test_update_cheltuiala():
    c1 = create_cheltuiala('1', 1, 100, '10.04.2021', 'intretinere')
    cheltuieli = []
    cheltuieli = add_cheltuiala(cheltuieli, get_ID(c1), get_nr_apartament(c1), get_suma(c1), get_data(c1), get_tipul(c1))
    c2 = create_cheltuiala('1', 2, 200, '12.04.2021', 'intretinere')
    cheltuieli = update_cheltuiala(cheltuieli, get_ID(c2), get_nr_apartament(c2), get_suma(c2),get_data(c2), get_tipul(c2))
    assert cheltuieli == [c2]
