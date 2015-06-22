import logging
import argparse


# self.rotor_reflectors = {
#     "a": "EJMZALYXVBWFCRQUONTSPIKHGD",
#     "b": "YRUHQSLDPXNGOKMIEBFZCWVJAT",
#     "c": "FVPJIAOYEDRZXWGCTKUQSBNMHL",
#     "b_thin": "ENKQAUYWJICOPBLMDXZVFTHRGS",
#     "c_thin": "RDOBJNTKVEHMLFCWZAXGYIPSUQ",
#     "etw": "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     }

# use pointers rather than new objects

class Enigma(object):
    "Recreation of the Wehrmacht Naval Enigma, pre-M4."

    def __init__(self, rotor_ids, rotor_key):
        self.rotor_key = rotor_key
        self.rotor_ids = rotor_ids
        self.logger = logging.getLogger()

    def set_rotor_position(self):
        "Sets rotor positions according to the key"
        self.shifts = []
        for l in self.rotor_key:
            self.shifts.append(ord(l) - 65)
        self.logger.debug("Rotor positions are %s", self.shifts)

        i = 0
        for rotor in self.rotors:
            movement = self.rotors[rotor][:self.shifts[i]]
            # print movement
            self.init_vector = self.rotors[rotor][self.shifts[i]:] + movement
            self.rotors[rotor] = self.init_vector
            i += 1
        self.logger.info("Rotors set to %s", self.rotors)

    def build_machine(self):
        "Assembles the entire machine"
        self.build_rotors()
        self.set_rotor_position()

    # def rotor_circuit(self, shift):
    #     return bin(pow(2, 25))

    def build_rotors(self):
        self.rotor_wiring = {
            "i": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
            "ii": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
            "iii": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
            "iv": "ESOVPZJAYQUIRHXLNFTGKDCMWB",
            "v": "VZBRGITYUPSDNHLXAWMJQOFECK",
            "vi": "JPGVOUMFYQBENHZRDKASXLICTW",
            "vii": "NZJHGRCXMYSWBOUFAIVLPEKQDT",
            "viii": "FKQHTLXOCBJSPDZRAMEWNIUYGV",
            }

        self.rotors = {}
        for numeral in self.rotor_ids:
            self.rotors[numeral] = self.rotor_wiring[numeral]
        self.logger.info("Raw rotor wirings are %s", self.rotors)


def main(args):
    log_fmt = "%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s"

    if args.debug:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(level=level, format=log_fmt)
    logger = logging.getLogger()

    e = Enigma(rotor_ids=["i", "ii", "iii"], rotor_key="ABC")
    e.build_machine()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Simulating the Enigma machine")
    parser.add_argument("--debug", action="store_true")

    args = parser.parse_args()

    main(args)
