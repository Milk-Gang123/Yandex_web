from yandex_testing_lesson import is_under_queen_attack
import pytest


def test_attack_diag():
    assert is_under_queen_attack('a1', 'h8') is True


def test_attack_row():
    assert is_under_queen_attack('a1', 'c1') is True


def test_attack_col():
    assert is_under_queen_attack('a1', 'a8') is True


def test_attack_same():
    assert is_under_queen_attack('a1', 'a1') is True


def test_attack_false():
    assert is_under_queen_attack('a1', 'h7') is False


def test_wrong_size():
    with pytest.raises(ValueError):
        is_under_queen_attack('A1', 'A8')


def test_wrong_pos():
    with pytest.raises(ValueError):
        is_under_queen_attack('a9', 'a1')


def test_wrong_pos2():
    with pytest.raises(ValueError):
        is_under_queen_attack('a1', 'a0')


def test_wrong_number():
    with pytest.raises(ValueError):
        is_under_queen_attack('42', 'a1')


def test_wrong_number2():
    with pytest.raises(ValueError):
        is_under_queen_attack('a2', '41')


def test_wrong_format():
    with pytest.raises(ValueError):
        is_under_queen_attack('1a', 'a2')


def test_wrong_format2():
    with pytest.raises(ValueError):
        is_under_queen_attack('a7', '8a')


def test_int():
    with pytest.raises(TypeError):
        is_under_queen_attack(42, 'a4')


def test_int2():
    with pytest.raises(TypeError):
        is_under_queen_attack('a5', 42)


def test_list():
    with pytest.raises(TypeError):
        is_under_queen_attack(['a', '7'], 'b4')


def test_list2():
    with pytest.raises(TypeError):
        is_under_queen_attack('b8', ['a', '7'])


def test_wrong_length():
    with pytest.raises(ValueError):
        is_under_queen_attack('abc4', 'b4')