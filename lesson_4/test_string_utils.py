import pytest
from string_utils import StringUtils

utils = StringUtils()


@pytest.mark.parametrize("test_input,expected", [
    ("skypro", "Skypro"),
    ("лето осень", "Лето осень"),
    (" ", " "),
    (" 123", " 123"),
    (" sun ", " sun ")
])
def test_capitilize(test_input, expected):
    assert utils.capitilize(test_input) == expected


@pytest.mark.xfail()
def test_capitilize_with_numbers():
    assert utils.capitilize("123") == "123"


@pytest.mark.parametrize("test_input,expected", [
    (" skypro", "skypro"),
    (" Frozen ", "Frozen "),
    ("  Summer", "Summer"),
    (" ", "")
    ])
def test_trim(test_input, expected):
    assert utils.trim(test_input) == expected


@pytest.mark.xfail()
def test_trim_with_space():
    assert utils.trim(" Sun") == " Sun"


@pytest.mark.xfail()
def test_trim_with_numbers():
    assert utils.trim(" 123") == " 123"


@pytest.mark.parametrize("string, delimeter, result", [
    ("1,2,3,4", ",", ["1", "2", "3", "4"]),
    ("a@b@c@d", "@", ["a", "b", "c", "d"]),
    (" ", None, []),
    ("Tom,Alex,Emmy", None, ["Tom", "Alex", "Emmy"])
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result


@pytest.mark.parametrize("string, symbol, result", [
    ("Лето", "Л", True),
    ("summer", "s", True),
    (" 123", "1", True),
    ("", "", True),
    ("Winter", "y", False),
    ("123", "9", False),
    ("Бобэр", "к", False)
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result


@pytest.mark.parametrize("string, symbol, result", [
    ("Лето", "Л", "ето"),
    ("summer", "r", "summe"),
    ("123 ", "3", "12 "),
    ("", "", ""),
    ("Winter", "y", "Winter"),
    ("123", "9", "123"),
    ("Бобэр", "к", "Бобэр")
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result


@pytest.mark.parametrize("string, symbol, result", [
    ("Лето", "Л", True),
    ("summer", "s", True),
    ("123", "1", True),
    (" 123", " ", True),
    ("", "", True),
    ("Winter", "K", False),
    ("123", "8", False),
    ("Бобэр", "к", False)
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    ("Лето", "о", True),
    ("summer", "r", True),
    ("123 ", " ", True),
    ("123", "3", True),
    ("", "", True),
    ("Winter", "y", False),
    ("123", "9", False),
    ("Бобэр", "к", False)
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result


@pytest.mark.parametrize("string, result", [
    ("", True),
    (" ", True),
    ("  ", True),
    ("123", False),
    ("@@", False),
    ("   1  ", False)
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result


@pytest.mark.parametrize("lst, joiner, result", [
    (["1, 2, 3, 4"], "-", "1, 2, 3, 4"),
    (["I", "Love", "Winter"], "@", "I@Love@Winter"),
    (["Девять", "Пять"], "Минус", "ДевятьМинусПять"),
    (["9", "5"], "", "95"),
    ([], "-", ""),
    ([], "пять", "")
])
def test_list_to_string(lst, joiner, result):
    if joiner is None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result