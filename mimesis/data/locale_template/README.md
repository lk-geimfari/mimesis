## How to add new locale

This is a template of the locale structure. There are eight json
files (`File name`) which include data related to some data providers (`Provider`):

```
.----------------------------.
| File name        Provider  |
.----------------------------.
├── address.json   # Address()
├── builtin.json   # YourSpecProvider()
├── business.json  # Business()
├── datetime.json  # Datetime()
├── food.json      # Food()
├── person.json    # Person()
├── science.json   # Science()
└── text.json      # Text()
```

Almost all locales have a similar structure, but the structure of the locale file may differ when there are any builtins specific data providers for this locale.
For example, locale `ru` has a different structure of `person.json`, because in Russia there are mandatory patronymic names.
So, it is useful for this locale only (and a couple of other).
It means that if someone wants to use patronymic names then he must import builtin specific provider:

````python
>>> from mimesis.builtins import RussiaSpecProvider
>>> ru = RussiaSpecProvider()
>>> ru.patronymic()
'Васильевна'
````

Only if your locale uses any specific fields it could be added into json files otherwise, it is not permitted to modify the structure.
You should not modify the provider object directly if the data which you add is not common for all locales.

If you want to create `YourCountrySpecProvider()`, then you should add all related data to the file `locale/builtin.json`.

## Sub-locale
If your language is common for a lot of countries then you must inherit common data from the generic locale.

For example, English (`en`) is the official language in a lot of countries and if we want to add support
for New Zealand (`en-nz`) then you need specify only the data which is specific to this country.
All the generic data will be automatically inherited from `en`.

Before Pull Request:

