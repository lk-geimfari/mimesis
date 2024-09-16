.. _locale:

Locales
=======

The Mimesis supports multiple locales. This means that you can generate
data in different languages and for different countries.

The default locale for all providers is English (United States) (``Locale.EN``).

You have to import :class:`~mimesis.enums.Locale` object first, like this:

.. code-block:: python

    from mimesis.locales import Locale

Now you can specify a locale when creating providers and they will return data that
is appropriate for the language or country associated with that locale:

.. code-block:: python

    from mimesis import Address
    from mimesis.locales import Locale

    de = Address(locale=Locale.DE)
    ru = Address(locale=Locale.RU)

    de.region()
    # Output: 'Brandenburg'

    ru.federal_subject()
    # Output: 'Алтайский край'

    de.address()
    # Output: 'Mainzer Landstraße 912'

    ru.address()
    # Output: 'ул. Пехотная 125'

See the table below for more details.

Overriding locale
-----------------

Sometimes you need only some data from other locale and creating an instance for such cases
is not really good,  so it's better just temporarily override current locale for provider's instance:

.. code-block:: python

    from mimesis import Person
    from mimesis.locales import Locale

    person = Person(locale=Locale.EN)
    person.full_name()
    # Output: 'Ozie Melton'

    with person.override_locale(Locale.RU):
        person.full_name()

    # Output: 'Симона Богданова'

    person.full_name()
    # Output: 'Waldo Foster'

You can also use it with :class:`~mimesis.Generic()`:

.. code-block:: python

    from mimesis import Generic
    from mimesis.locales import Locale

    generic = Generic(locale=Locale.EN)
    generic.text.word()
    # Output: 'anyone'

    with generic.text.override_locale(Locale.FR):
        generic.text.word()

    # Output: 'mieux'

    generic.text.word()
    # Output: 'responsibilities'

Supported locales
-----------------

Mimesis currently includes support for 42 different locales (see :class:`~mimesis.enums.Locale` for more details).

The table below lists all supported locales and their associated
countries.

=======  =======  ====================  ====================  ====================
Country   Code    Associated attribute  Name                  Native Name
=======  =======  ====================  ====================  ====================
   🇦🇪    `ar-ae`  **Locale.AR_AE**      Arabic U.A.E          العربية
   🇩🇿    `ar-dz`  **Locale.AR_DZ**      Arabic Algeria        العربية
   🇪🇬    `ar-eg`  **Locale.AR_EG**      Arabic Egypt          العربية
   🇯🇴    `ar-jo`  **Locale.AR_JO**      Arabic Jordan         العربية
   🇴🇲    `ar-om`  **Locale.AR_OM**      Arabic Oman           العربية
   🇲🇦    `ar-ma`  **Locale.AR_MA**      Arabic Morocco        العربية
   🇸🇾    `ar-sy`  **Locale.AR_SY**      Arabic Syria          العربية
   🇹🇳    `ar-tn`  **Locale.AR_TN**      Arabic Tunisia        العربية
   🇾🇪    `ar-ye`  **Locale.AR_YE**      Arabic Yemen          العربية
   🇨🇿    `cs`     **Locale.CS**         Czech                 Česky
   🇩🇰    `da`     **Locale.DA**         Danish                Dansk
   🇩🇪    `de`     **Locale.DE**         German                Deutsch
   🇦🇹    `de-at`  **Locale.DE_AT**      Austrian German       Deutsch
   🇨🇭    `de-ch`  **Locale.DE_CH**      Swiss German          Deutsch
   🇬🇷	 `el`	  **Locale.EL**         Greek                 Ελληνικά
   🇺🇸    `en`     **Locale.EN**         English               English
   🇦🇺    `en-au`  **Locale.EN_AU**      Australian English    English
   🇨🇦    `en-ca`  **LocALE.EN_CA**      Canadian English      English
   🇬🇧    `en-gb`  **Locale.EN_GB**      British English       English
   🇪🇸    `es`     **Locale.ES**         Spanish               Español
   🇲🇽    `es-mx`  **Locale.ES_MX**      Mexican Spanish       Español
   🇪🇪    `et`     **Locale.ET**         Estonian              Eesti
   🇮🇷    `fa`     **Locale.FA**         Farsi                 فارسی
   🇫🇮    `fi`     **Locale.FI**         Finnish               Suomi
   🇫🇷    `fr`     **Locale.FR**         French                Français
   🇭🇷    `hr`     **Locale.HR**         Croatian              Hrvatski
   🇭🇺    `hu`     **Locale.HU**         Hungarian             Magyar
   🇮🇸    `is`     **Locale.IS**         Icelandic             Íslenska
   🇮🇹    `it`     **Locale.IT**         Italian               Italiano
   🇯🇵    `ja`     **Locale.JA**         Japanese              日本語
   🇰🇿    `kk`     **Locale.KK**         Kazakh                Қазақша
   🇰🇷	 `ko`	  **Locale.KO**         Korean                한국어
   🇳🇱    `nl`     **Locale.NL**         Dutch                 Nederlands
   🇧🇪    `nl-be`  **Locale.NL_BE**      Belgium Dutch         Nederlands
   🇳🇴    `no`     **Locale.NO**         Norwegian             Norsk
   🇵🇱    `pl`     **Locale.PL**         Polish                Polski
   🇵🇹    `pt`     **Locale.PT**         Portuguese            Português
   🇧🇷    `pt-br`  **Locale.PT_BR**      Brazilian Portuguese  Português Brasileiro
   🇷🇺    `ru`     **Locale.RU**         Russian               Русский
   🇸🇰    `sk`     **Locale.SK**         Slovak                Slovensky
   🇸🇪    `sv`     **Locale.SV**         Swedish               Svenska
   🇹🇷    `tr`     **Locale.TR**         Turkish               Türkçe
   🇺🇦    `uk`     **Locale.UK**         Ukrainian             Українська
   🇨🇳    `zh`     **Locale.ZH**         Chinese               汉语
=======  =======  ====================  ====================  ====================
