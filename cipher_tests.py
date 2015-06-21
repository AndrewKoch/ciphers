import unittest

import ciphers


class CipherTests(unittest.TestCase):

    def test_one(self):
        self.assertEqual(
            ciphers.one("CallmeCaesar", 13), "PNYYZRPNRFNE")
        self.assertEqual(
            ciphers.one("Tomorrow we march on Carthage", 1),
            "UPNPSSPXXFNBSDIPODBSUIBHF")

    def test_two(self):
        self.assertEqual(ciphers.two("abc"), "ZYX"),
        self.assertEqual(ciphers.two("zyx"), "ABC")
        self.assertEqual(ciphers.two("AlephTavBethShin"), "ZOVKSGZEYVGSHSRM")
        with self.assertRaises(Exception):
            self.assertEqual(ciphers.two("ab3"))

if __name__ == '__main__':
    unittest.main()
