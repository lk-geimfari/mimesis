# -*- coding: utf-8 -*-

from unittest import TestCase

import elizabeth.data.common as common
from elizabeth.elizabeth import Hardware


class HardwareTestCase(TestCase):
    def setUp(self):
        self.hard = Hardware()

    def tearDown(self):
        del self.hard

    def test_resolution(self):
        result = self.hard.resolution()
        self.assertIn(result, common.RESOLUTIONS)

    def test_screen_size(self):
        result = self.hard.screen_size()
        self.assertIn(result, common.SCREEN_SIZES)

    def test_generation(self):
        result = self.hard.generation()
        self.assertIn(result, common.GENERATION)

    def test_cpu_frequency(self):
        result = self.hard.cpu_frequency().split('G')[0]
        self.assertLess(float(result), 4.4)

    def test_cpu(self):
        result = self.hard.cpu()
        self.assertIn(result, common.CPU)

    def test_cpu_codename(self):
        result = self.hard.cpu_codename()
        self.assertIn(result, common.CPU_CODENAMES)

    def test_ram_type(self):
        result = self.hard.ram_type()
        self.assertIn(result, ['DDR2', 'DDR3', 'DDR4'])

    def test_ram_size(self):
        result = self.hard.ram_size().split(' ')
        self.assertGreater(len(result), 0)

    def test_ssd_or_hdd(self):
        result = self.hard.ssd_or_hdd()
        self.assertIn(result, common.MEMORY)

    def test_graphics(self):
        result = self.hard.graphics()
        self.assertIn(result, common.GRAPHICS)

    def test_manufacturer(self):
        result = self.hard.manufacturer()
        self.assertIn(result, common.MANUFACTURERS)

    def test_hardware_full(self):
        result = self.hard.hardware_info()
        self.assertGreater(len(result), 15)

    def test_phone_model(self):
        result = self.hard.phone_model()
        self.assertIn(result, common.PHONE_MODELS)
