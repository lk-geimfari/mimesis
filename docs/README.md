## Small guidebook [v0.1.9]

## Personal
```python

person = Personal('en_us')

# Get a random integer value.
# For example: 21
age = person.age(minimum=17, maximum=35)

# Get a random name.
# For example: Christina
name = person.name()

# Get a random surname.
# For example: Wolf
surname = person.surname()

# Get a random full name.
# For example: Leo Johnson.
full_name = person.full_name(gender='m')

# Get a random username.
# For example: foretime10
username = person.username()

# Generate a random password.
password = person.password(length=15)

# Generate a random email using usernames.
# For example: foretime10@live.com
email = person.email()

# Generate a random home page using usernames.
# For example: http://www.font6.info
home_page = person.home_page()

# Get a random subreddit thread from list. 
# If nsfw=True then will be returned NSFW subreddit
# For example: /r/games
subreddit = p.subreddit(nsfw=False, full_url=False)

# Bitcoin address. Support only 2 most common format: 'P2PKH' and 'P2SH'
# For example:
bitcoin = person.bitcoin(address_format='p2sh')

# Generate a random card verification value (CVV)
# For example: 731
cvv = person.cvv()

# Generate a random CID code.
# For example: 7834
cid = person.cid()

# Generate a random credit card number (Visa or MasterCard)
# For example: 3519 2073 7960 3241
credit_card = person.credit_card_number()

# Get a random gender.
# For example: Male or M if abbreviated=True
gender = person.gender(abbreviated=True)

# Get a random profession.
# For example: Programmer
profession = person.profession()

# Get a random political views.
# For example: Liberal
political_views = person.political_views()

# Get a random worldview
# For example: Naturalistic Pantheism
worldview = person.worldview()

# Get a random views on.
# For example: Negative
views_on = person.views_on()

# Get a random nationality.
# For example: Russian
nationality = person.nationality()

# Get a random university.
# For example: MIT
university = person.university()

# Get a random qualification.
# For example: Master
qualification = person.qualification()

# Get a random language.
# For example: Russian
language = person.language()

# Get a random movie.
# For example: Pulp Fiction
favorite_movie = person.favorite_movie()

# Generate a random phone number.
# For example: +7-(963)409-11-22
telephone = person.telephone()

```

## Datetime
```python
datetime = Datetime('en_us')

# Get a random day of week.
# For example: Sun.
day_of_week = datetime.day_of_week(abbreviated=True)

# Get a random month.
# For example:  Dec.
month = datetime.month(abbreviated=True)

# Get a random periodicity string.
# For example: Never
periodicity = datetime.periodicity()

# Generate a random date formatted as a d/m/Y
# For example: 11/05/2016
date = datetime.date(sep='/', with_time=True)

# Generate a random days of month, from 1 to 31.
# For example: 21
day_of_month = datetime.day_of_month()

```
## Network
```python
# Class for generate data for working with network,
network = Network()

# Generate IPv4 address
ip_v4 = network.ip_v4()

# Generate IPv6 address.
ip_v6 = network.ip_v6()

# Generate mac address.
mac = network.mac_address()

# Get a random user agent.
user_agent = network.user_agent()
```

## Science
```python
science = Science('en_us')

# Get a random mathematical formula.
# For example: A = (ab)/2
math_formula = science.math_formula()

# Get a random chemical element. If argument name_only=True
# then will be returned only Name, else dict with more information
# For example: {'Symbol': 'S',
#               'Name': 'Sulfur',
#               'Atomic number': '16'
#             }
# or name of chemical element: 'Helium'
chemical_e  = science.chemical_element()

# Get the wording of the law of physics.
physical_law = science.physical_law()

# Get a random link to scientific article on Wikipedia.
# For example: https://en.wikipedia.org/wiki/Black_hole
article = science.article_on_wiki()

# Get a random name of scientist.
# For example: Konstantin Tsiolkovsky
scientist = science.scientist()
```
## File

```python
file = File()

# Get a random file extension.
# All available file types:
# 1. source - '.py', '.rb', '.cpp' and other.
# 2. text = '.doc', '.log', '.rtf' and other.
# 3. data = '.csv', '.dat', '.pps' and other.
# 4. audio = '.mp3', '.flac', '.m4a' and other.
# 5. video = '.mp4', '.m4v', '.avi' and other.
# 6. image = '.jpeg', '.jpg', '.png' and other.
# 7. executable = '.exe', '.apk', '.bat' and other.
# 8. compressed = '.zip', '.7z', '.tar.xz' and other.
# For example: '.py'
extension = file.extension(file_type='source')

```

