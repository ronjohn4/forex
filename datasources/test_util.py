from datasources.util import Currencies

def test_USD_in_list():
    cl = Currencies()
    assert "USD" in cl.list()
