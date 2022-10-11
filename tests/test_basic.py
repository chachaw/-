import unittest

from app.checkers.user import register_params_check


class BasicTestCase(unittest.TestCase):
    '''
    TODO: 在这里补充注册相关测试用例
    '''

    def test_accept(self):
        accept = {
            "username": "aaaa11",
            "password": "a1B2c3---",
            "nickname": "114514",
            "url": "https://114514.com",
            "mobile": "+86.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(accept), ("ok", True))

    def test_username(self):
        no_uname = {
            "password": "a1B2c3---",
            "nickname": "114514",
            "url": "https://114514.com",
            "mobile": "+86.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(no_uname), ("username", False))
        not_match = {
            "username": "aaa-11",
            "password": "a1B2c3---",
            "nickname": "114514",
            "url": "https://114514.com",
            "mobile": "+86.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(not_match), ("username", False))
        too_short = {
            "username": "aaa1",
            "password": "a1B2c3---",
            "nickname": "114514",
            "url": "https://114514.com",
            "mobile": "+86.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(too_short), ("username", False))
        too_long = {
            "username": "aaa1123123123123123211",
            "password": "a1B2c3---",
            "nickname": "114514",
            "url": "https://114514.com",
            "mobile": "+86.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(too_long), ("username", False))

    def test_password(self):
        no_passwd = {
            "username": "aaaa11",
            "nickname": "114514",
            "url": "https://114514.com",
            "mobile": "+86.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(no_passwd), ("password", False))
        not_match = {
            "username": "aaaa11",
            "password": "a1B2c3---!@",
            "nickname": "114514",
            "url": "https://114514.com",
            "mobile": "+86.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(not_match), ("password", False))
        too_short = {
            "username": "aaaa11",
            "password": "a1B2c3-",
            "nickname": "114514",
            "url": "https://114514.com",
            "mobile": "+86.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(too_short), ("password", False))
        too_long = {
            "username": "aaaa11",
            "password": "a1B2c3---asdadasdasdasd",
            "nickname": "114514",
            "url": "https://114514.com",
            "mobile": "+86.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(too_long), ("password", False))
        no_upper = {
            "username": "aaaa11",
            "password": "a1b2c3---",
            "nickname": "114514",
            "url": "https://114514.com",
            "mobile": "+86.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(no_upper), ("password", False))
        no_lower = {
            "username": "aaaa11",
            "password": "A1B2C3---",
            "nickname": "114514",
            "url": "https://114514.com",
            "mobile": "+86.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(no_lower), ("password", False))
        no_number = {
            "username": "aaaa11",
            "password": "aabccC---",
            "nickname": "114514",
            "url": "https://114514.com",
            "mobile": "+86.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(no_number), ("password", False))
        no_symbol = {
            "username": "aaaa11",
            "password": "a1b2c3AAA",
            "nickname": "114514",
            "url": "https://114514.com",
            "mobile": "+86.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(no_symbol), ("password", False))

    def test_nickname(self):
        no_nickname = {
            "username": "aaaa11",
            "password": "a1b2c3-AAA",
            "url": "https://114514.com",
            "mobile": "+86.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(
            no_nickname), ("nickname", False))

    def test_no_url(self):
        no_url = {
            "username": "aaaa11",
            "password": "a1b2c3-AAA",
            "nickname": "114514",
            "mobile": "+86.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(no_url), ("url", False))

    def test_url_not_match_https(self):
        not_match_https = {
            "username": "aaaa11",
            "password": "a1B2c3---",
            "nickname": "114514",
            "url": "https1://114514.com",
            "mobile": "+86.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(
            not_match_https), ("url", False))

    def test_url_not_match_http(self):
        not_match_http = {
            "username": "aaaa11",
            "password": "a1B2c3---",
            "nickname": "114514",
            "url": "http1://114514.com",
            "mobile": "+86.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(not_match_http), ("url", False))

    def test_url_too_long(self):
        too_long = {
            "username": "aaaa11",
            "password": "a1B2c3---",
            "nickname": "114514",
            "url": "http:// \
                1145141919810364364114514191981036436411451419.com",
            "mobile": "+86.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(too_long), ("url", False))

    def test_url_no_dot(self):
        no_dot = {
            "username": "aaaa11",
            "password": "a1B2c3---",
            "nickname": "114514",
            "url": "http:// \
                1145141919810364364114514191981036436411451419com",
            "mobile": "+86.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(no_dot), ("url", False))

    def test_url_part_error(self):
        have_none = {
            "username": "aaaa11",
            "password": "a1B2c3---",
            "nickname": "114514",
            "url": "http://1145141919810..com",
            "mobile": "+86.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(have_none), ("url", False))
        __first = {
            "username": "aaaa11",
            "password": "a1B2c3---",
            "nickname": "114514",
            "url": "http://-1145141919810.com",
            "mobile": "+86.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(__first), ("url", False))
        __end = {
            "username": "aaaa11",
            "password": "a1B2c3---",
            "nickname": "114514",
            "url": "http://1145141919810-.com",
            "mobile": "+86.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(__end), ("url", False))
        no_match_symbol = {
            "username": "aaaa11",
            "password": "a1B2c3---",
            "nickname": "114514",
            "url": "http://114514###1919810.com",
            "mobile": "+86.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(
            no_match_symbol), ("url", False))

    def test_end_of_numbers(self):
        end_of_numbers = {
            "username": "aaaa11",
            "password": "a1B2c3---",
            "nickname": "114514",
            "url": "http://1145141919810.114",
            "mobile": "+86.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(end_of_numbers), ("url", False))

    def test_mobile(self):
        no_mobile = {
            "username": "aaaa11",
            "password": "a1B2c3---",
            "nickname": "114514",
            "url": "http://1145141919810.com",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(no_mobile), ("mobile", False))
        no_plus = {
            "username": "aaaa11",
            "password": "a1B2c3---",
            "nickname": "114514",
            "url": "http://1145141919810.com",
            "mobile": "86.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(no_plus), ("mobile", False))
        less_2_numbers = {
            "username": "aaaa11",
            "password": "a1B2c3---",
            "nickname": "114514",
            "url": "http://1145141919810.com",
            "mobile": "+8.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(
            less_2_numbers), ("mobile", False))
        more_2_numbers = {
            "username": "aaaa11",
            "password": "a1B2c3---",
            "nickname": "114514",
            "url": "http://1145141919810.com",
            "mobile": "+863.114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(
            more_2_numbers), ("mobile", False))
        no_dot = {
            "username": "aaaa11",
            "password": "a1B2c3---",
            "nickname": "114514",
            "url": "http://1145141919810.com",
            "mobile": "+86114514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(no_dot), (
            "mobile", False))
        less_12_numbers = {
            "username": "aaaa11",
            "password": "a1B2c3---",
            "nickname": "114514",
            "url": "http://1145141919810.com",
            "mobile": "+86.11451419198",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(
            less_12_numbers), ("mobile", False))
        more_12_numbers = {
            "username": "aaaa11",
            "password": "a1B2c3---",
            "nickname": "114514",
            "url": "http://1145141919810.com",
            "mobile": "+86.1145141919810",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(
            more_12_numbers), ("mobile", False))
        unexpected_symbols = {
            "username": "aaaa11",
            "password": "a1B2c3---",
            "nickname": "114514",
            "url": "http://1145141919810.com",
            "mobile": "+86.11A514191981",
            "magic_number": 0
        }
        self.assertEqual(register_params_check(
            unexpected_symbols), ("mobile", False))

    def test_magic_number(self):
        accept = {
            "username": "aaaa11",
            "password": "a1B2c3---",
            "nickname": "114514",
            "url": "https://114514.com",
            "mobile": "+86.114514191981",
        }
        self.assertEqual(register_params_check(accept), ("ok", True))

    def test_not_number_mnumber(self):
        not_number = {
            "username": "aaaa11",
            "password": "a1B2c3---",
            "nickname": "114514",
            "url": "https://114514.com",
            "mobile": "+86.114514191981",
            "magic_number": "a"
        }
        self.assertEqual(register_params_check(
            not_number), ("magic_number", False))


"""
    def test_register_params_check(self):
        self.assertEqual(register_params_check(None), ("ok", True))"""


if __name__ == '__main__':
    unittest.main()
