import unittest

import ciphers


class CipherTests(unittest.TestCase):

    def test_formatter(self):
        self.assertEqual(
            ciphers.format_output("ABCDEFGHIJKLMNOPQRSTUVWYXZ"),
            "ABCDE FGHIJ KLMNO PQRST UVWYX Z")

    def test_one(self):
        self.assertEqual(
            ciphers.one("CallmeCaesar", 13), "PNYYZ RPNRF NE")
        self.assertEqual(
            ciphers.one("Tomorrow we march on Carthage", 1),
            "UPNPS SPXXF NBSDI PODBS UIBHF")

    def test_two(self):
        self.assertEqual(ciphers.two("abc"), "ZYX"),
        self.assertEqual(ciphers.two("zyx"), "ABC")
        self.assertEqual(ciphers.two("AlephTavBethShin"), "ZOVKS GZEYV GSHSR M")
        with self.assertRaises(Exception):
            self.assertEqual(ciphers.two("ab3"))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
