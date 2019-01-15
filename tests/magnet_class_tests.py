import unittest

from src import Magnet


magnet = Magnet()

class MagnetClassTest(unittest.TestCase):
    def test_create_instance(self):
        magnet_instance = Magnet()
        self.assertIsInstance(magnet_instance, Magnet)


