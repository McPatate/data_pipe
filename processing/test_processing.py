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
    def test_body_cleanup(self):
        byte_string = b'henl\no\n good sir\n'
        self.assertEqual('henlo good sir', processing.clean_body(byte_string))
    # def test_image_payload_preparation(self):
    #     obj = {
    #         "objType": "img",
    #         "image": "/9j/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wgARCABYAFcDASIAAhEBAxEB/8QAGwAAAgMBAQEAAAAAAAAAAAAABQYAAwQCAQf/xAAYAQADAQEAAAAAAAAAAAAAAAABAgMEAP/aAAwDAQACEAMQAAABDdYGK+jPzVsCmfZZPKMVmZY65ggEobtM5hOnXv6XRQXRyRn9AB1H54/nnF5E6r7dfHQS55CjvlXd66b7s7X0BQhsFhuNWfR1N2fRnOZHl8CKt2e597Q+fPnsYr+bQa18o1L/AFiZbjw5keVRqL12ezqNf0H5689j3Y6hYYj4lDifoC0uZj10YoUT+5E2lD0lsowTJOtHkgJ1lkOMjJJt/8QAJBAAAgICAgICAgMAAAAAAAAAAgMBBAAFERITIhQxITIVJDP/2gAIAQEAAQUC4kqqWMGWV2Hgh7AHje1wqnjyEiIbfc2YN1VgX3WFA5Vg5w0zCbqpFOsrmsrNlsOOtAqNvxcqUjslKRNxosIbNcAXrlBWGLYCZN5JRBJ4y92ZsAb4adRrUI70m3bCQsbT/cqqzqlVQFVNRjsGWVJVVbawQWkGH/J7b2p2GtFgGEW0XImxdGO6qwu5+KYvLWQsl7Sv0/sbGagrprNRHi64JyzPrTHvaHbPkq+46rVb8tqTKQFC+rBeAsrzE/IsRZW7yTY/I0vxbHOM1M8t59F/oTRHBeLmgxsPc0guNiYWRzXtxkZqv3KZgPqDPrgwk8sMC6FSqKK7i4G2UebInNT9h9YwORGeok1RLKyIxavRnu88jNZPAgyOCfEY27EY/YzM/KPDtGWQDGZTq9R4mJjK7umDc4ht2ZwjIs5z2Ka9CZxdWByBiM//xAAkEQACAgIBAwQDAAAAAAAAAAAAAQIRAyESEDFBBBMiMkJRYf/aAAgBAwEBPwGEl2M2WXHQo+ZHCiUr0iLUVRHhVUeojriihJuoruZP6RlS2W0qJ5PBjSfckl+BkJLfSX2ZBHKN0ZX4Ek0I5fNnufoqb2cK3IeZ+BqpNE4qyMEhs+z30//EAB8RAAICAwACAwAAAAAAAAAAAAABEBECEiFBcSAxUf/aAAgBAgEBPwHZfRsz3G34bF4mWK8Qu8EUUzvwycOFFQ0a2LE9HPMY9Rdw3Uf/xAArEAACAQIEBQMEAwAAAAAAAAABAgADERIhIjEEEBNBUSMyQmFxgaEUILH/2gAIAQEABj8CyiJtfdpdXCgZks0RRhZr33gC8K4BHvvkOVViNGEymhN0H7mrRc7GU6iteiR37WG0y1m+4O0WlTW5OQgRmXqt4ztKYUkrawl3pG8SivDVNWWK0swuZ9MML3w0gc2hp0atfiLbBe35gpVuoL7AG818TgBzs9ODiHOpgcItHWkvqt3lFGq07d2l1a/I0uHHXcbgbD8wvxLlahOVMDKEO5Shf2D5R9CpS+K+ZwrsRZv1M+8FN8iBk3iEKuoL75ltLNlh/cx8U7LTO1FT/ssqhVHiAX9FZVrUaOGnsbmK6UOs3azRHr0Om6nITCO0VrbxxXXT2hWjWZaBzwifyKY1r57zUbHxH6dcLQvb6wUFUOwzZptixb+JpHKsxh6dNAPEtWXE3kRcCnyR4ntgOAEyoadItc6V2l0q4HuCRhveakHR2GHcmWK4eVYc2J325ZzzGGLUN4/VCrT3BJ3iU0bGWXOmPj9SZYxm5sYLDkWC6RuALmemFF88Vp00uGQ5u3tX7zVnUf3te95a94ebffmx+V4y1BpI2MNMgYCLWlhsJYbzL+28ss903mQmcseVpvMpqPKwGcuw5//EACMQAQACAgICAgIDAAAAAAAAAAEAESExQVFhcYGhscEQ0fH/2gAIAQEAAT8hLmw8FxEm6xy4wQaJCBaoCOfcBcUrL4IYHM2VvY24lqAgF6HHzHpxWTEwbCdqfkRRalBgCOIvAl9cZdSXiowbeVliB56fuVs7LcPiojU3Mz8bd9wkY11RyuaDt+kRXi9JLgElvF1MQYE1O/cA6iFig8svBssKq/1KXDVCMHG4gA6g17dJhgHTE98wOf6i4DdDSZHcytS5OiX9y2at/CZBcybL1BlCMt/MVuw2twTXZRy+Icy74ECV5G/UJi/QoISqcGOj+474Itx7lsTLwhIMezSlx+ox40szXdSvpLR3NDCN48g8QFgVgl/15hyYbKMywGay0hOCQ4tgNeC4SqaUKiXnJi5f981MHmXddXyRuImFgMYIg6jlAHCDx5lOyJqKcQ4xeR5HRj7jK9Gd3cyYT5mYQEVJgHwnJEoRUxg26IMKVo6OoOiCmwxsQxy0GEFnUA3McUPlXBFFWfSR0oJcQYvlNS/mUBS9AabdVz6jooe9599SvVxzHNBmaYP3CsS4mAVb46giDlZRikdhxqCaQKDqCtLikG21hN4Vy1bNYzn4Kw6y+YDlb4h1YkYz55Yp0zzGqM/xrCxU4jqXQ7Y/asaQoOVHBywIsheJ/9oADAMBAAIAAwAAABDWyRurx33fgrMAcbGkOTurLs2SOhv7OKMOID7/xAAgEQEBAQABBAIDAAAAAAAAAAABABEhMUFRYZGxEHHw/9oACAEDAQE/EHYoCFApy7chnRtgmcZ82MFgD1cbGgMy4RuA9vqQmnMhEVvA6yRDVn9+pKK+fMUMfxDMlla4McQYfUaAhCnaTPKZGz1UFazHxgJ7LakHwTApK6QAv//EAB0RAQEBAQEAAwEBAAAAAAAAAAEAESExEEFRYYH/2gAIAQIBAT8QGNXL3kvdiv8Ak6zxZ+yPPv5GQXS5B4ey12U2QhnZB7ZIbxi6R8F/IC5nLDwv6hsoUAM2A86nH9RfZ+pavXJuD4//xAAjEAEAAgMAAwEBAAIDAAAAAAABABEhMUFRYXGRgaGx0eHx/9oACAEBAAE/EMezSCgDQ3mF6NVz7FAYadd+zUAn5aajkpkEs/sWg41fh7rznUQpt459iCJi9g7gGtF0tluqx/ZcZgwFVrA+LhrU1wZBDhNhPfiJeBqOMCqd1POGeD4IadZbtHrAF566mTIjqhnJ/JZwG6OOmsH9IVfoiXvYY22k+uoisqGg6/DSv8/4jpCToLS6DvL8XKKGE7NqsP4IXvFrCvMYuuA3qF/mJ04Bbz7UCimAanVcip/jKV3CKevKHOM1LcBUtjdjnL+S0xGyDXiHWtjMYrz61O0/lxlUgUHSZorN+ZXCiJeg9yCVnvJcEjEmdPUzvOYV0gbhQ9c0/wDJReoszgBQHr/mXyUwytkpszqFeLrzayr3L3JbmCkGSwq2NBynkvaIdYPeTtDXuYy3CAPkQkORUdn6lpHFkOo2hTVniMgMAgMjlyeqhxHGAFdXW3Sdjm652EyqNqNY6ln5L0iWQJ86fZQsdiD1sSxecZzyPaaEWm7VWxcISPJgP5DKVYrRik973qUaCBsOF6eD5CJqTfkfC9hQVKrQeA5AZ+SpVmhf1j2uVaWb22uWCxOrQLf6lVIWWKLh93CRYpSS0bQLF34tjRWPiDKR2yx/VDrQeYgN4vMQWziLQW7OK343AsMgSB9hFDhiCxbT9ZgoUHdO43CEtHC301MWTNS3Qc1EWg2OWkNXyJSHXDtLYrP7GjOGGmLC/Bacs8wQ8QWEfIiYdc3GOM1fUOZRInkf+4I7mUhJnSfyBWUNcPMHL7JXDJOi8oNVWVq3xGV7Wde4W5v1uFteiWtTi4Gl5R5ou9o0nSppo59zLFgUvb7fcFCapmeXCJ4oEC1nEoO5iOoB46Hvv2YkLIWNid+R79hlNbKJQQgGABQEzV3B1BO2snRNokwgKsV+xJo1CWzEwIebi1PCtEVRHtGTTeHMsST0rgUCy1W2M0Agb0/kulC3Sg6Y6k3eEbWDnJwD+QrJKAJuROkwRYDHKhoE/9k=",
    #         "height": "88",
    #         "width": "87"
    #     }
    #     obj_to_test = processing.prepare_image_payload(obj)
    #     obj['md5'] = "8854b54ffbd1ca18962c3200150a6194"
    #     self.assertEqual(obj, obj_to_test)

if __name__ == '__main__':
    unittest.main()