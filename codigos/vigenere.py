import argparse

# Define parameters
TEXT = "ssuvp"
KEY = "skynet"
DECRYPT = True  # False: cifra TEXT, True: descifra TEXT

LETTERS = 26

def vigenere_method(text, key, decrypt, verbose=False):
    sign = -1 if decrypt else 1
    result = []

    if verbose:
        print(f"{'i':<3} | {'in':<3} | {'k':<3} | {'out':<3}")
        print("-" * 21)

    for i, ch in enumerate(text):
        k = key[i % len(key)]
        out = shift(ch, sign * (ord(k) - ord('a')))
        result.append(out)

        if verbose:
            print(f"{i:<3} | {ch:<3} | {k:<3} | {out:<3}")

    return "".join(result)

def shift(ch, offset):
    return chr((ord(ch) - ord('a') + offset) % LETTERS + ord('a'))

def parse_args():
    parser = argparse.ArgumentParser(description="Cifrado de Vigenere")
    parser.add_argument("-t", "--text", default=TEXT, help="Texto a cifrar o descifrar (solo letras)")
    parser.add_argument("-k", "--key", default=KEY, help="Clave (solo letras)")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("-d", "--decrypt", dest="decrypt", action="store_true", default=DECRYPT, help="Descifra el texto")
    mode.add_argument("-c", "--encrypt", dest="decrypt", action="store_false", help="Cifra el texto")
    parser.add_argument("-v", "--verbose", action="store_true", help="Muestra la tabla letra por letra")
    args = parser.parse_args()

    args.text = args.text.lower()
    args.key = args.key.lower()
    if not (args.text.isascii() and args.text.isalpha()):
        parser.error("--text debe tener solo letras a-z")
    if not (args.key.isascii() and args.key.isalpha()):
        parser.error("--key debe tener solo letras a-z")

    return args





args = parse_args()
result = vigenere_method(args.text, args.key, args.decrypt, args.verbose)

if args.verbose:
    print()
print(result)
