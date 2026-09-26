import argparse

# Define parameters
TEXT = "ssuvp"
KEY = None         # Optional: con -d y sin clave, se adivina la clave
KEY_LENGTH = None  # Optional: con -d y sin clave, si queda en None se estima

LETTERS = 26

def vigenere_encrypt(plain_text, key, verbose=False):
    return apply_key(plain_text, key, 1, verbose)

def vigenere_decrypt(cipher_text, key, verbose=False):
    return apply_key(cipher_text, key, -1, verbose)

def vigenere_estimate_key_length(cipher_text, verbose=False):
    # Devuelve el largo de clave mas probable (int >= 1)
    raise NotImplementedError("vigenere_estimate_key_length")

def vigenere_crack(cipher_text, key_length, verbose=False):
    # Adivina la clave de largo key_length y descifra con ella
    # Devuelve (key, plain_text); para descifrar usar vigenere_decrypt
    raise NotImplementedError("vigenere_crack")

def apply_key(text, key, sign, verbose):
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
    parser.add_argument("-k", "--key", default=KEY, help="Clave (solo letras). Con -d y sin -k, se adivina")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Descifra el texto (por defecto cifra)")
    parser.add_argument("-l", "--key-length", type=int, default=KEY_LENGTH, help="Largo de la clave a adivinar (solo con -d y sin -k). Si no se pasa, se estima")
    parser.add_argument("-v", "--verbose", action="store_true", help="Muestra la tabla letra por letra")
    args = parser.parse_args()

    args.text = args.text.lower()
    if not (args.text.isascii() and args.text.isalpha()):
        parser.error("--text debe tener solo letras a-z")

    if args.key is not None:
        args.key = args.key.lower()
        if not (args.key.isascii() and args.key.isalpha()):
            parser.error("--key debe tener solo letras a-z")
    elif not args.decrypt:
        parser.error("para cifrar hace falta --key")

    if args.key_length is not None:
        if not args.decrypt or args.key is not None:
            parser.error("--key-length solo se usa con -d y sin --key")
        if not 1 <= args.key_length <= len(args.text):
            parser.error("--key-length debe estar entre 1 y el largo del texto")

    return args

def main():
    args = parse_args()

    key = None
    if not args.decrypt:
        result = vigenere_encrypt(args.text, args.key, args.verbose)
    elif args.key is not None:
        result = vigenere_decrypt(args.text, args.key, args.verbose)
    else:
        key_length = args.key_length
        if key_length is None:
            key_length = vigenere_estimate_key_length(args.text, args.verbose)
        key, result = vigenere_crack(args.text, key_length, args.verbose)

    if args.verbose:
        print()
    if key is not None:
        print(f"clave: {key}")
    print(result)

if __name__ == "__main__":
    main()
