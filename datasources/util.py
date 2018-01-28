import requests
import xmltodict

url = "https://www.currency-iso.org/dam/downloads/lists/list_one.xml"


class objectview(object):
    def __init__(self, d):
        self.__dict__ = d

    def __str__(self):
        return 'id:{0}, currency:{1}, name:{2}, countryname:{3}'.format(self.__dict__['id'],
                                                                        self.__dict__['currency'],
                                                                        self.__dict__['name'],
                                                                        self.__dict__['countryname'])

class Currencies():
    __currency_list = {}

    def __init__(self):
        if not self.__currency_list:
            r = requests.get(url)
            doc = xmltodict.parse(r.text)
            for v in doc['ISO_4217']['CcyTbl']['CcyNtry']:
                try:
                    if v['Ccy'] in self.__currency_list:
                        self.__currency_list[v['Ccy']].countryname.append(v['CtryNm'])
                    else:
                        self.__currency_list[v['Ccy']] = objectview({'name' : v['CcyNm'],
                                                          'id' : v['CcyNbr'],
                                                          'countryname' : [v['CtryNm']],
                                                          'currency': v['Ccy']})
                except:
                    pass    #country with no currency like Antarctica and Palestine


    def list(self):
        return self.__currency_list
