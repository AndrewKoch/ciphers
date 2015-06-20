import logging

import ciphers


def main():
    logger = logging.getLogger()
    log_fmt = "%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s"

    level = logging.INFO

    logging.basicConfig(level=level, format=log_fmt)
    logger = logging.getLogger()


def test_one():
    logger = logging.getLogger()

    print "\n***** Testing the first cipher *****\n"

    test_one = ciphers.one("Call me Caesar", 13), "Pnyy zr Pnrfne"
    test_two = ciphers.one("Tomorrow we march on Carthage", 13), "Ecnn og Ecguct"

    if test_one[0] == test_one[1]:
        logger.info("Passed test one: expected %s, got %s", test_one[1], test_one[0])
    else:
        logger.info("Failed test one: expected %s, got %s", test_one[1], test_one[0])
    if test_two[0] == test_two[1]:
        logger.info("Passed test two: expected %s, got %s", test_two[1], test_two[0])
    else:
        logger.info("Failed test two: expected %s, got %s", test_two[1], test_two[0])

def test_two():
    logger = logging.getLogger()

    print "\n***** Testing the second cipher *****\n"

    test_one = ciphers.two("abc"), "ZYX"
    test_two = ciphers.two("zyx"), "ABC"
    test_three = ciphers.two("AlephTavBethShin"), "ZOVKSGZEYVGSHSRM"

    if test_one[0] == test_one[1]:
        logger.info("Passed test one: expected %s, got %s", test_one[0], test_one[1])
    else:
        logger.info("Failed test one: expected %s, got %s", test_one[0], test_one[1])

    if test_two[0] == test_two[1]:
        logger.info("Passed test two: expected %s, got %s", test_two[0], test_two[1])
    else:
        logger.info("Failed test two: expected %s, got %s", test_two[0], test_two[1])

    if test_three[0] == test_three[1]:
        logger.info("Passed test two: expected %s, got %s", test_three[0], test_three[1])
    else:
        logger.info("Failed test two: expected %s, got %s", test_three[0], test_three[1])

    try:
        test_four = ciphers.two("ab3")
    except Exception as e:
        logger.exception(e)
