# -*- coding: utf-8 -*-

from unittest import TestCase

from elizabeth.core.intd import (
    CPU_CODENAMES, PHONE_MODELS, MEMORY,
    RESOLUTIONS, MANUFACTURERS, CPU,
    GENERATION, SCREEN_SIZES, GRAPHICS
)
from elizabeth.core.providers import Hardware


class HardwareTest(TestCase):
    def setUp(self):
        self.hard = Hardware()

    def tearDown(self):
        del self.hard

    def test_resolution(self):
        result = self.hard.resolution()
        self.assertIn(result, RESOLUTIONS)

    def test_screen_size(self):
        result = self.hard.screen_size()
        self.assertIn(result, SCREEN_SIZES)

    def test_generation(self):
        result = self.hard.generation()
        self.assertIn(result, GENERATION)

    def test_cpu_frequency(self):
        result = self.hard.cpu_frequency().split('G')[0]
        self.assertLess(float(result), 4.4)

    def test_cpu(self):
        result = self.hard.cpu()
        self.assertIn(result, CPU)

    def test_cpu_codename(self):
        result = self.hard.cpu_codename()
        self.assertIn(result, CPU_CODENAMES)

    def test_ram_type(self):
        result = self.hard.ram_type()
        self.assertIn(result, ['DDR2', 'DDR3', 'DDR4'])

    def test_ram_size(self):
        result = self.hard.ram_size().split(' ')
        self.assertGreater(len(result), 0)

    def test_ssd_or_hdd(self):
        result = self.hard.ssd_or_hdd()
        self.assertIn(result, MEMORY)

    def test_graphics(self):
        result = self.hard.graphics()
        self.assertIn(result, GRAPHICS)

    def test_manufacturer(self):
        result = self.hard.manufacturer()
        self.assertIn(result, MANUFACTURERS)

    def test_phone_model(self):
        result = self.hard.phone_model()
        self.assertIn(result, PHONE_MODELS)
