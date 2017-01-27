# -*- coding: utf-8 -*-

import re
from unittest import TestCase

from elizabeth.core.providers import Network

from ._patterns import *


class NetworkTest(TestCase):
    def setUp(self):
        self.net = Network()

    def test_ip_v4(self):
        ip = self.net.ip_v4()
        self.assertTrue(re.match(IP_V4_REGEX, ip))

    def test_ip_v6(self):
        ip = self.net.ip_v6()
        self.assertTrue(re.match(IP_V6_REGEX, ip))

    def test_mac_address(self):
        mac = self.net.mac_address()
        self.assertTrue(re.match(MAC_ADDRESS_REGEX, mac))
