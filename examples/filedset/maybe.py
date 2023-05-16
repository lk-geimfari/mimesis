from mimesis import Fieldset
from mimesis.keys import maybe
from mimesis.locales import Locale

fieldset = Fieldset(Locale.EN, i=5)

print(fieldset("email", key=maybe(None, probability=0.6)))
