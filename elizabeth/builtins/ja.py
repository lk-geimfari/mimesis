class JapanSpecProvider(object):
    """Class that provides special data for ja"""

    class Meta:
        name = 'japan_provider'

    @staticmethod
    def full_to_half(text, alnum=True):
        """Convert all full width katakana, alphanumeric and few special
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
            "＋": "+", "ー": "ｰ", "／": "/", "：": ":", "；": ";",
            "＜": "<", "＝": "=", "＞": ">", "？": "?", "＠": "@", "［": "[",
            "＼": "\\", "］": "]", "＾": "^", "＿": "_", "｀": "`", "｛": "{",
            "｜": "|", "｝": "}", "～": "~", "・": "･", "「": "｢", "」": "｣"
        }
        # leaving "。": "｡", "、": "," out for now

        _fh_alnum_offset = 65248  # 0xFEE0
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
        """Convert all half width katakana, alphanumeric, and special characters
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
            "ｮ": "ョ", "!": "！", "\"": "＂", "#": "＃", "$": "＄", "%": "％",
            "&": "＆", "'": "＇", "(": "（", ")": "）", "*": "＊", "+": "＋",
            "ｰ": "ー", "/": "／", ":": "：", ";": "；", "<": "＜", "=": "＝",
            ">": "＞", "?": "？", "@": "＠", "[": "［", "\\": "＼", "]": "］",
            "^": "＾", "_": "＿", "`": "｀", "{": "｛", "|": "｜", "}": "｝",
            "~": "～", "･": "・", "｢": "「", "｣": "」"
        }

        def hf_parse(char, result):
            """Parse the char from half-width to full-width, append to result,
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
