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
    def minify(file_path):
        """Prepare files to minify.
        """
        with open(file_path, 'r') as f:
            json_text = json.loads(f.read())
            minimized = json.dumps(json_text, separators=(',', ':'),
                                   sort_keys=True, indent=0)

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
