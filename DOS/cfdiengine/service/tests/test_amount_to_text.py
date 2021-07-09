from . import misc

def test_amount_to_text():
    assert misc.numspatrans(1500) == 'mil quinientos'
