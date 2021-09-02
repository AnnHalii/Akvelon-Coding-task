MIN_LIMIT_NUMBER = 2
MAX_LIMIT_NUMBER = 2 ** 32 - 1
ASCII_ZERO_CODE = 48


class BaseError(Exception):
    pass


class ValueTooSmallError(BaseError):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(BaseError):
    """Raised when the input value is too large"""
    pass


class DecimalError(BaseError):
    """Raised when the input value is decimal"""
    pass


class NumberFormatter:

    def __init__(self, string):
        self.string = string
        self.string_len = len(string)
        self.validate()

    def validate(self):
        """Checks the valid of a string"""
        if not self.string_len >= MIN_LIMIT_NUMBER:
            raise ValueTooSmallError("This value is too small")
        if self.string_len > MAX_LIMIT_NUMBER:
            raise ValueTooLargeError("This value is too large")
        if '.' in self.string:
            raise DecimalError

    def parse_int(self):
        counter, number = 0, 0
        sign = 1
        """Advance through whitespaces until another character is encountered"""
        while counter < self.string_len and self.string[counter] == ' ':
            counter += 1

        """Check signs"""
        if counter < self.string_len and self.string[counter] == '-':
            sign = -1
            counter += 1
        elif counter < self.string_len and self.string[counter] == '+':
            counter += 1

        """Check for valid characters"""
        while counter < self.string_len:
            d = ord(self.string[counter]) - ASCII_ZERO_CODE
            if 0 <= d < 10:
                number = (number * 10) + d
            else:
                break
            counter += 1
        return number * sign


if __name__ == "__main__":
    formatter = NumberFormatter("-1234")
    print(formatter.parse_int())
