import requests
import xmltodict

url = "https://www.currency-iso.org/dam/downloads/lists/list_one.xml"


class Currencies():
    __currency_list = {}

    def __init__(self):
        r = requests.get(url)
        doc = xmltodict.parse(r.text)
        for v in doc['ISO_4217']['CcyTbl']['CcyNtry']:
            try:
                self.__currency_list[v['Ccy']] = dict(v)
            except:
                pass    #Antarctica doesn't have all fields

    def list(self):
        return self.__currency_list
