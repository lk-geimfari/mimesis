import pandas as pd

from mimesis.locales import Locale
from mimesis.schema import Fieldset

fs = Fieldset(locale=Locale.EN, i=5)

df = pd.DataFrame.from_dict(
    {
        "ID": fs("increment"),
        "Name": fs("person.full_name"),
        "Email": fs("email"),
        "Phone": fs("telephone", mask="+1 (###) #5#-7#9#"),
    }
)

print(df)
