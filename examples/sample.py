from pprint import pprint

from church import Address, Personal, ASCIISymbols

p = Personal('en_us')

a = ASCIISymbols

pprint(p.email())
pprint(p.username())
pprint(p.home_page())
pprint(p.password())
print(a.gender_symbol('m'))
pprint(a.emoji())
