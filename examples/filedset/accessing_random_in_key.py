from mimesis import Field
from mimesis.locales import Locale

field = Field(Locale.EN, seed=42)

key_fb = lambda r, rnd: rnd.choice(["foo", "bar"]) + r

field("email", key=key_fb)
# Output: "bazany1925@gmail.com"

field = Field(Locale.EN, seed=42)

field("email", key=key_fb)
# Output: "bazany1925@gmail.com"
