import extract
import unittest
import random

class TestExtract(unittest.TestCase):
    def setUp(self):
        pass
    def test_round_half_up(self):
        r = range(0, 2)
        nb_to_test = extract.round_half_up(random.uniform(0, 1))
        self.assertTrue(nb_to_test in r)
    def test_fetch_imgs(self):
        ig = extract.imgs_gen()
        self.assertTrue(next(ig))
    def test_log_payload_prep(self):
        message = 'The answer is *wait for a couple million years* 42'
        payload = extract.prepare_log_payload(message)
        self.assertEqual('{ "objType":"log", "message":"The answer is *wait for a couple million years* 42" }', payload)
    def test_image_payload_prep(self):
        message = (b'The answer is *wait for a couple million years* 42', 42, 42)
        payload = extract.prepare_image_payload(*message)
        self.assertEqual('{ "objType":"img", "image":"VGhlIGFuc3dlciBpcyAqd2FpdCBmb3IgYSBjb3VwbGUgbWlsbGlvbiB5ZWFycyogNDI=", "height":"42", "width":"42" }', payload)
    def test_base64_string_creation(self):
        byte_string = b'hello'
        self.assertEqual('aGVsbG8=', extract.create_base64_string(byte_string))

if __name__ == '__main__':
    unittest.main()