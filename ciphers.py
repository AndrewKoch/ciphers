import logging
import argparse

import cipher_tests


def one(crib, seed):  # Caesar
    "Takes plaintext and seed and returns ciphertext."

    logger = logging.getLogger()

    logger.info("Received plaintext is %s with a seed of %s", crib, seed)
    ciphertext = ""
    for el in crib:
        ord_el = ord(el) + seed
        ciphertext += chr(ord_el)
    return ciphertext


def two(crib):  # Atbash
    "Takes plaintext of letters and returns ciphertext."
    logger = logging.getLogger()

    logger.info("Received plaintext is %s", crib)
    if not crib.isalpha():
        raise Exception("Letters only.")
    crib = crib.upper()

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
    logger.info("Ciphertext is %s\n", ciphertext)
    return ciphertext


def main(args):
    logger = logging.getLogger()
    log_fmt = "%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s"

    if args.debug:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(level=level, format=log_fmt)
    logger = logging.getLogger()

    if args.run_tests:
        cipher_tests.test_one()
        cipher_tests.test_two()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Set logger level")
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("--run_tests", action="store_true")

    args = parser.parse_args()

    main(args)
