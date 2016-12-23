# -*- coding: utf-8 -*-

from unittest import TestCase

from elizabeth.core.elizabeth import Transport
import elizabeth.core.interdata as common


class TransportTest(TestCase):
    def setUp(self):
        self.transport = Transport()

    def tearDown(self):
        del self.transport

    def test_truck(self):
        result = self.transport.truck().split('-')
        manufacturer, model = result[0], result[1]
        self.assertIn(manufacturer, common.TRUCKS)
        self.assertTrue(len(model) == 7)

        result = self.transport.truck(model_mask='###').split('-')
        manufacturer, model = result[0], result[1]
        self.assertIn(manufacturer, common.TRUCKS)
        self.assertTrue(len(model) == 3)

    def test_car(self):
        result = self.transport.car()
        self.assertIn(result, common.CAR)

    def test_airplane(self):
        mask = '@###'
        result = self.transport.airplane(model_mask=mask).split()
        manufacturer, model = result[0], result[1]
        self.assertIn(manufacturer, common.AIRPLANES)
        self.assertTrue(len(model) == len(mask))
