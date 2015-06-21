import unittest
import logging
import argparse


import ciphers
import utils


class CipherTests(unittest.TestCase):

    def setUp(self):
        self.logger = logging.getLogger()

    def test_formatter(self):
        self.logger.info("Testing the output formatter")
        self.assertEqual(
            utils.format_output("ABCDEFGHIJKLMNOPQRSTUVWYXZ"),
            "ABCDE FGHIJ KLMNO PQRST UVWYX Z")

    def test_caeser(self):
        self.logger.info("Testing the Caeser Cipher")

        caesar_one = ciphers.SimpleSubs("Tomorrow we march on Carthage")
        self.assertEqual(
            caesar_one.encrypt_caesar(1),
            "UPNPS SPXXF NBSDI PODBS UIBHF")

        caesar_two = ciphers.SimpleSubs("Call me Caesar")
        self.assertEqual(
            caesar_two.encrypt_caesar(13), "PNYYZ RPNRF NE")

    def test_atbash(self):
        self.logger.info("Testing the Atbash Cipher")
        self.assertEqual(ciphers.two("abc"), "ZYX"),
        self.assertEqual(ciphers.two("zyx"), "ABC")
        self.assertEqual(ciphers.two("AlephTavBethShin"), "ZOVKS GZEYV GSHSR M")
        with self.assertRaises(Exception):
            self.assertEqual(ciphers.two("ab3"))

    def test_vigenere(self):
        self.logger.info("Testing the Vigenere Cipher")

        vigenere_one = ciphers.Vigenere("ATTACKATDAWN", "AMERICA")
        self.assertEqual(vigenere_one.encrypt(), "AFXRK MATPE NV")

        vigenere_two = ciphers.Vigenere("ALLIESHAVEOURCODE", "PXYZNL")
        self.assertEqual(vigenere_two.encrypt(), "PIJHR DWXTD BFGZM CR")

        vigenere_three = ciphers.Vigenere("Hello World", "pizza time")
        self.assertEqual(vigenere_three.encrypt(), "WMKKO PWDPS")


def main(args):
    log_fmt = "%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s"

    if args.debug:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(level=level, format=log_fmt)
    logger = logging.getLogger()

    # Turns off logging
    if args.no_log:
        logger.disabled = True

    # For custom argparsing, equal to unittest.main()
    runner = unittest.TextTestRunner()
    itersuite = unittest.TestLoader().loadTestsFromTestCase(CipherTests)
    runner.run(itersuite)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Set logger level")
    parser.add_argument("--debug", action="store_true",
                        help="Sets logging to debug")
    parser.add_argument("--no_log", action="store_true",
                        help="Turns off all logging")

    args = parser.parse_args()

    main(args)
