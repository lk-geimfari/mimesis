# Test
import json

from church.utils import pull

structure = {
    "personal": {
        "names": {
            "male": [],
            "female": [],
        },
        "surnames": [],
        "gender": [],
        "views_on": [],
        "language": [],
        "nationality": [],
        "occupation": [],
        "worldview": [],
        "political_views": [],
        "academic_degree": [],
        "sexuality": [],
        "favorite_movie": [],
        "university": [],
    },
    "datetime": {
        "day": {
            "name": [],
            "abbr": []
        },
        "month": {
            "name": [],
            "abbr": []
        },
        "periodicity": [],

    },
    "address": {
        "city": [],
        "country": {
            "iso_code": [],
            "name": []
        },
        "street": {
            "name": [],
            "suffix": []
        },
        "state": {
            "name": [],
            "abbr": []
        }
    },
    "food": {
        "fruits": [],
        "vegetables": [],
        "dishes": [],
        "spices": [],
        "drinks": []
    },
    "text": {
        "text": [],
        "quotes": [],
        "color": [],
        "words": {
            "normal": [],
            "bad": []
        }
    },
    "business": {
        "company": {
            "name": [],
            "type": {
                "title": [],
                "abbr": []
            }

        }
    },
    "science": {
        "scientist": [],
        "article": [],
        "chemical_elements": []
    },
}


LANG = 'da'

# with open('data.json', 'r') as j:
#     structure = json.load(j)

che_data = pull('ch_el', LANG)
for i in che_data:
    structure['science']['chemical_elements'].append(i.strip())

data = pull('cities', LANG)
for i in data:
    structure['address']['city'].append(i.strip())

data = pull('colors', LANG)
for i in data:
    structure['text']['color'].append(i.strip())

data = pull('company', LANG)
for i in data:
    structure['business']['company']['name'].append(i.strip())

data = pull('company_type', LANG)
for i in data:
    st = i.split('|')
    title, abbr = st[0], st[1]
    structure['business']['company']['type']['title'].append(title.strip())
    structure['business']['company']['type']['abbr'].append(abbr.strip())

data = pull('countries', LANG)
for i in data:
    st = i.split('|')
    name, iso = st[1], st[0]
    structure['address']['country']['name'].append(name.strip())
    structure['address']['country']['iso_code'].append(iso.strip())

data = pull('days', LANG)
for i in data:
    st = i.split('|')
    name, abbr = st[0], st[1]
    structure['datetime']['day']['abbr'].append(abbr.strip())
    structure['datetime']['day']['name'].append(name.strip())

data = pull('dishes', LANG)
for i in data:
    structure['food']['dishes'].append(i.strip())

data = pull('drinks', LANG)
for i in data:
    structure['food']['drinks'].append(i.strip())

data = pull('f_names', LANG)
for i in data:
    structure['personal']['names']['female'].append(i.strip())

data = pull('m_names', LANG)
for i in data:
    structure['personal']['names']['male'].append(i.strip())

data = pull('fruits_berries', LANG)
for i in data:
    structure['food']['fruits'].append(i.strip())

data = pull('gender', LANG)
for i in data:
    structure['personal']['gender'].append(i.strip())

data = pull('languages', LANG)
for i in data:
    structure['personal']['language'].append(i.strip())

data = pull('months', LANG)
for i in data:
    st = i.split('|')
    name, abbr = st[0], st[1]
    structure['datetime']['month']['abbr'].append(abbr.strip())
    structure['datetime']['month']['name'].append(name.strip())

data = pull('languages', LANG)
for i in data:
    structure['personal']['language'].append(i.strip())

data = pull('movies', LANG)
for i in data:
    structure['personal']['favorite_movie'].append(i.strip())

data = pull('nation', LANG)
for i in data:
    structure['personal']['nationality'].append(i.strip())

data = pull('periodicity', LANG)
for i in data:
    structure['datetime']['periodicity'].append(i.strip())

data = pull('political_views', LANG)
for i in data:
    structure['personal']['political_views'].append(i.strip())

data = pull('professions', LANG)
for i in data:
    structure['personal']['occupation'].append(i.strip())

data = pull('qualifications', LANG)
for i in data:
    structure['personal']['academic_degree'].append(i.strip())

data = pull('professions', LANG)
for i in data:
    structure['personal']['occupation'].append(i.strip())

data = pull('quotes', LANG)
for i in data:
    structure['text']['quotes'].append(i.strip())

data = pull('science_wiki', LANG)
for i in data:
    structure['science']['article'].append(i.strip())

data = pull('science_wiki', LANG)
for i in data:
    structure['science']['article'].append(i.strip())

data = pull('scientist', LANG)
for i in data:
    structure['science']['scientist'].append(i.strip())

data = pull('sexuality', LANG)
for i in data:
    structure['personal']['sexuality'].append(i.strip())

data = pull('spices', LANG)
for i in data:
    structure['food']['spices'].append(i.strip())

data = pull('spices', LANG)
for i in data:
    structure['food']['spices'].append(i.strip())

data = pull('streets', LANG)
for i in data:
    structure['address']['street']['name'].append(i.strip())

data = pull('st_suffix', LANG)
for i in data:
    structure['address']['street']['suffix'].append(i.strip())

data = pull('states', LANG)
for i in data:
    structure['address']['state']['name'].append(i.strip())

structure['address']['state']['abbr'].append("Test")

data = pull('surnames', LANG)
for i in data:
    structure['personal']['surnames'].append(i.strip())

data = pull('swear_words', LANG)
for i in data:
    structure['text']['words']['bad'].append(i.strip())

data = pull('text', LANG)
for i in data:
    structure['text']['text'].append(i.strip())

data = pull('university', LANG)
for i in data:
    structure['personal']['university'].append(i.strip())

data = pull('vegetables', LANG)
for i in data:
    structure['food']['vegetables'].append(i.strip())

data = pull('views_on', LANG)
for i in data:
    structure['personal']['views_on'].append(i.strip())

data = pull('words', LANG)
for i in data:
    structure['text']['words']['normal'].append(i.strip())

data = pull('worldview', LANG)
for i in data:
    structure['personal']['worldview'].append(i.strip())

with open('data.json', 'w') as j:
    structure = json.dump(structure, j)
