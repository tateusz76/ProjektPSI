print('{:{align}{width}}'.format('test', align='^', width='12'))

print('{:{width}.{prec}f}'.format(5.364265, width=12, prec=3))

from datetime import datetime
dt = datetime(2021, 10, 15, 10, 44)
print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%Y-%m-%d', tfmt='%H:%M'))

print('{:{}{sign}{}.{}}'.format(3.1465626, '>', 5, 5, sign='+'))

class Plant(object):
    type = 'krzok'
    kinds = [{'name': 'jerzyna'}, {'name': 'jerzynaaleinna'}]
print('{p.type}: {p.kinds[0][name]}'.format(p=Plant()))