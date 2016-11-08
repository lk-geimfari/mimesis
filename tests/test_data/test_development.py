# -*- coding: utf-8 -*-

from unittest import TestCase

import elizabeth._common as common
from elizabeth.elizabeth import Development


class DevelopmentTestCase(TestCase):
    def setUp(self):
        self.dev = Development()

    def tearDown(self):
        del self.dev

    def test_license(self):
        result = self.dev.software_license()
        self.assertIn(result, common.LICENSES)

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
        self.assertIn(result, common.PROGRAMMING_LANGS)

    def test_database(self):
        result = self.dev.database()
        self.assertIn(result, common.SQL)

        _result = self.dev.database(nosql=True)
        self.assertIn(_result, common.NOSQL)

    def test_other(self):
        result = self.dev.other()
        self.assertIn(result, common.OTHER_TECH)

    def test_framework(self):
        result = self.dev.framework(_type='front')
        self.assertIn(result, common.FRONTEND)

        _result = self.dev.framework(_type='back')
        self.assertIn(_result, common.BACKEND)

    def test_stack_of_tech(self):
        result = self.dev.stack_of_tech(nosql=True)
        self.assertIsInstance(result, dict)

    def test_os(self):
        result = self.dev.os()
        self.assertIn(result, common.OS)

    def test_stackoverflow_question(self):
        url = self.dev.stackoverflow_question()
        post_id = int(url.split('/')[-1])
        self.assertTrue(post_id >= 1000000)
        self.assertTrue(post_id <= 9999999)

    # TODO: Write it
    def test_hardware_info(self):
        pass
