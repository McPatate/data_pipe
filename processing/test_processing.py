import processing
import unittest
import random

class TestProcessing(unittest.TestCase):
    def setUp(self):
        pass
    def test_base64_string_creation(self):
        byte_string = b'hello'
        self.assertEqual('aGVsbG8=', processing.create_base64_string(byte_string))
    def test_decoding_base64_string(self):
        string = 'aGVsbG8='
        self.assertEqual(b'hello', processing.decode_base64_string(string))

if __name__ == '__main__':
    unittest.main()