from yandex_testing_lesson import Rectangle
import pytest


def test_str1():
    with pytest.raises(TypeError):
        Rectangle('42', 24)

def test_str2():
    with pytest.raises(TypeError):
        Rectangle(24, '42')


def test_negative1():
    with pytest.raises(ValueError):
        Rectangle(-15, 55)


def test_negative2():
    with pytest.raises(ValueError):
        Rectangle(15, -55)


def test_list1():
    with pytest.raises(TypeError):
        Rectangle([15], 55)


def test_list2():
    with pytest.raises(TypeError):
        Rectangle(15, [55])


def test_dict1():
    with pytest.raises(TypeError):
        Rectangle({15}, 55)


def test_dict2():
    with pytest.raises(TypeError):
        Rectangle(15, {55})


def test_get_area():
    assert Rectangle(2, 4).get_area() == 8


def test_det_perimeter():
    assert Rectangle(2, 4).get_perimeter() == 12