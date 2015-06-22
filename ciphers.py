import logging
import argparse


import utils


class SimpleSubs(object):

    def __init__(self, crib):
        self.crib = utils.format_input(crib)
        self.ciphertext = ""
        self.logger = logging.getLogger()

    def make_alphabet(self):
        return [chr(i) for i in range(65, 91)]

    def encrypt_caesar(self, shift):
        "Applies single shift Caesar Encryption."
        for l in self.crib:
            n = ord(l) + shift
            if n > 90:
                n -= 26
            self.ciphertext += chr(n)

        self.ciphertext = utils.format_output(self.ciphertext)
        self.logger.debug("Ciphertext is %s", self.ciphertext)
        return self.ciphertext

    def encrypt_atbash(self):
        "Applies reverse alphabet to plaintext as Atbash Cipher"
        rev_alpha = self.make_alphabet()[::-1]
        for l in self.crib:
            n = ord(l) - 65
            self.ciphertext += rev_alpha[n]

        self.ciphertext = utils.format_output(self.ciphertext)
        self.logger.debug("Ciphertext is %s", self.ciphertext)
        return self.ciphertext


class Vigenere(object):

    def __init__(self, crib, key):
        self.crib = utils.format_input(crib)
        self._user_key = utils.format_input(key)
        self.ciphertext = ""
        self.logger = logging.getLogger()

    def _make_line(self, seed):
        line = [chr(i) for i in range(65, 91)]
        return line[seed:] + [chr(i) for i in range(65, 65 + seed)]

    def _make_table(self):
        return [self._make_line(i) for i in range(0, 26)]

    def _key_maker(self, key, crib_len):
        key_iters = (crib_len) // len(key)
        key_partial = key[:crib_len % len(key)]

        return (key * key_iters) + key_partial

    def encrypt(self):
        self.table = self._make_table()
        self.logger.debug("Constructed Vigenere table as:\n%s", self.table)

        self.full_key = self._key_maker(self._user_key, len(self.crib))
        self.logger.debug("Full key is %s", self.full_key)

        _coordinates = []
        for i in range(len(self.full_key)):
            _row = ord(self.full_key[i]) - 65
            _col = ord(self.crib[i]) - 65
            _coordinates.append([_row, _col])
        self.logger.debug("Table coordinates are %s", _coordinates)

        for x, y in _coordinates:
            self.ciphertext += self.table[x][y]
        self.ciphertext = utils.format_output(self.ciphertext)

        self.logger.debug("Ciphertext is %s", self.ciphertext)
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
    parser = argparse.ArgumentParser(description="Encryptions")
    parser.add_argument("--debug", action="store_true")

    args = parser.parse_args()

    main(args)
