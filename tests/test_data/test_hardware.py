# -*- coding: utf-8 -*-

import pytest

from elizabeth.core.providers import Hardware
from elizabeth.data.int import (
    CPU_CODENAMES, PHONE_MODELS, HDD_SSD,
    RESOLUTIONS, MANUFACTURERS, CPU,
    GENERATION, SCREEN_SIZES, GRAPHICS,
    GENERATION_ABBR,
)


@pytest.fixture
def hard():
    return Hardware()


def test_resolution(hard):
    result = hard.resolution()
    assert result in RESOLUTIONS


def test_screen_size(hard):
    result = hard.screen_size()
    assert result in SCREEN_SIZES


def test_generation(hard):
    result = hard.generation()
    assert result in GENERATION
    assert isinstance(result, str)

    abbr = hard.generation(abbr=True)
    assert abbr in GENERATION_ABBR
    assert isinstance(abbr, str)


def test_cpu_frequency(hard):
    result = hard.cpu_frequency().split('G')[0]
    assert float(result) < 4.4


def test_cpu(hard):
    result = hard.cpu()
    assert result in CPU


def test_cpu_codename(hard):
    result = hard.cpu_codename()
    assert result in CPU_CODENAMES


def test_ram_type(hard):
    result = hard.ram_type()
    assert result in ['DDR2', 'DDR3', 'DDR4']


def test_ram_size(hard):
    result = hard.ram_size().split(' ')
    assert len(result) > 0


def test_ssd_or_hdd(hard):
    result = hard.ssd_or_hdd()
    assert result in HDD_SSD


def test_graphics(hard):
    result = hard.graphics()
    assert result in GRAPHICS


def test_manufacturer(hard):
    result = hard.manufacturer()
    assert result in MANUFACTURERS


def test_phone_model(hard):
    result = hard.phone_model()
    assert result in PHONE_MODELS
