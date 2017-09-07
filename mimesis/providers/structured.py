import json

from mimesis.data import (CSS_PROPERTIES, CSS_SELECTORS, CSS_SIZE_UNITS,
                          HTML_CONTAINER_TAGS, HTML_MARKUP_TAGS)
from mimesis.providers import BaseProvider, Internet
from mimesis.providers.text import Text


class Structured(BaseProvider):
    """Provider for structured text data such as CSS, HTML, JSON etc."""

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

    def json(self, items=5, max_depth=3, recursive=False):
        """Generate a random snippet of JSON.

        :param items: Number of top-level items to produce.
        :param max_depth: Maximum depth of each top-level item.
        :param recursive:
            When used recursively, will return a Python object instead of JSON
            string.
        :return: JSON
        """

        # choose root element type
        root = self.random.choice([list, dict])()

        for _ in range(items):

            key = self.text.word()

            if max_depth > 0:
                value = self.random.choice([
                    self.text.sentence(),
                    self.random.randint(1, 10000),
                    self.random.random(),
                    self.json(max_depth=max_depth - 1,
                              recursive=True),
                ])
                if isinstance(root, list):
                    root.append(value)
                elif isinstance(root, dict):
                    root[key] = value

        if recursive:
            return root

        return json.dumps(root, indent=4)
