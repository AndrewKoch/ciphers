import unittest
import logging
import argparse


import enigma


class EnigmaTests(unittest.TestCase):

    def setUp(self):
        self.logger = logging.getLogger()

    def test_initialization_vector(self):
        self.logger.info("Moving rotors to their initial position")
        e = enigma.Enigma(rotor_ids=["i", "ii", "iii"], rotor_key="ABC")
        e.build_machine()
        self.assertEquals(
            e.rotors, {'i': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
                       'ii': 'JDKSIRUXBLHWTMCQGZNPYFVOEA',
                       'iii': 'FHJLCPRTXVZNYEIWGAKMUSQOBD'
                       })

    def test_single_rotor(self):
        self.logger.info("Testing the wiring of a single rotor")
        # self.assertEquals()

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
    itersuite = unittest.TestLoader().loadTestsFromTestCase(EnigmaTests)
    runner.run(itersuite)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Set logger level")
    parser.add_argument("--debug", action="store_true",
                        help="Sets logging to debug")
    parser.add_argument("--no_log", action="store_true",
                        help="Turns off all logging")

    args = parser.parse_args()

    main(args)
