import unittest

from elizabeth.builtins import USASpecProvider


class USATest(unittest.TestCase):
    def setUp(self):
        self.usa = USASpecProvider()

    def tearDown(self):
        del self.usa

    def test_usps_tracking_number(self):
        result = self.usa.tracking_number(service='usps')
        self.assertIsNotNone(result)
        self.assertTrue(len(result) == 24 or len(result) == 17)

        result_1 = self.usa.tracking_number(service='fedex')
        self.assertIsNotNone(result_1)
        self.assertTrue(len(result_1) == 14 or len(result_1) == 18)

        result_2 = self.usa.tracking_number(service='ups')
        self.assertIsNotNone(result_2)
        self.assertTrue(len(result_2) == 18)

        self.assertRaises(ValueError,
                          lambda: self.usa.tracking_number(service='x'))

    def test_personality(self):
        result = self.usa.personality(category='rheti')
        self.assertTrue((int(result)) <= 9 or (int(result) >= 1))

        result_1 = self.usa.personality(category='mbti')
        self.assertIsInstance(result_1, str)
        self.assertTrue(len(result_1) == 4)
        self.assertTrue(result_1.isupper())

    def test_ssn(self):
        result = self.usa.ssn()
        self.assertIsNotNone(result)
        self.assertNotEqual('666', result[:3])
        self.assertRegex(result, '^\d{3}-\d{2}-\d{4}$')
        self.assertTrue(result.replace('-', '').isdigit())
        self.assertTrue(len(result.replace('-', '')) == 9)
