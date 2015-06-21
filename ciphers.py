import logging
import argparse


import utils


class SimpleSubs(object):

    def __init__(self, crib):
        self.crib = utils.format_input(crib)
        self.ciphertext = ""

        self.logger = logging.getLogger()

    def encrypt_caesar(self, shift):
        "Applies single shift Caesar Encryption."
        for l in self.crib:
            n = ord(l) + shift
            if n > 90:
                n -= 26
            self.ciphertext += chr(n)

        self.logger.info("Ciphertext is %s", self.ciphertext)
        self.ciphertext = utils.format_output(self.ciphertext)
        return self.ciphertext

    def encrypt_atbash(self):
        pass


def two(crib):  # Atbash
    "Takes plaintext of letters and returns ciphertext"
    logger = logging.getLogger()
    logger.info("Received plaintext is %s", crib)
    crib = utils.format_input(crib)

    ciphertext = ""
    for el in crib:
        if el <= "n":
            logger.debug("Plaintext letter is %s", el)

            shift = ((ord("M") - ord(el)) * 2 + 1)
            logger.debug("Shift is %s", shift)

            ord_el = ord(el) + shift
            logger.debug("Unicode integer value is %s", ord_el)

            logger.debug("Encrypted letter is %s", chr(ord_el))
            ciphertext += chr(ord_el)

        elif el >= "M":
            logger.debug("Plaintext letter is %s", el)

            shift = ((ord(el) - ord("N")) * 2 + 1)
            logger.debug("Shift is %s", shift)

            ord_el = ord(el) - shift
            logger.debug("Unicode integer value is %s", ord_el)

            logger.debug("Encrypted letter is %s", chr(ord_el))
            ciphertext += chr(ord_el)

    ciphertext = utils.format_output(ciphertext)
    logger.info("Ciphertext is %s\n", ciphertext)
    return ciphertext


# Polyalphabetic substitution
class Vigenere(object):
    def __init__(self, crib, key):
        self.crib = utils.format_input(crib)
        self._user_key = utils.format_input(key)
        self.ciphertext = ""
        self.logger = logging.getLogger()

    def __repr__(self):
        return self.ciphertext

    def make_line(self, seed):
        line = [chr(i) for i in range(65, 91)]
        return line[seed:] + [chr(i) for i in range(65, 65 + seed)]

    def _make_table(self):
        return [self.make_line(i) for i in range(0, 26)]

    def _key_maker(self, key, crib_len):
        self._key_iters = (crib_len) // len(key)
        self._key_partial = key[:crib_len % len(key)]

        return (key * self._key_iters) + self._key_partial

    def encrypt(self):
        self.table = self._make_table()
        self.logger.debug("Constructed Vigenere table as:\n%s", self.table)

        self.full_key = self._key_maker(self._user_key, len(self.crib))
        self.logger.info("Full key is %s", self.full_key)

        self._coordinates = []
        for i in range(len(self.full_key)):
            self._row = ord(self.full_key[i]) - 65
            self._col = ord(self.crib[i]) - 65
            self._coordinates.append([self._row, self._col])
        self.logger.debug("Table coordinates are %s", self._coordinates)

        for x, y in self._coordinates:
            self.ciphertext += self.table[x][y]
        self.ciphertext = utils.format_output(self.ciphertext)

        self.logger.info("Ciphertext is %s", self.ciphertext)
        return self.ciphertext


def main(args):
    log_fmt = "%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s"

    if args.debug:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(level=level, format=log_fmt)
    logger = logging.getLogger()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Set logger level")
    parser.add_argument("--debug", action="store_true")

    args = parser.parse_args()

    main(args)
