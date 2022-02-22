from yandex_testing_lesson import count_chars
import pytest


def test_empty():
    assert count_chars('') == {}

def test_str1():
    assert count_chars('a') == {'a': 1}

def test_str2():
    assert count_chars('ded') == {'d': 2, 'e': 1}


def test_int():
    with pytest.raises(TypeError):
        count_chars(42)

def test_list():
    with pytest.raises(TypeError):
        count_chars(['mozk'])