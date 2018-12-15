# -*- coding: utf-8 -*-
import re

import pytest

from mimesis import Hardware
from mimesis.data import (
    CPU,
    CPU_CODENAMES,
    CPU_MODEL_CODES,
    GENERATION,
    GRAPHICS,
    HDD_SSD,
    MANUFACTURERS,
    PHONE_MODELS,
    RAM_SIZES,
    RAM_TYPES,
    RESOLUTIONS,
    SCREEN_SIZES,
)

from . import patterns


class TestHardware(object):

    @pytest.fixture
    def hard(self):
        return Hardware()

    def test_str(self, hard):
        assert re.match(patterns.PROVIDER_STR_REGEX, str(hard))

    def test_resolution(self, hard):
        result = hard.resolution()
        assert result in RESOLUTIONS

    def test_screen_size(self, hard):
        result = hard.screen_size()
        assert result in SCREEN_SIZES

    def test_generation(self, hard):
        result = hard.generation()
        assert result in GENERATION
        assert isinstance(result, str)

    def test_cpu_model_code(self, hard):
        result = hard.cpu_model_code()
        assert result in CPU_MODEL_CODES
        assert isinstance(result, str)

    def test_cpu_frequency(self, hard):
        result = hard.cpu_frequency().split('G')[0]
        assert float(result) < 4.4

    def test_cpu(self, hard):
        result = hard.cpu()
        assert result in CPU

    def test_cpu_codename(self, hard):
        result = hard.cpu_codename()
        assert result in CPU_CODENAMES

    def test_ram_type(self, hard):
        result = hard.ram_type()
        assert result in RAM_TYPES

    def test_ram_size(self, hard):
        result = hard.ram_size()
        assert result in RAM_SIZES

    def test_ssd_or_hdd(self, hard):
        result = hard.ssd_or_hdd()
        assert result in HDD_SSD

    def test_graphics(self, hard):
        result = hard.graphics()
        assert result in GRAPHICS

    def test_manufacturer(self, hard):
        result = hard.manufacturer()
        assert result in MANUFACTURERS

    def test_phone_model(self, hard):
        result = hard.phone_model()
        assert result in PHONE_MODELS


class TestSeededHardware(object):

    @pytest.fixture
    def h1(self, seed):
        return Hardware(seed=seed)

    @pytest.fixture
    def h2(self, seed):
        return Hardware(seed=seed)

    def test_resolution(self, h1, h2):
        assert h1.resolution() == h2.resolution()

    def test_screen_size(self, h1, h2):
        assert h1.screen_size() == h2.screen_size()

    def test_generation(self, h1, h2):
        assert h1.generation() == h2.generation()

    def test_cpu_model_code(self, h1, h2):
        assert h1.cpu_model_code() == h2.cpu_model_code()

    def test_cpu_frequency(self, h1, h2):
        assert h1.cpu_frequency() == h2.cpu_frequency()

    def test_cpu(self, h1, h2):
        assert h1.cpu() == h2.cpu()

    def test_cpu_codename(self, h1, h2):
        assert h1.cpu_codename() == h2.cpu_codename()

    def test_ram_type(self, h1, h2):
        assert h1.ram_type() == h2.ram_type()

    def test_ram_size(self, h1, h2):
        assert h1.ram_size() == h2.ram_size()

    def test_ssd_or_hdd(self, h1, h2):
        assert h1.ssd_or_hdd() == h2.ssd_or_hdd()

    def test_graphics(self, h1, h2):
        assert h1.graphics() == h2.graphics()

    def test_manufacturer(self, h1, h2):
        assert h1.manufacturer() == h2.manufacturer()

    def test_phone_model(self, h1, h2):
        assert h1.phone_model() == h2.phone_model()
