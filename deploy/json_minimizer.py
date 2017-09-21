import os
from os.path import (
    abspath,
    dirname,
    exists,
    join,
    splitext,
    relpath,
)
import json

import re


class Minimizer(object):
    """Minify content of all json file for all locales.
    """

    def __init__(self):
        self.data_path = '/mimesis/data'
        self.data_dir = dirname(
            dirname(abspath(__file__))) + self.data_path

    @staticmethod
    def is_json(file_name):
        return splitext(file_name)[1] == '.json'

    @staticmethod
    def __minify(string, strip_space=True):
        """Author of this functions: Gerald Storer.
        The code released under the MIT license.
        """
        tokenizer = re.compile('"|(/\*)|(\*/)|(//)|\n|\r')
        end_slashes_re = re.compile(r'(\\)*$')

        in_string = False
        in_multi = False
        in_single = False

        new_str = []
        index = 0

        for match in re.finditer(tokenizer, string):
            if not (in_multi or in_single):
                tmp = string[index:match.start()]
                if not in_string and strip_space:
                    tmp = re.sub('[ \t\n\r]+', '', tmp)
                new_str.append(tmp)
            elif not strip_space:
                new_str.append(' ' * (match.start() - index))

            index = match.end()
            val = match.group()

            if val == '"' and not (in_multi or in_single):
                escaped = end_slashes_re.search(string, 0, match.start())
                if not in_string or (escaped is None or len(escaped.group()) % 2 == 0):
                    in_string = not in_string
                index -= 1
            elif not (in_string or in_multi or in_single):
                if val == '/*':
                    in_multi = True
                elif val == '//':
                    in_single = True
            elif val == '*/' and in_multi and not (in_string or in_single):
                in_multi = False
                if not strip_space:
                    new_str.append(' ' * len(val))
            elif val in '\r\n' and not (in_multi or in_string) and in_single:
                in_single = False
            elif not ((in_multi or in_single) or (val in ' \r\n\t' and strip_space)):
                new_str.append(val)

            if not strip_space:
                if val in '\r\n':
                    new_str.append(val)
                elif in_multi or in_single:
                    new_str.append(' ' * len(val))

        new_str.append(string[index:])
        return ''.join(new_str)

    @staticmethod
    def minify(file_path):
        """Prepare files to minify.
        """
        with open(file_path, 'r') as f:
            json_text = Minimizer().__minify(json.loads(f.read()))
            minimized = json.dumps(json_text, separators=(',', ':'))

        if len(file_path) > 0:
            output_path = abspath(file_path)
            abs_path = abspath(dirname(output_path))

            if not exists(abs_path):
                os.makedirs(abs_path)

            with open(output_path, 'w') as f:
                f.write(minimized)

    def find(self):
        """Find all files of all locales.
        """
        paths = []

        for root, _, files in os.walk(self.data_dir):
            for file in sorted(files):
                if self.is_json(file):
                    rel_path = relpath(root, self.data_dir)
                    paths.append(join(rel_path, file))

        return sorted(paths)

    def start(self):
        """Start json minimizer and exit when all json
        files was minimized.
        """
        for rel_path in self.find():
            file_path = join(self.data_dir, rel_path)
            self.minify(file_path)

        return exit(0)


if __name__ == '__main__':
    minimizer = Minimizer()
    minimizer.start()
