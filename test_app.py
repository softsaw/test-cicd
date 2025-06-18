import app
import unittest
import exchange_rate_helper

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True
        return super().setUp()
    
    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "Hello World")
    
    def test_get_all_rates(self):
        response = self.app.get('/rates')
        self.assertEqual(response.status_code, 200)
        actual = len(response.json["rates"])
        expected = len(exchange_rate_helper.getAllExchangeRates())
        self.assertEqual(expected, actual)

    def test_get_all_currencies(self):
        response = self.app.get("/currencies")
        self.assertEqual(response.status_code, 200)
        actual = len(response.json["currencies"])
        expected = len(exchange_rate_helper.getAllExchangeRates())
        self.assertEqual(expected, actual)

    def test_get_supported_currency(self):
        response = self.app.get("/rate/NGN")
        self.assertEqual(response.status_code, 200)
        actual = len(response.json["rates"])
        expected = len(exchange_rate_helper.getAllExchangeRates())-1
        self.assertEqual(expected, actual)

    def test_get_unsupported_currency(self):
        response = self.app.get("/rate/CAD")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json["error"], "Unsupported currency provided")

if __name__ == '__main__':
    unittest.main()