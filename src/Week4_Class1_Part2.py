class Morse:
    def __init__(self):
        self.__encode_dict__ = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                                'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                                'M': '--',
                                'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                                'U': '..-',
                                'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----',
                                '2': '..---',
                                '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                                '9': '----.',
                                '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
                                '(': '-.--.',
                                ')': '-.--.-',
                                ' ': '   '}
        self.__decode_dict__ = {}
        """Building reverse dictionary"""
        for k, v in self.__encode_dict__.items():
            self.__decode_dict__[v] = k

    def decode(self, encoded):
        decoded = ""
        for e in encoded.split():
            decoded += self.__decode_dict__[e] + ' '
        return decoded

    def encode(self, string):
        encoded = ""
        for e in string:
            encoded += self.__encode_dict__[e.upper()]
        return encoded


morse = Morse()
codificado = morse.encode("Hola Mundo")
print(codificado)
print(morse.decode("... --- ..."))
