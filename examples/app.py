import json

from church.utils import jull

data = jull('da')

# address, business, datetime, food, personal, science, text
address = data['address']
with open('address.json', 'w') as f:
    json.dump(address, f)

business = data['business']
with open('business.json', 'w') as f:
    json.dump(business, f)

datetime = data['datetime']
with open('datetime.json', 'w') as f:
    json.dump(datetime, f)

food = data['food']
with open('food.json', 'w') as f:
    json.dump(food, f)

personal = data['personal']
with open('personal.json', 'w') as f:
    json.dump(personal, f)

science = data['science']
with open('science.json', 'w') as f:
    json.dump(science, f)

text = data['text']
with open('text.json', 'w') as f:
    json.dump(text, f)
