from pprint import pprint

from church import Personal

p = Personal('en_us')

pprint(p.email())
pprint(p.username())
pprint(p.home_page())
pprint(p.password())
