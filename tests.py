from number_formatter import NumberFormatter, ValueTooSmallError, DecimalError, ValueTooLargeError
import unittest


class NumberFormatterTest(unittest.TestCase):

    def test_parse_int_common_negative(self):
        self.assertEqual(NumberFormatter("-12345").parse_int(), -12345)

    def test_parse_int_common_positive(self):
        self.assertEqual(NumberFormatter("+198545").parse_int(), 198545)

    def test_parse_int_decimal_error_raises(self):
        with self.assertRaises(DecimalError):
            NumberFormatter("-1.2")

    def test_parse_int_value_too_small_error_raises(self):
        with self.assertRaises(ValueTooSmallError):
            NumberFormatter(" ")

    def test_parse_int_empty_string_raises(self):
        with self.assertRaises(ValueTooSmallError):
            NumberFormatter("")

    def test_parse_int_common_string(self):
        self.assertEqual(NumberFormatter("kkkk").parse_int(), 0)

    def test_parse_int_value_too_large_error_raises(self):
        class MockedString(str):
            def __len__(self):
                return 2**32

        with self.assertRaises(ValueTooLargeError):
            NumberFormatter(MockedString())


if __name__ == "__main__":
    unittest.main()
