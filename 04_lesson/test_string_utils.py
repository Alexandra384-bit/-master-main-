import pytest
from string_utils import StringUtils

@pytest.fixture
def string_utils():
    return StringUtils()

def test_capitalize(string_utils):
    assert string_utils.capitalize('skypro') == 'Skypro'
    assert string_utils.capitalize('hello world') == 'Hello world'
    assert string_utils.capitalize('') == ''
    assert string_utils.capitalize('123') == '123'

@pytest.mark.parametrize('str1, value', [('shcool', 'Shcool')])
def test_capitalize_parametrize(string_utils, str1, value):
    assert string_utils.capitalize('shcool') == value

def test_trim(string_utils):
    assert string_utils.trim('   skypro') == 'skypro'
    assert string_utils.trim(' hello world') == 'hello world'
    assert string_utils.trim('    ') == ''
    assert string_utils.trim('        123') == '123'
    assert string_utils.trim('[]') == '[]'

def test_contains(string_utils):
    assert string_utils.contains('skypro', 'k') == True
    assert string_utils.contains('hello world', 'h' and 'w') == True
    assert string_utils.contains('  ', 'm') == False
    assert string_utils.contains('123', '2') == True
    assert string_utils.contains('123', '5') == False
    
def test_delete_symbol(string_utils):
    assert string_utils.delete_symbol('skypro', 'r') == 'skypo'
    assert string_utils.delete_symbol('hello world', ' ') == 'helloworld'
    assert string_utils.delete_symbol('123456', '234') == '156'

