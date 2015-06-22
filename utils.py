import logging

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
    logger.debug("Returning blocked ciphertext as %s", blocked_cipher)
    return blocked_cipher
