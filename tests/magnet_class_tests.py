import unittest

from src import Magnet

OPEN_FLAG = 1
CLOSE_FLAG = 0
magnet = Magnet()

class MagnetClassTest(unittest.TestCase):
    def test_create_instance(self):
        magnet_instance = Magnet()
        self.assertIsInstance(magnet_instance, Magnet)

    def test_read_open_state(self):
        magnet = Magnet()
        self.assertEqual(magnet.get_state(),OPEN_FLAG)

    def test_read_close_state(self):
        magnet = Magnet()
        self.assertEqual(magnet.get_state(),CLOSE_FLAG)
