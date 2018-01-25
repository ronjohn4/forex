from datasources.util import Currencies
import pytest

@pytest.fixture()
def currency_list():
    return Currencies().list()

def test_USD_in_list(currency_list):
    assert "USD" in currency_list

def test_USD_name():
    assert 'US Dollar' == currency_list['name']

def test_USD_id():
    assert '840' == currency_list['id']

def test_USD_country():
    assert 'USD' == currency_list['country']

def test_USD_units():
    assert '2' == currency_list['units']

def test_USD_countryname():
    assert '' == currency_list['countryname']
