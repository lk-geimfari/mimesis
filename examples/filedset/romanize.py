from mimesis.keys import romanize
from mimesis.locales import Locale
from mimesis.schema import Field, Fieldset

fieldset = Fieldset(Locale.RU, i=5)
fieldset("name", key=romanize(Locale.RU))

field = Field(locale=Locale.UK)
field("full_name", key=romanize(Locale.UK))
