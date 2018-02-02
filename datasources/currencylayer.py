# currencylayer.com
from datasources import util
import requests
import json

mykey = 'cdbbffffc2174c2734d73db22a0e757c'
debug = False


class objectview(object):
    def __init__(self, d):
        self.__dict__ = d

    def __str__(self):
        return 'id:{0}, collectiondate:{1}, collectiontime:{2}, countercurrency:{3}, ' \
               'quotecurrency:{4}, value:{5}'.format(
                                                    self.__dict__['id'],
                                                    self.__dict__['collectiondate'],
                                                    self.__dict__['collectiontime'],
                                                    self.__dict__['countercurrency'],
                                                    self.__dict__['quotecurrency'],
                                                    self.__dict__['value'])


class currency():
    __pair_list = []

    def now(self):
        liveurl = 'http://www.apilayer.net/api/live?access_key={0}'.format(mykey)
        self.__loaddate(liveurl)
        return self.__pair_list

    def history(self, getdate):
        historicalurl = 'http://apilayer.net/api/historical?access_key={0}&date={1}'.format(mykey, getdate)
        self.__loaddate(historicalurl)
        return self.__pair_list

    def __loaddate(self, url):
        if debug:
            # Hardcoded test data ======
            d = '{"success": "True", "timestamp": 1517184850, "source": "USD", "quotes": {"USDYER": 249.949997, ' \
                '"USDBHD": 0.376899, "USDTOP": 2.232601, "USDBMD": 1, "USDBOB": 6.860239, "USDMXN": 18.483801, ' \
                '"USDCRC": 565.999634, "USDERN": 14.990135, "USDWST": 2.495603, "USDGGP": 0.7073, "USDHUF": 248.600006,' \
                ' "USDKRW": 1062.579956, "USDPAB": 1, "USDRSD": 95.181503, "USDSOS": 561.999918, "USDBND": 1.310604, ' \
                '"USDDOP": 48.700001, "USDCAD": 1.23156, "USDMNT": 2412.999804, "USDGMD": 48.419998, "USDAZN": 1.699603, ' \
                '"USDXDR": 0.686995, "USDMYR": 3.865021, "USDANG": 1.779845, "USDSRD": 7.419774, "USDTWD": 29.099001, ' \
                '"USDDJF": 176.830002, "USDAOA": 203.417999, "USDCLF": 0.02222, "USDCVE": 88.749754, "USDLYD": 1.322098, ' \
                '"USDOMR": 0.384499, "USDGYD": 204.860001, "USDFKP": 0.706499, "USDAUD": 1.232096, "USDDKK": 5.991897, ' \
                '"USDBGN": 1.572702, "USDSZL": 11.861697, "USDCDF": 1565.49797, "USDPLN": 3.326206, "USDGHS": 4.538504, ' \
                '"USDALL": 107.249723, "USDSCR": 13.398421, "USDETB": 27.209999, "USDSEK": 7.86949, "USDKYD": 0.820241, ' \
                '"USDAMD": 480.100006, "USDPEN": 3.211502, "USDLKR": 153.699997, "USDBBD": 2, "USDILS": 3.387897, ' \
                '"USDCZK": 20.367098, "USDARS": 19.549999, "USDBTC": 8.6e-05, "USDCNY": 6.319803, "USDMGA": 3180.000015, ' \
                '"USDJPY": 108.533997, "USDUGX": 3621.999748, "USDLAK": 8274.000244, "USDLRD": 127.919998, ' \
                '"USDXCD": 2.694858, "USDJEP": 0.7073, "USDTND": 2.399499, "USDBWP": 9.564405, "USDQAR": 3.6398, ' \
                '"USDJOD": 0.707011, "USDCUP": 26.5, "USDKMF": 411.01001, "USDHKD": 7.8179, "USDMMK": 1329.999531, ' \
                '"USDSGD": 1.306799, "USDLBP": 1510.999899, "USDMWK": 713.47998, "USDGTQ": 7.336001, "USDIQD": 1184, ' \
                '"USDSDG": 6.998198, "USDTZS": 2245.999681, "USDAED": 3.6729, "USDBIF": 1750.97998, "USDPKR": 110.459999, ' \
                '"USDZAR": 11.852503, "USDFJD": 1.986976, "USDSTD": 19719.800781, "USDGBP": 0.70733, "USDNZD": 1.358988, ' \
                '"USDCHF": 0.93398, "USDPYG": 5606.999813, "USDLVL": 0.62055, "USDKGS": 68.364998, "USDCOP": 2805, ' \
                '"USDGNF": 9002.000397, "USDGIP": 0.7067, "USDSHP": 0.7067, "USDXAG": 0.057234, "USDHTG": 63.409994, ' \
                '"USDDZD": 113.468002, "USDIRR": 36774.999856, "USDPGK": 3.159894, "USDXAU": 0.00074, ' \
                '"USDUZS": 8139.999921, "USDMAD": 9.130601, "USDMUR": 32.150002, "USDZWL": 322.355011, ' \
                '"USDZMK": 9001.187314, "USDNAD": 11.868027, "USDAWG": 1.78, "USDSYP": 514.97998, "USDAFN": 69.110001, ' \
                '"USDSBD": 7.743402, "USDIDR": 13304, "USDMOP": 8.047199, "USDIMP": 0.7073, "USDZMW": 9.691543, ' \
                '"USDMVR": 15.57015, "USDTHB": 31.309999, "USDUYU": 28.259789, "USDTJS": 8.808797, "USDMRO": 351.99992, ' \
                '"USDNIO": 30.709999, "USDKZT": 321.209991, "USDMDL": 16.656969, "USDVUV": 104.290001, "USDLTL": 3.048694, ' \
                '"USDISK": 100.199997, "USDJMD": 123.870003, "USDRON": 3.747397, "USDLSL": 11.849666, "USDRWF": 835.75, ' \
                '"USDKPW": 900.00018, "USDBAM": 1.575941, "USDKES": 102.050003, "USDHRK": 5.964797, "USDSVC": 8.750133, ' \
                '"USDTRY": 3.750995, "USDKWD": 0.2992, "USDBRL": 3.152902, "USDBSD": 1, "USDHNL": 23.514999, ' \
                '"USDBTN": 63.599998, "USDNGN": 357.999714, "USDXOF": 519.999763, "USDTTD": 6.744499, "USDGEL": 2.447803, ' \
                '"USDCUC": 1, "USDEUR": 0.804598, "USDBZD": 1.997794, "USDMZN": 59.599998, "USDSLL": 7630.000064, ' \
                '"USDVEF": 9.975034, "USDXPF": 96.375018, "USDUAH": 28.490238, "USDEGP": 17.639999, "USDXAF": 527.369995, ' \
                '"USDKHR": 3999.999952, "USDBYR": 19600, "USDPHP": 50.939999, "USDBDT": 82.860001, "USDRUB": 56.187401, ' \
                '"USDVND": 22709, "USDUSD": 1, "USDMKD": 49.380001, "USDNPR": 101.720001, "USDNOK": 7.68682, ' \
                '"USDSAR": 3.749698, "USDCLP": 602.299988, "USDBYN": 2.019939, "USDTMT": 3.41, "USDINR": 63.568976}, ' \
                '"terms": "https://currencylayer.com/terms", "privacy": "https://currencylayer.com/privacy"}'
            d = json.loads(d)
            ts = '1517191455'
        else:
            r = requests.get(url)
            d = r.json()
            ts = d['timestamp']
            # used to collect test data from a live read
            # print('Test Data start--------------------')
            # print(d)
            # print('Test Data end  --------------------')

        collectiondate = util.unixToDate(ts)
        collectiontime = util.unixToTime(ts)

        self.__pair_list = []

        for k, v in d['quotes'].items():
            self.__pair_list.append(objectview(
                {
                    'collectiondate': collectiondate,
                    'collectiontime': collectiontime,
                    'countercurrency': k[:3],
                    'quotecurrency': k[3:],
                    'value': v
                }
            ))


    def list(self):
        return self.__pair_list