## Address
```python
address = Address('en_us')

# Generate a random street number.
street_number = address.street_number()

# Get a random street name.
street_name = address.street_name()

# Get a random street suffix.
# For example: Street.
street_suffix = address.street_suffix()

# Get a random address.
# 786 Clinton Lane
street_address = address.street_address()

# Get a random states or subject of country. For 'ru_ru' always will
# be getting subject of Russian Federation.
# For other localization will be getting state.
state = address.state_or_subject()

# Get real postal code.
# For example: 389213
postal_code = address.postal_code()

# Get a random country.
# For example: Russia or Ru if only_iso_code=True:
country = address.country()

# Get a random name of city
# For example: Saint Petersburg
city = address.city()
```

## Text
```python
data = Text('en_us')

# Get random text.
# quantity=5 is a quantity of sentence
text = data.lorem_ipsum(quantity=5)

# Get a random sentence.
sentence = data.sentence()

# Get a random title. Equal to sentence().
title = data.title()

# Get the random words.
# For example: human, rabbit, love, hope, tiger, cat, dog
words = data.words(quantity=7)

# Get a random word.
# For example: peach
word = data.word()

# Get a random swear word.
# For example: shit
bad = data.swear_word()

# Get a list of naughty strings (bad input)
# For example: $ENV{'HOME'}
naughty = data.naughty_strings()

# Get a random quotes from movie.
# For example: 'Bond...James Bond.'
quote = data.quote_from_movie()

# Get currency code. ISO 4217
# For example: USD
currency = data.currency_iso()

# Get random name of color.
# For example: White
color = data.company()

# Get a random company name.
# For example: AI Research Group.
company = data.company()

# Get a random company type.
# For example: Inc.
company_type = data.company_type()
```

## Development
```python
dev = Development()

# Get a random license from list.
software_license = Development.license()

# Get a random database name.
# For example: Riak or if nosql=False PostgreSQL
db = Development.database(nosql=True)

# Get a random value list.
# For example: Docker
other_skill = Development.other()

# Get a random programming language from list.
programming_language = Development.programming_language()

# Get a random framework from file.
# For example:  Python/Django
# or
# React/Redux if _type='front'
framework = Development.framework(_type='back')

# Get a random stack.
# {'front-end': 'Twitter Bootstrap',
# 'back-end': 'Python/Flask'
# 'other': 'Docker', 
# 'db': 'Couchbase', 
# }
stack = Development.stack_of_tech(nosql=True)

# Get a random link to github repository.
# For example: https://github.com/lk-geimfari/church
repo = Development.github_repo()
```

## Food

```python
food = Food('en_us')

# Get a random alcoholic drink.
# Example: Vodka
alco_drink = food.alcoholic_drink()

# Get a random berry.
# Example: Blackberry
berry = food.berry()

# Get a random cocktail.
# Example: Amber Moon
cocktail = food.cocktail()

# Get a random dish for current locale
# Example ('ru_ru'): Борщ 
dish = food.dish()

# Get a random fruit.
# Example: Apple
fruit = food.fruit()

# Get a random mushroom
# Example: Laetiporus sulphureus
mushroom = food.mushroom()

# Get a random herbs or spices.
# Example: Artemisia
spices_or_herbs = food.spices()

# Get a random vegetable.
# Example: Belgian Endive
vegetable = food.vegetable()
```

## Hardware

```python
hardware = Hardware()

# Get a random CPU name.
# Example: Intel® Core i3
cpu_name = hardware.cpu()

# Get a random CPU codename.
# Example: Bear Ridge
cpu_codename = hardware.cpu_codename()

# Get a random frequency of CPU.
# Example: 2.3 GHz
cpu_frequency = hardware.cpu_frequency()

# Get a random generation.
# Example: 2nd Generation
generation = hardware.generation()

# Get a random graphics.
# Example: Intel® HD Graphics 620
graphics = hardware.graphics()

# Get a random manufacturer
# Example: HP
manufacturer = hardware.manufacturer()

# Get a random size of RAM.
# Example: 32GB
ram_size = hardware.ram_size()

# Get a random type of RAM
# Example: DDR3
ram_type = hardware.ram_type()

# Get a random resolution of screen.
# Example: 1440x900
resolution_of_screen = hardware.resolution()

# Get a random size of screen (in inch).
# Example: 15.4″
screen_size = hardware.screen_size()

# Get a random information about drive
# Example: 1TB HDD(7200 RPM) + 32GB SSD
ssd_or_hdd = hardware.ssd_or_hdd()

# Generate a random information about hardware.
# Example:  Acer Intel® Core i7 2nd Generation 3.50 GHz/1920x1200/12″/
# 1TB HDD + 64GB SSD/DDR3-32GB/Intel® HD Graphics 5300  
hardware_full_info = hardware.hardware_full_info()

# Get a random model of phone.
# Example: Nokia Lumia 610
phone_model = hardware.phone_model()
```