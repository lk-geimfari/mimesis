# -*- coding: utf-8 -*-

import pytest
import re

from elizabeth.core.providers import Network

from ._patterns import *


@pytest.fixture
def net():
    return Network()


def test_ip_v4(net):
    ip = net.ip_v4()
    assert re.match(IP_V4_REGEX, ip)


def test_ip_v6(net):
    ip = net.ip_v6()
    assert re.match(IP_V6_REGEX, ip)


def test_mac_address(net):
    mac = net.mac_address()
    assert re.match(MAC_ADDRESS_REGEX, mac)
