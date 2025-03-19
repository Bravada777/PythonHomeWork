import pytest
from string_utils import StringUtils

utils = StringUtils()

@pytest.mark.parametrize("input_str, expected_output", [
    ("skypro", "Skypro"),              # Простой случай
    ("abc", "Abc"),                    # Первая буква уже заглавная
    ("  hello", " Hello"),             # Пробелы в начале
    ("HELLO", "Hello"),                # Весь текст заглавными буквами
    ("", ""),                          # Пустая строка
])
def test_capitalize(input_str, expected_output):
    assert utils.capitalize(input_str) == expected_output


@pytest.mark.parametrize("input_str, expected_output", [
    ("   skypro", "skypro"),           # Простой случай
    ("hello   ", "hello   "),          # Пробелы справа
    ("  abc  ", "abc  "),              # Пробелы слева и справа
    ("", ""),                          # Пустая строка
])
def test_trim(input_str, expected_output):
    assert utils.trim(input_str) == expected_output


@pytest.mark.parametrize("input_str, symbol, expected_output", [
    ("SkyPro", "S", True),             # Символ присутствует
    ("SkyPro", "U", False),            # Символ отсутствует
    ("abba", "b", True),               # Несколько совпадений
    ("", "", False),                   # Пустые строки
    ("abcdef", "z", False),            # Нет совпадений
])
def test_contains(input_str, symbol, expected_output):
    assert utils.contains(input_str, symbol) == expected_output


@pytest.mark.parametrize("input_str, symbol, expected_output", [
    ("SkyPro", "k", "SyPro"),          # Один символ
    ("SkyPro", "Pro", "Sky"),          # Подстрока
    ("aaaa", "a", ""),                 # Удаляются все символы
    ("Hello World", "l", "Heo Wor"),   # Несколько символов
    ("", "", ""),                      # Пустые строки
])
def test_delete_symbol(input_str, symbol, expected_output):
    assert utils.delete_symbol(input_str, symbol) == expected_output


@pytest.mark.negative
def test_none_input():
    with pytest.raises(TypeError):
        utils.capitalize(None)
        utils.trim(None)
        utils.contains(None, None)
        utils.delete_symbol(None, None)