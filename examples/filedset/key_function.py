from mimesis import Field, Fieldset
from mimesis.locales import Locale

field = Field(Locale.EN)
fieldset = Fieldset(Locale.EN, i=3)

print(field("name", key=str.upper))

print(fieldset("name", key=str.upper))
