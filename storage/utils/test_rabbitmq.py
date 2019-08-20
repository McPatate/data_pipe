import unittest
import pika
import rabbitmq

class TestRMQHelper(unittest.TestCase):
    def setUp(self):
        self.rmq = rabbitmq.RMQHelper()
    def test_connection(self):
        self.assertTrue(self.rmq.connection)
    def test_open_channel(self):
        self.assertTrue(self.rmq.open_channel(), type(pika.channel.Channel))
    def test_property_creation(self):
        self.assertTrue(self.rmq.create_properties(), pika.BasicProperties(delivery_mode=2))

if __name__ == '__main__':
    unittest.main()