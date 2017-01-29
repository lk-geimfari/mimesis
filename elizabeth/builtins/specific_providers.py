from random import randint, choice

from elizabeth.core import Code
from elizabeth.exceptions import JSONKeyError
from elizabeth.utils import pull

# TODO: Rename provider to *SpecificProvider, where * is locale code.
__all__ = [
    'USASpecProvider',
    'BrazilSpecProvider',
    'RussiaSpecProvider',
    'JapanSpecProvider'
]

# Internal
_custom_code = Code.custom_code


class BrazilSpecProvider(object):
    """Class that provides special data for pt-br"""

    class Meta:
        name = 'brazil_provider'

    @staticmethod
    def cpf(with_mask=True):
        """
        Get a random CPF (brazilian social security code)

        :param with_mask: use CPF mask (###.###.###-##) in the return
        :returns: Random CPF
        :Example:
            001.137.297-40
        """

        def get_verifying_digit_cpf(cpf, peso):
            """
            Calculates the verifying digit for the CPF

            :param cpf: ist of integers with the CPF
            :param peso: Integer with the weight for the modulo 11 calculate
            :returns: the verifying digit for the CPF
            """
            soma = 0
            for index, digit in enumerate(cpf):
                soma += digit * (peso - index)
            resto = soma % 11
            if resto == 0 or resto == 1 or resto >= 11:
                return 0
            return 11 - resto

        cpf_without_dv = [randint(0, 9) for _ in range(9)]
        first_dv = get_verifying_digit_cpf(cpf_without_dv, 10)

        cpf_without_dv.append(first_dv)
        second_dv = get_verifying_digit_cpf(cpf_without_dv, 11)
        cpf_without_dv.append(second_dv)

        cpf = ''.join([str(i) for i in cpf_without_dv])

        if with_mask:
            return cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
        return cpf

    @staticmethod
    def cnpj(with_mask=True):
        """
        Get a random cnpj (brazilian social security code)

        :param with_mask: use cnpj mask (###.###.###-##) in the return
        :returns: Random cnpj
        :Example:
            77.732.230/0001-70
        """

        def get_verifying_digit_cnpj(cnpj, peso):
            """
            Calculates the verifying digit for the cnpj
            :param cnpj: list of integers with the cnpj
            :param peso: integer with the weigth for the modulo 11 calcule
            :returns: the verifying digit for the cnpj
            """
            soma = 0
            if peso == 5:
                peso_list = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
            elif peso == 6:
                peso_list = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
            for i, _ in enumerate(cnpj):
                soma += peso_list[i] * cnpj[i]
            resto = soma % 11
            if resto < 2:
                return 0
            return 11 - resto

        cnpj_without_dv = [randint(0, 9) for _ in range(12)]

        first_dv = get_verifying_digit_cnpj(cnpj_without_dv, 5)
        cnpj_without_dv.append(first_dv)

        second_dv = get_verifying_digit_cnpj(cnpj_without_dv, 6)
        cnpj_without_dv.append(second_dv)

        cnpj = ''.join([str(i) for i in cnpj_without_dv])

        if with_mask:
            return cnpj[:2] + '.' + cnpj[2:5] + '.' + cnpj[5:8] + '/' + \
                   cnpj[8:12] + '-' + cnpj[12:]
        return cnpj


class USASpecProvider(object):
    """Class that provides special data for en"""

    class Meta:
        name = 'usa_provider'

    @staticmethod
    def tracking_number(service='usps'):
        """
        Generate random tracking number for USPS, FedEx and UPS.
        :param service:
        :return:
        """
        service = service.lower()

        if service not in ('usps', 'fedex', 'ups'):
            raise ValueError('Unsupported post service')

        services = {
            'usps': (
                '#### #### #### #### ####',
                '@@ ### ### ### US'
            ),
            'fedex': (
                "#### #### ####",
                "#### #### #### ###"
            ),
            'ups': ("1Z@####@##########",)
        }
        mask = choice(services[service])
        return _custom_code(mask=mask)

    @staticmethod
    def ssn():
        """
        Generate a random, but valid Social Security Number.

        :returns: Random SSN
        :Example:
            569-66-5801
        """
        # Valid SSNs exclude 000, 666, and 900-999 in the area group
        area = randint(1, 899)
        if area == 666:
            area = 665

        return '{:03}-{:02}-{:04}'.format(
            area, randint(1, 99), randint(1, 9999))

    @staticmethod
    def personality(category='mbti'):
        """
        Generate a type of personality.

        :param category: Category.
        :return: Personality type.
        :Example:
            ISFJ.
        """
        mbtis = ("ISFJ", "ISTJ", "INFJ", "INTJ",
                 "ISTP", "ISFP", "INFP", "INTP",
                 "ESTP", "ESFP", "ENFP", "ENTP",
                 "ESTJ", "ESFJ", "ENFJ", "ENTJ")

        if category.lower() == 'rheti':
            return randint(1, 10)

        return choice(mbtis)


