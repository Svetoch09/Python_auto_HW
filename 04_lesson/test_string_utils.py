import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("Skypro", "Skypro"),
    ("SKYPRO", "Skypro"),
    ("sKYPRO", "Skypro"),
    ("skyPro", "Skypro"),
    (" skypro", " skypro"),
    ("hello world", "Hello world"),
    ("привет", "Привет"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("!@#$%^&*", "!@#$%^&*"),
    ("😝", "😝"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str", [
    12345,
    None,
])
def test_capitalize_raises_attribute_error(input_str):
    # Ожидаем, что при выполнении этой функции возникнет AttributeError
    with pytest.raises(AttributeError):
        string_utils.capitalize(input_str)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    ("    SKYPRO", "SKYPRO"),
    (" Привет", "Привет"),
    (" python ", "python "),
    (" 123go", "123go"),
    (" hello world", "hello world"),
    (" !@#$%^&*", "!@#$%^&*"),
    (" 😝", "😝"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", ""),
    ("skypro", "skypro"),
    ("python ", "python "),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str", [
    12345,
    None,
])
def test_trim_raises_attribute_error(input_str):
    with pytest.raises(AttributeError):
        string_utils.trim(input_str)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("skypro", "s", True),
    ("skypro", "y", True),
    ("skypro", "o", True),
    ("banana", "a", True),
    ("skypro", "skypro", True),
    ("SKYPRO", "K", True),
    ("test 12345", "4", True),
    ("!@#$%^&*", "%", True),
    ("😝", "😝", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("skypro", "n", False),
    ("skypro", "P", False),
    ("SKYPRO", "r", False),
    ("SKYPRO", "", True),
    ("hello world", " ", True),
    ("     ", " ", True),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol", [
    (12345, 2),
    (None, "N")
    ])
def test_contains_raises_attribute_error(input_str, symbol):
    with pytest.raises(AttributeError):
        string_utils.contains(input_str, symbol)


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("skypro", "p", "skyro"),
    ("delete", "delete", ""),
    ("привет", "п", "ривет"),
    ("SkyPro", "Pro", "Sky"),
    ("SKYPRO", "O", "SKYPR"),
    ("Banana", "a", "Bnn"),
    ("hello world", " ", "helloworld"),
    ("sky1pro", "1", "skypro"),
    ("12345", "34", "125"),
    ("100 dollars", "0", "1 dollars"),
])
def test_delete_simbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("skypro", "n", "skypro"),
    ("SKYPRO", "s", "SKYPRO"),
    ("", "s", ""),
    ("skypro", "", "skypro"),
])
def test_delete_simbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol", [
    (12345, 2),
    (None, "N")
    ])
def test_delete_raises_attribute_error(input_str, symbol):
    with pytest.raises(AttributeError):
        string_utils.contains(input_str, symbol)
