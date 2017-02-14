# -*- coding: utf-8 -*-

import pytest

from elizabeth.core.intd import (
    CPU_CODENAMES, PHONE_MODELS, MEMORY,
    RESOLUTIONS, MANUFACTURERS, CPU,
    GENERATION, SCREEN_SIZES, GRAPHICS
)
from elizabeth.core.providers import Hardware


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
    assert result in MEMORY


def test_graphics(hard):
    result = hard.graphics()
    assert result in GRAPHICS


def test_manufacturer(hard):
    result = hard.manufacturer()
    assert result in MANUFACTURERS


def test_phone_model(hard):
    result = hard.phone_model()
    assert result in PHONE_MODELS