class RussiaSpecProvider(object):
    """Specific data for russian language (ru)"""

    class Meta:
        name = 'russia_provider'

    @staticmethod
    def patronymic(gender='female'):
        """
        Generate random patronymic name.

        :param gender: Gender of person.
        :return: Patronymic name.
        :Example:
            Алексеевна.
        """
        gender = gender.lower()

        try:
            patronymic = pull('personal.json', 'ru')['patronymic']
            return choice(patronymic[gender])
        except:
            raise JSONKeyError(
                'Not exist key. Please use one of ["female", "male"]')

    @staticmethod
    def passport_series(year=None):
        """
        Generate random series of passport.

        :param year: Year of manufacture.
        :return: Series.
        :Example:
            02 15.
        """
        year = randint(10, 16) if not \
            year else year

        region = randint(1, 99)
        return '{:02d} {}'.format(region, year)

    @staticmethod
    def passport_number():
        """
        Generate random passport number.

        :return: Number.
        :Example:
            560430
        """
        return _custom_code(mask='######')

    def series_and_number(self):
        """
        Generate a random passport number and series.

        :return: Series and number.
        :Example:
            57 16 805199.
        """
        return '%s %s' % (
            self.passport_series(),
            self.passport_number()
        )


class JapanSpecProvider(object):
    """Class that provides special data for jp"""

    class Meta:
        name = 'japan_provider'

    @staticmethod
    def full_to_half(text, alnum=True):
        """
        Convert all full width katakana, alphanumeric and few special
        characters like （, ）, ・ to equivalent half width character.

        :param text: The text to be converted.
        :param alnum: Convert alphanumeric, default True.
        :return: Text with full width characters converted to half width.

        :Example:
            QVCｼﾞｬﾊﾟﾝ(0123)
        """
        fh_kana_special = {
            "ア": "ｱ", "イ": "ｲ", "ウ": "ｳ", "エ": "ｴ", "オ": "ｵ", "カ": "ｶ",
            "キ": "ｷ", "ク": "ｸ", "ケ": "ｹ", "コ": "ｺ", "ガ": "ｶﾞ", "ギ": "ｷﾞ",
            "グ": "ｸﾞ", "ゲ": "ｹﾞ", "ゴ": "ｺﾞ", "サ": "ｻ", "シ": "ｼ", "ス": "ｽ",
            "セ": "ｾ", "ソ": "ｿ", "ザ": "ｻﾞ", "ジ": "ｼﾞ", "ズ": "ｽﾞ", "ゼ": "ｾﾞ",
            "ゾ": "ｿﾞ", "タ": "ﾀ", "チ": "ﾁ", "ツ": "ﾂ", "テ": "ﾃ", "ト": "ﾄ",
            "ダ": "ﾀﾞ", "ヂ": "ﾁﾞ", "ヅ": "ﾂﾞ", "デ": "ﾃﾞ", "ド": "ﾄﾞ", "ナ": "ﾅ",
            "ニ": "ﾆ", "ヌ": "ﾇ", "ネ": "ﾈ", "ノ": "ﾉ", "ハ": "ﾊ", "ヒ": "ﾋ",
            "フ": "ﾌ", "ヘ": "ﾍ", "ホ": "ﾎ", "バ": "ﾊﾞ", "ビ": "ﾋﾞ", "ブ": "ﾌﾞ",
            "ベ": "ﾍﾞ", "ボ": "ﾎﾞ", "パ": "ﾊﾟ", "ピ": "ﾋﾟ", "プ": "ﾌﾟ", "ペ": "ﾍﾟ",
            "ポ": "ﾎﾟ", "マ": "ﾏ", "ミ": "ﾐ", "ム": "ﾑ", "メ": "ﾒ", "モ": "ﾓ",
            "ヤ": "ﾔ", "ユ": "ﾕ", "ヨ": "ﾖ", "ラ": "ﾗ", "リ": "ﾘ", "ル": "ﾙ",
            "レ": "ﾚ", "ロ": "ﾛ", "ワ": "ﾜ", "ヲ": "ｦ", "ン": "ﾝ", "ァ": "ｧ",
            "ィ": "ｨ", "ゥ": "ｩ", "ェ": "ｪ", "ォ": "ｫ", "ッ": "ｯ", "ャ": "ｬ",
            "ュ": "ｭ", "ョ": "ｮ", "！": "!", "＂": "\"", "＃": "#", "＄": "$",
            "％": "%", "＆": "&", "＇": "'", "（": "(", "）": ")", "＊": "*",
            "＋": "+", "ー": "ｰ", "／": "/",  "：": ":", "；": ";",
            "＜": "<", "＝": "=", "＞": ">", "？": "?", "＠": "@", "［": "[",
            "＼": "\\", "］": "]", "＾": "^", "＿": "_", "｀": "`", "｛": "{",
            "｜": "|", "｝": "}", "～": "~", "・": "･",  "「": "｢", "」": "｣"
        }
        # leaving "。": "｡", "、": "," out for now

        _fh_alnum_offset = 65248 # 0xFEE0
        result = ""
        for char in text:
            if char in fh_kana_special:
                result += fh_kana_special[char]
            elif alnum and ord("０") <= ord(char) <= ord("ｚ"):
                result += chr(ord(char) - _fh_alnum_offset)
            else:
                result += char
        return result

    @staticmethod
    def half_to_full(text, alnum=True):
        """
        Convert all half width katakana, alphanumeric, and special characters
        ((, ), ) to equivalent full width character.

        :param text: The text to be converted.
        :param alnum: Convert alphanumeric, default True.
        :return: Text with half width characters converted to full width.

        :Example:
            ＱＶＣジャパン（０１２３）
        """
        _hf_alnum_offset = 65248
        result = ""

        hf_voiced_kana = {
            "ｶﾞ": "ガ", "ｷﾞ": "ギ", "ｸﾞ": "グ", "ｹﾞ": "ゲ", "ｺﾞ": "ゴ", "ｻﾞ": "ザ",
            "ｼﾞ": "ジ", "ｽﾞ": "ズ", "ｾﾞ": "ゼ", "ｿﾞ": "ゾ", "ﾀﾞ": "ダ", "ﾁﾞ": "ヂ",
            "ﾂﾞ": "ヅ", "ﾃﾞ": "デ", "ﾄﾞ": "ド", "ﾊﾞ": "バ", "ﾋﾞ": "ビ", "ﾌﾞ": "ブ",
            "ﾍﾞ": "ベ", "ﾎﾞ": "ボ", "ﾊﾟ": "パ", "ﾋﾟ": "ピ", "ﾌﾟ": "プ", "ﾍﾟ": "ペ",
            "ﾎﾟ": "ポ"
        }
        hf_kana_special = {
            "ｱ": "ア", "ｲ": "イ", "ｳ": "ウ", "ｴ": "エ", "ｵ": "オ", "ｶ": "カ",
            "ｷ": "キ", "ｸ": "ク", "ｹ": "ケ", "ｺ": "コ", "ｻ": "サ", "ｼ": "シ",
            "ｽ": "ス", "ｾ": "セ", "ｿ": "ソ", "ﾀ": "タ", "ﾁ": "チ", "ﾂ": "ツ",
            "ﾃ": "テ", "ﾄ": "ト", "ﾅ": "ナ", "ﾆ": "ニ", "ﾇ": "ヌ", "ﾈ": "ネ",
            "ﾉ": "ノ", "ﾊ": "ハ", "ﾋ": "ヒ", "ﾌ": "フ", "ﾍ": "ヘ", "ﾎ": "ホ",
            "ﾏ": "マ", "ﾐ": "ミ", "ﾑ": "ム", "ﾒ": "メ", "ﾓ": "モ", "ﾔ": "ヤ",
            "ﾕ": "ユ", "ﾖ": "ヨ", "ﾗ": "ラ", "ﾘ": "リ", "ﾙ": "ル", "ﾚ": "レ",
            "ﾛ": "ロ", "ﾜ": "ワ", "ｦ": "ヲ", "ﾝ": "ン", "ｧ": "ァ", "ｨ": "ィ",
            "ｩ": "ゥ", "ｪ": "ェ", "ｫ": "ォ", "ｯ": "ッ", "ｬ": "ャ", "ｭ": "ュ",
            "ｮ": "ョ", "!": "！", "\"":"＂", "#": "＃", "$":"＄", "%": "％",
            "&": "＆", "'": "＇", "(": "（", ")": "）", "*": "＊", "+": "＋",
            "ｰ": "ー", "/": "／",  ":": "：", ";": "；", "<": "＜", "=": "＝",
            ">": "＞", "?": "？", "@": "＠", "[": "［", "\\": "＼", "]": "］",
            "^": "＾", "_": "＿", "`": "｀", "{": "｛", "|": "｜", "}": "｝",
            "~": "～", "･": "・", "｢": "「", "｣": "」"
        }

        def hf_parse(char, result):
            """
            Parse the char from half-width to full-width, append to result,
            and return result.

            :param char: Character to be parsed from half-width to full-width.
            :param result: Previous result string.
            :return: Result appended with parsed char.
            :Example:
                ラーメン
            """
            if char in hf_kana_special:
                result += hf_kana_special[char]
            elif alnum and ord("0") <= ord(char) <= ord("z"):
                result += chr(ord(char) + _hf_alnum_offset)
            else:
                result += char
            return result

        # leave "｡": "。", ",": "、", for now
        i = 0
        while i < len(text) - 1:
            # need to lookahead for separate voice mark
            pair = text[i] + text[i + 1]
            if (text[i + 1] == "ﾞ" or text[i + 1] == "ﾟ") and \
                pair in hf_voiced_kana:
                result += hf_voiced_kana[pair]
                i += 2
                continue
            else:
                result = hf_parse(text[i], result)
            i += 1

        if i == len(text) - 1:
            result = hf_parse(text[i], result)

        return result

