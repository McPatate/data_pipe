import pika

class RMQHelper:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost')
        )

    def open_channel(self):
        return self.connection.channel()

    def create_properties(self):
        return pika.BasicProperties(delivery_mode=2) # persistent message

    def __del__(self):
        self.connection.close()
