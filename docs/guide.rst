===========
Quick Start
===========

Personal
--------

.. code-block:: python

	from elizabeth import Personal

	person = Personal('en')

	# Get a random integer value from range.
	# Output: 21
	age = person.age(mi=17, mx=35)


	# Get a random name.
	# Output: Christina
	name = person.name(gender='female')

	# Get a random surname.
	# Output: Wolf
	surname = person.surname()

	# Get a random full name.
	# Output: Leo Johnson.
	full_name = person.full_name(gender='male')

	# Get a random username.
	# Output: john1032
	username = person.username()

	# Get a random title (prefix/suffix) for name/surname.
	# Available types: typical, aristocratic, religious, academic
	# Output: PhD.
	title = person.title(gender='female', type_='academic')

	# Generate a random password.
	password = person.password(length=15)

	# Generate a random email using usernames.
	# Output: foretime10@live.com
	email = person.email()

	# Generate a random home page using usernames.
	# Output: http://www.font6.info
	home_page = person.home_page()

	# Get a random subreddit thread from list.
	# If nsfw=True then will be returned NSFW subreddit
	# Output: /r/games
	subreddit = p.subreddit(nsfw=False, full_url=False)

	# Get a bitcoin address.
	# Output:
	bitcoin = person.bitcoin()

	# Generate a random card verification value (CVV)
	# Output: 731
	cvv = person.cvv()

	# Generate a random CID code.
	# Output: 7834
	cid = person.cid()

	# Generate a random credit card number (Visa or MasterCard)
	# Output: 4001 2073 7960 3241
	credit_card = person.credit_card_number(card_type='visa')

	# Get a random gender.
	# Output: Male
	gender = person.gender()
	# Output:  ♂
	gender_symbol = person.gender(symbol=True)

	# Get a random occupation.
	# Output: Programmer
	occupation = person.occupation()

	# Get a random political views.
	# Output: Liberal
	political_views = person.political_views()

	# Get a random worldview
	# Output: Naturalistic Pantheism
	worldview = person.worldview()

	# Get a random views on.
	# Output: Negative
	views_on = person.views_on()

	# Get a random nationality.
	# Output: Russian
	nationality = person.nationality()

	# Get a random university.
	# Output: MIT
	university = person.university()

	# Get a random academic degree.
	# Output: Master
	ad = person.academic_degree()

	# Get a random language.
	# Output: Russian
	language = person.language()

	# Get a random movie.
	# Output: Pulp Fiction
	favorite_movie = person.favorite_movie()

	# Generate a random phone number.
	# Output: +7-(963)409-11-22
	telephone = person.telephone()
	# You're also can use mask
	mask = +1-### ### ## ##
	# Output: +1-763 001 13 22
	telephone = person.telephone(mask)

	# Generate identifier by mask
	# Output: 8492-436-03/11
	id = person.identifier(mask="####-###-##/##")


Datetime
--------

.. code-block:: python

	datetime = Datetime('en')

	# Get a random day of week.
	# Output: Sun.
	day_of_week = datetime.day_of_week(abbr=True)

	# Get a random month.
	# Output:  Dec.
	month = datetime.month(abbr=True)

	# Get a random periodicity string.
	# Output: Never
	periodicity = datetime.periodicity()

	# Generate a random date formatted for the locale
	# Output: 11/05/2016
	date = datetime.date()

	# Specify a custom date format and a range in years
	# Output: 2008-08-21
	date = datetime.date(start=2000, end=2010, fmt="%y-%m-%d")

	# Generate a random days of month, from 1 to 31.
	# Output: 21
	day_of_month = datetime.day_of_month()

	# Generate a random time formatted for the locale
	# Output: 22:00:50
	time = datetime.time()

	# Specify a custom time format
	# Output: 22:00
	date = datetime.time(fmt="%H:%M")

Business
--------

.. code-block:: python

	business = Business('en')

	# Get a random company type
	# abbr=True is abbreviated company type
	# Output: Incorporated (Inc. when abbr=True)
	company_type = business.company_type(abbr=False)

	# Get a random company name
	# Output: Gamma Systems
	company = business.company()

	# Generate a random copyright
	# mi=1990 is foundation date
	# mx=2016 is current date
	# without_date=True returns copyright without date
	# Output: © 1990-2016 Komercia, Inc
	copyright = business.copyright(mi=1990, mx=2016, without_date=False)

	# Get a currency code. ISO 4217 format
	#  Output: RUR
	currency = business.currency()

Network
-------

.. code-block:: python

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

