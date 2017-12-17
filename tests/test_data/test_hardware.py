# -*- coding: utf-8 -*-
import pytest

from mimesis import Hardware
from mimesis.data import (CPU, CPU_CODENAMES, GENERATION, GENERATION_ABBR,
                          GRAPHICS, HDD_SSD, MANUFACTURERS, PHONE_MODELS,
                          RESOLUTIONS, SCREEN_SIZES)


@pytest.fixture
def hard():
    return Hardware()


@pytest.fixture
def _seeded_hard():
    return Hardware(seed=42)


def test_resolution(hard):
    result = hard.resolution()
    assert result in RESOLUTIONS


def test_seeded_resolution(_seeded_hard):
    result = _seeded_hard.resolution()
    assert result == '1680x1050'
    result = _seeded_hard.resolution()
    assert result == '2880x1920'


def test_screen_size(hard):
    result = hard.screen_size()
    assert result in SCREEN_SIZES


def test_seeded_screen_size(_seeded_hard):
    result = _seeded_hard.screen_size()
    assert result == '14.1″'
    result = _seeded_hard.screen_size()
    assert result == '12.1″'


def test_generation(hard):
    result = hard.generation()
    assert result in GENERATION
    assert isinstance(result, str)

    abbr = hard.generation(abbr=True)
    assert abbr in GENERATION_ABBR
    assert isinstance(abbr, str)


def test_seeded_generation(_seeded_hard):
    result = _seeded_hard.generation(abbr=True)
    assert result == '5675R'
    result = _seeded_hard.generation()
    assert result == '2nd Generation'
    result = _seeded_hard.generation()
    assert result == '2nd Generation'
    result = _seeded_hard.generation()
    assert result == '7th Generation'


def test_cpu_frequency(hard):
    result = hard.cpu_frequency().split('G')[0]
    assert float(result) < 4.4


def test_seeded_cpu_frequency(_seeded_hard):
    result = _seeded_hard.cpu_frequency()
    assert result == '3.3GHz'
    result = _seeded_hard.cpu_frequency()
    assert result == '1.6GHz'


def test_cpu(hard):
    result = hard.cpu()
    assert result in CPU


def test_seeded_cpu(_seeded_hard):
    result = _seeded_hard.cpu()
    assert result == 'AMD Ryzen 7 1800X'
    result = _seeded_hard.cpu()
    assert result == 'AMD Ryzen 7 1800X'
    result = _seeded_hard.cpu()
    assert result == 'Intel® Core i5'


def test_cpu_codename(hard):
    result = hard.cpu_codename()
    assert result in CPU_CODENAMES


def test_seeded_cpu_codename(_seeded_hard):
    result = _seeded_hard.cpu_codename()
    assert result == 'Cannonlake'
    result = _seeded_hard.cpu_codename()
    assert result == 'Haswell'


def test_ram_type(hard):
    result = hard.ram_type()
    assert result in ['DDR2', 'DDR3', 'DDR4']


def test_seeded_ram_type(_seeded_hard):
    result = _seeded_hard.ram_type()
    assert result == 'DDR4'
    result = _seeded_hard.ram_type()
    assert result == 'DDR2'


def test_ram_size(hard):
    result = hard.ram_size().split(' ')
    assert len(result) > 0


def test_seeded_ram_size(_seeded_hard):
    result = _seeded_hard.ram_size()
    assert result == '64GB'
    result = _seeded_hard.ram_size()
    assert result == '4GB'


def test_ssd_or_hdd(hard):
    result = hard.ssd_or_hdd()
    assert result in HDD_SSD


def test_seeded_ssd_or_hdd(_seeded_hard):
    result = _seeded_hard.ssd_or_hdd()
    assert result == '512GB SSD'
    result = _seeded_hard.ssd_or_hdd()
    assert result == '64GB SSD'


def test_graphics(hard):
    result = hard.graphics()
    assert result in GRAPHICS


def test_seeded_graphics(_seeded_hard):
    result = _seeded_hard.graphics()
    assert result == 'NVIDIA GeForce GTX 980'
    result = _seeded_hard.graphics()
    assert result == 'Intel® Iris™ Graphics 550'


def test_manufacturer(hard):
    result = hard.manufacturer()
    assert result in MANUFACTURERS


def test_seeded_manufacturer(_seeded_hard):
    result = _seeded_hard.manufacturer()
    assert result == 'Fujitsu'
    result = _seeded_hard.manufacturer()
    assert result == 'Acer'


def test_phone_model(hard):
    result = hard.phone_model()
    assert result in PHONE_MODELS


def test_seeded_phone_model(_seeded_hard):
    result = _seeded_hard.phone_model()
    assert result == 'Nokia Lumia 2520'
    result = _seeded_hard.phone_model()
    assert result == 'Apple iPhone 6s'
