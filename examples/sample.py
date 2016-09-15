from church import Address, Datetime, Science

p = Datetime('en_us')
sci = Science('en_us')

print(p.month(), p.month(abbreviated=True))
print(sci.article_on_wiki())
print(sci.scientist())