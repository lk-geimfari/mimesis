import json

from elizabeth.data import (CSS_PROPERTIES, CSS_SELECTORS, CSS_SIZE_UNITS,
                            HTML_CONTAINER_TAGS, HTML_MARKUP_TAGS)
from elizabeth.providers import BaseProvider, Hardware, Internet, Personal
from elizabeth.providers.text import Text


class Structured(BaseProvider):
    """Provider for structured text data such as CSS, Delimited, HTML, etc."""

    def __init__(self, *args, **kwargs):
        """
        :param locale: Current locale.
        """
        super().__init__(*args, **kwargs)
        self.internet = Internet()
        self.text = Text()

    def css(self):
        """Generates a random snippet of CSS.

        :return: CSS.
        :rtype: str
        :Example:
            'strong {
                pointer: crosshair;
                padding-right: 46pt;
                margin-left: 38em;
                padding-right: 65em
            }'
        """
        selector = self.random.choice(CSS_SELECTORS)
        css_sel = '{}{}'.format(selector, self.text.word())

        cont_tag = self.random.choice(list(HTML_CONTAINER_TAGS.keys()))
        mrk_tag = self.random.choice(HTML_MARKUP_TAGS)

        base = '{}'.format(self.random.choice([cont_tag, mrk_tag, css_sel]))
        props = '; '.join(
            [self.css_property() for _ in range(self.random.randint(1, 6))])
        return '{} {{{}}}'.format(base, props)

    def css_property(self):
        """Generates a random snippet of CSS that assigns value to a property.

        :return: CSS property.
        :rtype: str
        :Examples:
            'background-color: #f4d3a1'
        """
        prop = self.random.choice(list(CSS_PROPERTIES.keys()))
        val = CSS_PROPERTIES[prop]

        if isinstance(val, list):
            val = self.random.choice(val)
        elif val == 'color':
            val = self.text.hex_color()
        elif val == 'size':
            val = '{}{}'.format(self.random.randint(1, 99),
                                self.random.choice(CSS_SIZE_UNITS))

        return '{}: {}'.format(prop, val)

    def html(self):
        """Generate a random HTML tag with text inside and some attrs set.

        :return: HTML.
        :rtype: str
        :Examples:
            '<span class="select" id="careers">
                Ports are created with the built-in function open_port.
            </span>'
        """
        tag_name = self.random.choice(list(HTML_CONTAINER_TAGS))
        tag_attributes = list(HTML_CONTAINER_TAGS[tag_name])
        k = self.random.randint(1, len(tag_attributes))

        selected_attrs = self.random.sample(tag_attributes, k=k)

        attrs = []
        for attr in selected_attrs:
            attrs.append('{}="{}"'.format(
                attr, self.html_attribute_value(tag_name, attr)))

        html_result = '<{tag} {attrs}>{content}</{tag}>'
        return html_result.format(
            tag=tag_name,
            attrs=' '.join(attrs),
            content=self.text.sentence(),
        )

    def html_attribute_value(self, tag, attribute):
        """Random value for specified HTML tag attribute.

        :param tag: An HTML tag.
        :param attribute: An attribute of the specified tag.
        :type tag: str
        :type attribute: str
        :return: An attribute.
        :rtype: str
        """
        try:
            value = HTML_CONTAINER_TAGS[tag][attribute]
        except KeyError:
            raise NotImplementedError(
                'Tag {} or attribute {} is not supported'.format(
                    tag, attribute))

        if isinstance(value, list):
            value = self.random.choice(value)
        elif value == 'css':
            value = self.css_property()
        elif value == 'word':
            value = self.text.word()
        elif value == 'url':
            value = self.internet.home_page()
        else:
            raise NotImplementedError(
                'Attribute type {} is not implemented'.format(value))
        return value

    def json(self, provider_name, items=5):
        """Generate a random snippet of JSON

        :param provider_name: Name of provider to generate JSON data for.
        :type provider_name: str
        :param items: Number of top-level items to include.
        :type items: int
        :return: JSON.
        :rtype: str
        """
        providers = {
            'hardware': {
                'provider': Hardware,
                'root_element': 'computers',
            },
            'personal': {
                'provider': Personal,
                'root_element': 'users',
            },
        }

        try:
            provider_data = providers[provider_name.lower()]
        except KeyError:
            raise NotImplementedError(
                'Provider {} is not supported'.format(provider_name))

        try:
            provider = provider_data['provider'](self.locale)
        except TypeError:  # handle providers that do not accept locale
            provider = provider_data['provider']()

        root_element = provider_data['root_element']

        data = {root_element: []}

        for _ in range(items):
            element = dict()
            for attribute_name in dir(provider):
                attribute = getattr(provider, attribute_name)
                if attribute_name[:1] != '_' and callable(attribute):
                    element[attribute_name] = attribute()
            data[root_element].append(element)

        return json.dumps(data, indent=4)
