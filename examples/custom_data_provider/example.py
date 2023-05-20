from pathlib import Path

from mimesis import BaseDataProvider
from mimesis.locales import Locale


class CustomDataProvider(BaseDataProvider):
    class Meta:
        # Name of provider, which will be used when
        # you add this provider to mimesis.Generic.
        name = "custom_provider"
        # Name of json file for this provider.
        datafile = "data.json"
        # Directory where json file for this provider is located.
        # Must an instance of pathlib.Path.
        datadir = Path(__file__).parent.joinpath("datadir")

    def my_method(self) -> str:
        return self.random.choice(self.extract(["key"]))


custom_en = CustomDataProvider(locale=Locale.EN)
print(custom_en.my_method())

custom_ru = CustomDataProvider(locale=Locale.RU)
print(custom_ru.my_method())

# This will raise an error, because there is no such subdirectory in datadir.
# custom_de = CustomDataProvider(locale=Locale.DE)
