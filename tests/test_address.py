from church.church import Address, Datetime, BasicData, Personal, Network

a = Address('ru_ru')
# print(a.state_or_subject())
# print(a.street_address())
# print(a.street_name())
# print(a.street_number())
# print(a.telephone())
# print(a.street_suffix())

person = Personal('ru_ru')
# print(person.full_name())
# print(person.gender())
# print(person.profession())
print(person.email())

net = Datetime()
print(net.date( with_time=True))