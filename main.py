from datasources import util

cl = util.Currencies().list()
for k,v in cl.items():
    print(v)

