import unittest
import exchange_rate_helper

class TestExchangeRateHelper(unittest.TestCase):

    def test_get_all_rates(self):
        rates = exchange_rate_helper.getAllExchangeRates()
        expectedNumberOfRates = len(exchange_rate_helper.getSupportedCurrencies())
        actualNumberOfRates = len(rates)
        self.assertEqual(expectedNumberOfRates, actualNumberOfRates)

    def test_get_unsupported_currency_throws_exception(self):
        with self.assertRaises(ValueError):
            rates = exchange_rate_helper.getExchangeRatesForCurrency("YUAN")

    def test_rates_for_currency_returns_expected_number_of_items(self):
        rates = exchange_rate_helper.getExchangeRatesForCurrency("NGN")
        expectedNumberOfRates = len(exchange_rate_helper.getSupportedCurrencies()) - 1
        actualNumberOfRates = len(rates)
        self.assertEqual(expectedNumberOfRates, actualNumberOfRates)