from Domain.Cheltuiala import create_cheltuiala, get_ID, get_nr_apartament, get_suma, get_data, get_tipul, set_nr_apartament, \
                               set_suma, set_data, set_tipul

def test_cheltuiala():
    cheltuiala = create_cheltuiala('1', 3, 110, '19.10.2021', 'intretinere')
    assert get_ID(cheltuiala) == '1'
    assert get_nr_apartament(cheltuiala) == 3
    assert get_suma(cheltuiala) == 110
    assert get_data(cheltuiala) == '19.10.2021'
    assert get_tipul(cheltuiala) == 'intretinere'

    set_nr_apartament(cheltuiala,4)
    set_suma(cheltuiala, 150)
    set_data(cheltuiala, '21.10.2021')
    set_tipul(cheltuiala,'canal')

    assert get_nr_apartament(cheltuiala) == 4
    assert get_suma(cheltuiala) == 150
    assert get_data(cheltuiala) == '21.10.2021'
    assert get_tipul(cheltuiala) == 'canal'