- Rename folder `locale_template` to `your-locale-code`.
- Make sure that you have replaced all `["Tests""]` sections with data for your locale.
- Make sure that you have **removed** all `"__COMMENT_KEY__": "Description"` from json files. This data only for developers.
- Add your locale to `SUPPORTED_LOCALES` in `mimesis/locales.py`.
- Format the content of json files alphabetically using [jsoneditoronline.org](http://jsoneditoronline.org)
- If your locale uses shortened address format, then add your locale code to `SHORTENED_ADDRESS_FMT` in `mimesis/data/int/address.py`
- Make sure that you have added currency symbol for your locale to `CURRENCY_SYMBOLS` in `mimesis/data/int/business.py`
- Make sure that you have added your locale code to `ISBN_GROUPS` in  `mimesis/data/int/code.py`
- Run tests and make sure that all tests pass
- Add yourself to (`CONTRIBUTORS.md`)


#### You can grab code of your locale from the table below:


<table class="clsStd" summary="table">
<tbody><tr><td>af</td><td>Afrikaans </td><td>sq</td><td>Albanian </td></tr>
<tr><td>ar-sa</td><td>Arabic (Saudi Arabia) </td><td>ar-iq</td><td>Arabic (Iraq) </td></tr>
<tr><td>ar-eg</td><td>Arabic (Egypt) </td><td>ar-ly</td><td>Arabic (Libya) </td></tr>
<tr><td>ar-dz</td><td>Arabic (Algeria) </td><td>ar-ma</td><td>Arabic (Morocco) </td></tr>
<tr><td>ar-tn</td><td>Arabic (Tunisia) </td><td>ar-om</td><td>Arabic (Oman) </td></tr>
<tr><td>ar-ye</td><td>Arabic (Yemen) </td><td>ar-sy</td><td>Arabic (Syria) </td></tr>
<tr><td>ar-jo</td><td>Arabic (Jordan) </td><td>ar-lb</td><td>Arabic (Lebanon) </td></tr>
<tr><td>ar-kw</td><td>Arabic (Kuwait) </td><td>ar-ae</td><td>Arabic (U.A.E.) </td></tr>
<tr><td>ar-bh</td><td>Arabic (Bahrain) </td><td>ar-qa</td><td>Arabic (Qatar) </td></tr>
<tr><td>eu</td><td>Basque (Basque)</td><td>bg</td><td>Bulgarian </td></tr>
<tr><td>be</td><td>Belarusian </td><td>ca</td><td>Catalan </td></tr>
<tr><td>zh-tw</td><td>Chinese (Taiwan) </td><td>zh-cn</td><td>Chinese (PRC) </td></tr>
<tr><td>zh-hk</td><td>Chinese (Hong Kong SAR) </td><td>zh-sg</td><td>Chinese (Singapore) </td></tr>
<tr><td>hr</td><td>Croatian </td><td>cs</td><td>Czech </td></tr>
<tr><td>da</td><td>Danish </td><td>nl</td><td>Dutch (Standard) </td></tr>
<tr><td>nl-be</td><td>Dutch (Belgium) </td><td>en</td><td>English </td></tr>
<tr><td>en-us</td><td>English (United States) </td><td>en-gb</td><td>English (United Kingdom) </td></tr>
<tr><td>en-au</td><td>English (Australia) </td><td>en-ca</td><td>English (Canada) </td></tr>
<tr><td>en-nz</td><td>English (New Zealand) </td><td>en-ie</td><td>English (Ireland) </td></tr>
<tr><td>en-za</td><td>English (South Africa) </td><td>en-jm</td><td>English (Jamaica) </td></tr>
<tr><td>en</td><td>English (Caribbean) </td><td>en-bz</td><td>English (Belize) </td></tr>
<tr><td>en-tt</td><td>English (Trinidad) </td><td>et</td><td>Estonian </td></tr>
<tr><td>fo</td><td>Faeroese </td><td>fa</td><td>Farsi </td></tr>
<tr><td>fi</td><td>Finnish </td><td>fr</td><td>French (Standard) </td></tr>
<tr><td>fr-be</td><td>French (Belgium) </td><td>fr-ca</td><td>French (Canada) </td></tr>
<tr><td>fr-ch</td><td>French (Switzerland) </td><td>fr-lu</td><td>French (Luxembourg) </td></tr>
<tr><td>gd</td><td>Gaelic (Scotland) </td><td>ga</td><td>Irish </td></tr>
<tr><td>de</td><td>German (Standard) </td><td>de-ch</td><td>German (Switzerland) </td></tr>
<tr><td>de-at</td><td>German (Austria) </td><td>de-lu</td><td>German (Luxembourg) </td></tr>
<tr><td>de-li</td><td>German (Liechtenstein) </td><td>el</td><td>Greek </td></tr>
<tr><td>he</td><td>Hebrew </td><td>hi</td><td>Hindi </td></tr>
<tr><td>hu</td><td>Hungarian </td><td>is</td><td>Icelandic </td></tr>
<tr><td>id</td><td>Indonesian </td><td>it</td><td>Italian (Standard) </td></tr>
<tr><td>it-ch</td><td>Italian (Switzerland) </td><td>ja</td><td>Japanese </td></tr>
<tr><td>ko</td><td>Korean </td><td>ko</td><td>Korean (Johab) </td></tr>
<tr><td>lv</td><td>Latvian </td><td>lt</td><td>Lithuanian </td></tr>
<tr><td>mk</td><td>Macedonian (FYROM)</td><td>ms</td><td>Malaysian </td></tr>
<tr><td>mt</td><td>Maltese </td><td>no</td><td>Norwegian (Bokmal) </td></tr>
<tr><td>no</td><td>Norwegian (Nynorsk) </td><td>pl</td><td>Polish </td></tr>
<tr><td>pt-br</td><td>Portuguese (Brazil) </td><td>pt</td><td>Portuguese (Portugal) </td></tr>
<tr><td>rm</td><td>Rhaeto-Romanic </td><td>ro</td><td>Romanian </td></tr>
<tr><td>ro-mo</td><td>Romanian (Republic of Moldova) </td><td>ru</td><td>Russian </td></tr>
<tr><td>ru-mo</td><td>Russian (Republic of Moldova) </td><td>sz</td><td>Sami (Lappish) </td></tr>
<tr><td>sr</td><td>Serbian (Cyrillic) </td><td>sr</td><td>Serbian (Latin) </td></tr>
<tr><td>sk</td><td>Slovak </td><td>sl</td><td>Slovenian </td></tr>
<tr><td>sb</td><td>Sorbian </td><td>es</td><td>Spanish (Spain) </td></tr>
<tr><td>es-mx</td><td>Spanish (Mexico) </td><td>es-gt</td><td>Spanish (Guatemala) </td></tr>
<tr><td>es-cr</td><td>Spanish (Costa Rica) </td><td>es-pa</td><td>Spanish (Panama) </td></tr>
<tr><td>es-do</td><td>Spanish (Dominican Republic) </td><td>es-ve</td><td>Spanish (Venezuela) </td></tr>
<tr><td>es-co</td><td>Spanish (Colombia) </td><td>es-pe</td><td>Spanish (Peru) </td></tr>
<tr><td>es-ar</td><td>Spanish (Argentina) </td><td>es-ec</td><td>Spanish (Ecuador) </td></tr>
<tr><td>es-cl</td><td>Spanish (Chile) </td><td>es-uy</td><td>Spanish (Uruguay) </td></tr>
<tr><td>es-py</td><td>Spanish (Paraguay) </td><td>es-bo</td><td>Spanish (Bolivia) </td></tr>
<tr><td>es-sv</td><td>Spanish (El Salvador) </td><td>es-hn</td><td>Spanish (Honduras) </td></tr>
<tr><td>es-ni</td><td>Spanish (Nicaragua) </td><td>es-pr</td><td>Spanish (Puerto Rico) </td></tr>
<tr><td>sx</td><td>Sutu </td><td>sv</td><td>Swedish </td></tr>
<tr><td>sv-fi</td><td>Swedish (Finland) </td><td>th</td><td>Thai </td></tr>
<tr><td>ts</td><td>Tsonga </td><td>tn</td><td>Tswana </td></tr>
<tr><td>tr</td><td>Turkish </td><td>uk</td><td>Ukrainian </td></tr>
<tr><td>ur</td><td>Urdu </td><td>ve</td><td>Venda </td></tr>
<tr><td>vi</td><td>Vietnamese </td><td>xh</td><td>Xhosa </td></tr>
<tr><td>ji</td><td>Yiddish </td><td>zu</td><td>Zulu </td></tr>
</tbody></table>

