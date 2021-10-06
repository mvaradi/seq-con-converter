from unittest import TestCase
from seq_con_json_converter.utils import rgb_to_hex


class TestUtils(TestCase):

    def test_rgb_to_hex_with_rgb(self):
        # Test if the function can convert RGB to HEX
        self.assertEqual(rgb_to_hex("rgb(211,211,211)"), "#d3d3d3")

    def test_rgb_to_hex_with_hex(self):
        # Test if the function just return a HEX input
        self.assertEqual(rgb_to_hex("#fff"), "#fff")

    def test_rgb_to_het_raises_error(self):
        with self.assertRaises(ValueError) as context:
            rgb_to_hex("foo")
            self.assertTrue('Only RGB or HEX input allowed' in context.exception)