from datasources import currencylayer, datautil
import datetime

db = datautil.forexDB()
d = datetime.date(2018, 1, 1)
print('Starting to check for data on:', d)

while True:
    if not db.date_already_saved(d):
        print('loading:', d)
        currlayer = currencylayer.currency().history(str(d))
        for v in currlayer:
            db.add_pair(
                collectiondate=v.collectiondate,
                collectiontime=v.collectiontime,
                countercurrency=v.countercurrency,
                quotecurrency=v.quotecurrency,
                value=v.value
            )

    d = d + datetime.timedelta(days=1)
    # if d == datetime.date(2018, 2, 1):
    if d == datetime.date.today():
        print('Current to:', d)
        break
