from mimesis.providers import BaseProvider
from mimesis.utils import pull


class Text(BaseProvider):
    """Class for generate text data, i.e text, lorem ipsum and another."""

    def __init__(self, *args, **kwargs):
        """
        :param locale: Current locale.
        """
        super().__init__(*args, **kwargs)
        self.data = pull('text.json', self.locale)

    def alphabet(self, letter_case=None):
        """Get an alphabet for current locale.

        :param letter_case: Letter case.
        :return: Alphabet.
        :rtype: list
        """
        letter_case = 'uppercase' if \
            not letter_case else letter_case

        alpha = self.data['alphabet'][letter_case]
        return alpha

    def level(self):
        """Generate a random level of danger or something else.

        :return: Level.
        :Example:
            critical.
        """
        levels = self.data['level']
        return self.random.choice(levels)

    def text(self, quantity=5):
        """Generate the text.

        :param quantity: Quantity of sentences.
        :return: Text.
        :Example:
            Haskell is a standardized, general-purpose purely
            functional programming language, with non-strict semantics
            and strong static typing.
        """
        text = ''
        for _ in range(int(quantity)):
            text += ' ' + self.random.choice(self.data['text'])
        return text.strip()

    def sentence(self):
        """Get a random sentence from text.

        :return: Sentence.
        :Example:
            Any element of a tuple can be accessed in constant time.
        """
        return self.text(quantity=1)

    def title(self):
        """Get a random title.

        :return: The title.
        :Example:
            Erlang - is a general-purpose, concurrent,
            functional programming language.
        """
        return self.text(quantity=1)

    def words(self, quantity=5):
        """Get the random words.

        :param quantity: Quantity of words. Default is 5.
        :return: Word list.
        :Example:
            science, network, god, octopus, love.
        """
        words = self.data['words']['normal']
        words_list = [self.random.choice(words) for _ in range(int(quantity))]
        return words_list

    def word(self):
        """Get a random word.

        :return: Single word.
        :Example:
            Science.
        """
        return self.words(quantity=1)[0]

    def swear_word(self):
        """Get a random swear word.

        :return: Swear word.
        :Example:
            Damn.
        """
        bad_words = self.data['words']['bad']
        return self.random.choice(bad_words)

    def quote(self):
        """Get a random quote.

        :return: Quote from movie.
        :Example:
            "Bond... James Bond."
        """
        quotes = self.data['quotes']
        return self.random.choice(quotes)

    def color(self):
        """Get a random name of color.

        :return: Color name.
        :Example:
            Red.
        """
        colors = self.data['color']
        return self.random.choice(colors)

    def hex_color(self):
        """Generate a hex color.

        :return: Hex color code.
        :Example:
            #D8346B
        """
        letters = '0123456789ABCDEF'
        color_code = '#' + ''.join(self.random.sample(letters, 6))
        return color_code

    def answer(self):
        """Get a random answer in current language.

        :return: An answer.
        :rtype: str
        :Example:
            No
        """
        answers = self.data['answers']
        return self.random.choice(answers)
