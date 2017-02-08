# -*- coding: utf-8 -*-

from unittest import TestCase

from elizabeth.core.providers import Transport
from elizabeth.core.interdata import CAR, TRUCKS, AIRPLANES


class TransportTest(TestCase):
    def setUp(self):
        self.transport = Transport()

    def tearDown(self):
        del self.transport

    def test_truck(self):
        result = self.transport.truck().split('-')
        manufacturer, model = result[0], result[1]
        self.assertIn(manufacturer, TRUCKS)
        self.assertTrue(len(model) == 7)

        result = self.transport.truck(model_mask='###').split('-')
        manufacturer, model = result[0], result[1]
        self.assertIn(manufacturer, TRUCKS)
        self.assertTrue(len(model) == 3)

    def test_car(self):
        result = self.transport.car()
        self.assertIn(result, CAR)

    def test_airplane(self):
        mask = '@###'
        result = self.transport.airplane(model_mask=mask).split()
        manufacturer, model = result[0], result[1]
        self.assertIn(manufacturer, AIRPLANES)
        self.assertTrue(len(model) == len(mask))
