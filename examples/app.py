from church import Address, Personal

address = Address('en_us')

print(address.country())
print(address.street_address())

person = Personal('ru_ru')
print(person.email())
print(person.favorite_movie())