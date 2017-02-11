# -*- coding: utf-8 -*-

import unittest

from elizabeth.core.providers import Development
from elizabeth.core.intd import (
    FRONTEND,
    PROGRAMMING_LANGS,
    OS,
    OTHER_TECH,
    LICENSES,
    NOSQL,
    BACKEND,
    SQL
)


class DevelopmentTest(unittest.TestCase):
    def setUp(self):
        self.dev = Development()

    def tearDown(self):
        del self.dev

    def test_license(self):
        result = self.dev.software_license()
        self.assertIn(result, LICENSES)

    def test_version(self):
        result = self.dev.version().split('.')
        major = int(result[0])
        self.assertTrue((major >= 0) and (major <= 11))
        minor = int(result[1])
        self.assertTrue((minor >= 0) and (minor <= 11))
        micro = int(result[2])
        self.assertTrue((micro >= 0) and (micro <= 11))

    def test_programming_language(self):
        result = self.dev.programming_language()
        self.assertIn(result, PROGRAMMING_LANGS)

    def test_database(self):
        result = self.dev.database()
        self.assertIn(result, SQL)

        _result = self.dev.database(nosql=True)
        self.assertIn(_result, NOSQL)

    def test_other(self):
        result = self.dev.other()
        self.assertIn(result, OTHER_TECH)

    def test_frontend(self):
        result = self.dev.frontend()
        self.assertIn(result, FRONTEND)

    def test_backend(self):
        _result = self.dev.backend()
        self.assertIn(_result, BACKEND)

    def test_os(self):
        result = self.dev.os()
        self.assertIn(result, OS)

    def test_stackoverflow_question(self):
        url = self.dev.stackoverflow_question()
        post_id = int(url.split('/')[-1])
        self.assertTrue(post_id >= 1000000)
        self.assertTrue(post_id <= 9999999)

    # TODO: Write it
    def test_hardware_info(self):
        pass
