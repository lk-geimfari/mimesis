import os
import os.path as path
import json
import re
import logging

logging.basicConfig(level=logging.DEBUG)


# TODO: Refactor code, it's works very slowly.

class JsonMinimizer(object):
    def __init__(self, input_dir=None, output_dir=''):
        if not input_dir:
            self.input_dir = 'mimesis/data'
        else:
            self.input_dir = input_dir
        self.output_dir = output_dir
        self.input_abs = path.abspath(self.input_dir)

    def _json_minify(self, string, strip_space=True):
        """This function implemented by Pradyun S. Gedam.
        This function released under the MIT license.
        Repository: https://github.com/getify/JSON.minify/tree/python
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
                    # replace white space as defined in standard
                    tmp = re.sub('[ \t\n\r]+', '', tmp)
                new_str.append(tmp)
            elif not strip_space:
                # Replace comments with white space so that the JSON parser reports
                # the correct column numbers on parsing errors.
                new_str.append(' ' * (match.start() - index))

            index = match.end()
            val = match.group()

            if val == '"' and not (in_multi or in_single):
                escaped = end_slashes_re.search(string, 0, match.start())

                # start of string or unescaped quote character to end string
                if not in_string or (escaped is None or len(escaped.group()) % 2 == 0):  # noqa
                    in_string = not in_string
                index -= 1  # include " character in next catch
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
            elif not ((in_multi or in_single) or (val in ' \r\n\t' and strip_space)):  # noqa
                new_str.append(val)

            if not strip_space:
                if val in '\r\n':
                    new_str.append(val)
                elif in_multi or in_single:
                    new_str.append(' ' * len(val))

        new_str.append(string[index:])
        return ''.join(new_str)

    @staticmethod
    def is_json(file_name):
        if path.splitext(file_name)[1] == '.json':
            return True

    def minify(self, input_file, output_file):

        file_path = path.abspath(input_file)

        with open(file_path, 'r') as f:
            json_text = self._json_minify(f.read())
            minimized = json.dumps(json.loads(json_text),
                                   separators=(',', ':'))
        if len(output_file) > 0:
            output_path = path.abspath(output_file)
            abs_path = os.path.abspath(os.path.dirname(output_path))

            if not os.path.exists(abs_path):
                os.makedirs(abs_path)

            with open(output_path, 'w') as f:
                f.write(minimized)

        splitted = input_file.split('/')
        locale, filename = splitted[-2], splitted[-1]

        logging.info(
            '\033[92m File {locale}/{file} is minimized.\033[0m'.format(
                locale=locale, file=filename))

    def find(self):
        paths = []

        for root, dirs, files in os.walk(self.input_dir):
            for file in files:
                if self.is_json(file):
                    rel_path = path.relpath(root, self.input_dir)
                    paths.append(path.join(rel_path, file))

        return paths

    def start(self):
        logging.info('\033[34m JSON files minimizer is started.\033[0m')

        for rel_path in self.find():
            input_file = path.join(self.input_abs, rel_path)
            output_file = ''
            if len(self.output_dir) > 0:
                output_file = os.path.join(self.output_dir, rel_path)

            self.minify(input_file, output_file)

        logging.info('\033[34m All JSON file minimized!\033[0m')


if __name__ == '__main__':
    output = 'mimesis/minimized_data'

    answer = input('Do you want to start (y/n): ')
    answer = answer.lower().strip()

    if answer in ('y', 'yes'):
        minimizer = JsonMinimizer(output)
        minimizer.start()
