import logging
import argparse


def check_validity(crib):
    if not crib.isalpha():
        raise Exception("Letters only.")


def format_input(crib):
    "Removes whitespace, verifies characters are letters, and capitalizes them."
    crib = crib.replace(" ", "")
    check_validity(crib)
    crib = crib.upper()
    return crib


def format_output(ciphertext):
    "Seperates a string into blocks of five characters"
    logger = logging.getLogger()
    logger.debug("Length of ciphertext is %s", len(ciphertext))

    if len(ciphertext) <= 5:
        return ciphertext

    blocks = len(ciphertext) // 5
    logger.debug("Number of blocks: %s", blocks)

    block_index = 5
    blocked_cipher = ciphertext[:5]
    while (block_index / 5) < blocks:
        blocked_cipher += " " + ciphertext[block_index:block_index+5]
        block_index += 5

    if (len(ciphertext) % 5) != 0:
        blocked_cipher += " " + ciphertext[block_index:len(ciphertext)]
    logger.info("Returning blocked ciphertext as %s", blocked_cipher)
    return blocked_cipher


# Simple Substitions
def one(crib, seed):  # Caesar
    "Takes plaintext and seed and returns ciphertext"
    logger = logging.getLogger()
    logger.info("Received plaintext is %s with a seed of %s", crib, seed)
    crib = format_input(crib)

    ciphertext = ""
    for el in crib:
        logger.debug("Plaintext letter is %s", el)

        ord_el = ord(el) + seed
        if ord_el > 90:
            ord_el -= 26
        logger.debug("Unicode integer value is %s", ord_el)

        ciphertext += chr(ord_el)
        logger.debug("Encrypted letter is %s", chr(ord_el))

    logger.info("Ciphertext is %s\n", format_output(ciphertext))
    return format_output(ciphertext)


def two(crib):  # Atbash
    "Takes plaintext of letters and returns ciphertext"
    logger = logging.getLogger()
    logger.info("Received plaintext is %s", crib)
    crib = format_input(crib)

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

    ciphertext = format_output(ciphertext)
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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Set logger level")
    parser.add_argument("--debug", action="store_true")

    args = parser.parse_args()

    main(args)