Science
-------

.. code-block:: python

	science = Science('en')

	# Get a random mathematical formula.
	# Output: A = (ab)/2
	math_formula = science.math_formula()

	# Get a random chemical element. If argument name_only=True
	# then will be returned only Name, else dict with more information
	# Output: {'Symbol': 'S',
	#               'Name': 'Sulfur',
	#               'Atomic number': '16'
	#             }
	# or name of chemical element: 'Helium'
	chemical_e  = science.chemical_element()

	# Get the wording of the law of physics.
	physical_law = science.physical_law()

	# Get a random link to scientific article on Wikipedia.
	# Output: https://en.wikipedia.org/wiki/Black_hole
	article = science.article_on_wiki()

	# Get a random name of scientist.
	# Output: Konstantin Tsiolkovsky
	scientist = science.scientist()

File
----

.. code-block:: python

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
	# Output: '.py'
	extension = file.extension(file_type='source')

Address
-------

.. code-block:: python

	address = Address('en')

	# Generate a random street number.
	street_number = address.street_number()

	# Get a random street name.
	street_name = address.street_name()

	# Get a random street suffix.
	# Output: Street.
	street_suffix = address.street_suffix()

	# Get a random address.
	# 786 Clinton Lane
	street_address = address.address()

	# Get a random name of state
	# Output: Alabama (for locale 'en')
	state = address.state()

	# Get real postal code.
	# Output: 389213
	postal_code = address.postal_code()

	# Get a random country.
	# Output: RussiaSpecProvider or Ru if only_iso_code=True:
	country = address.country()

	# Get a random name of city
	# Output: Saint Petersburg
	city = address.city()

	# Get a random value of latitude (+90 to -90)
	# Output: -66.4214188124611
	latitude = address.latitude()

	# Get a random value of longitude (-180 to +180)
	# Output: 112.18440260511943
	longitude = address.longitude()

	# Get random geo coordinates
	# Output: {'latitude': 8.003968712834975, 'longitude': 36.02811153405548}
	coordinates = address.coordinates()

Numbers
-------

.. code-block:: python

	number = Numbers()

	# Get an array of random float number of 10**n
	# n=2 is raise 10 to the 'n' power
	# type_code='f' is a code of type('f'/'d')
	# to_list=True is to convert array to list
	floats = number.floats(n=2, type_code='f', to_list=True)

	# Get an array of prime numbers of 10**n
	# n=2 is raise 10 to the 'n' power
	# to_list=True is to convert array to list
	primes = number.primes(n=2, to_list=True)

Text
----

.. code-block:: python

	data = Text('en')

	# Get random text.
	# quantity=5 is a quantity of sentence
	text = data.text(quantity=5)

	# Get a random sentence.
	sentence = data.sentence()

	# Get a random title. Equal to sentence().
	title = data.title()

	# Get the random words.
	# Output: human, rabbit, love, hope, tiger, cat, dog
	words = data.words(quantity=7)

	# Get a random word.
	# Output: peach
	word = data.word()

	# Get a random swear word.
	# Output: shit
	bad = data.swear_word()

	# Get a list of naughty strings (bad input)
	# Output: $ENV{'HOME'}
	naughty = data.naughty_strings()

	# Get a random quote.
	# Output: 'Bond...James Bond.'
	quote = data.quote()

	# Get random name of color.
	# Output: White
	color = data.color()

Development
-----------

.. code-block:: python

	dev = Development()

	# Get a random license from list.
	software_license = Development.license()

	# Get a random database name.
	# Output: Riak or if nosql=False PostgreSQL
	db = Development.database(nosql=True)

	# Get a random value list.
	# Output: Docker
	other_skill = Development.other()

	# Get a random programming language from list.
	programming_language = Development.programming_language()

	# Get a random framework from file.
	# Output:  Python/Django
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
	# Output: https://github.com/lk-geimfari/elizabeth
	repo = Development.github_repo()

Food
----

.. code-block:: python

	food = Food('en')

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

Hardware
--------

.. code-block:: python

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


Path
----

.. code-block:: python

	from elizabeth import Path

	path = Path()

	root = path.root
	# Output: /

    home = path.home
	# Output: /home/

    user = path.user(gender='female')
	# Output: /home/mariko

    user_folder = path.users_folder(user_gender='male')
	# Output: /home/john/Documents

    dev = path.dev_dir()
	# Output: /home/fidelia/Development/Erlang

	project_dir = path.project_dir(user_gender='female')
	# Output:  /home/sherika/Development/Elixir/mercenary
