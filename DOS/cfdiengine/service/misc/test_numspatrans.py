from numspatrans import numspatrans

def test_amount_to_text():
    assert numspatrans(1500) == 'mil quinientos ', 'Error: no traduce bien el valor 1500'
