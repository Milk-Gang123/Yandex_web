from reverse import reverse
import pytest


def test_empty():
    assert reverse('') == ''

def test_sym():
    assert reverse('a') == 'a'

def test_pol():
    assert reverse('дед') == 'дед'

def test_str():
    assert reverse('дедвнутри') == 'иртунвдед'

def test_int():
    with pytest.raises(TypeError):
        reverse(42)

def test_list():
    with pytest.raises(TypeError):
        reverse(['mozk'])