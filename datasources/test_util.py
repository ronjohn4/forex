from datasources.util import Currencies
import pytest

curr_list = Currencies().list()

@pytest.fixture()
def currency_list():
    return curr_list

def test_USD_in_list(currency_list):
    assert "USD" in currency_list

def test_USD_name(currency_list):
    assert 'US Dollar' == currency_list['USD'].name

def test_USD_id(currency_list):
    assert '840' == currency_list['USD'].id

def test_USD_currency(currency_list):
    assert 'USD' == currency_list['USD'].currency

def test_USD_countryname(currency_list):
    assert 'UNITED STATES OF AMERICA (THE)' in currency_list['USD'].countryname

def test_listcount(currency_list):
    assert 178 == len(currency_list)


