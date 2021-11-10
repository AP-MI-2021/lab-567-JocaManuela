from Tests.test_CRUD import test_get_cheltuiala_by_ID, test_get_cheltuiala_by_nr_apartament, test_add_cheltuiala, \
                            test_delete_cheltuiala, test_update_cheltuiala
from Tests.test_Domain import test_cheltuiala
from Tests.test_functionalitati import test_delete_all_cheltuieli_pt_apartament, test_adunare_valoare, test_max_cheltuiala_pt_tip_cheltuiala, \
                                       test_ord_cheltuieli_descrescator_dupa_suma, test_sume_lunare, test_undo_redo

def run_all_tests():
    test_get_cheltuiala_by_ID()
    test_get_cheltuiala_by_nr_apartament()
    test_add_cheltuiala()
    test_delete_cheltuiala()
    test_update_cheltuiala()
    test_cheltuiala()
    test_delete_all_cheltuieli_pt_apartament()
    test_adunare_valoare()
    test_max_cheltuiala_pt_tip_cheltuiala()
    test_ord_cheltuieli_descrescator_dupa_suma()
    test_sume_lunare()
    test_undo_redo()
