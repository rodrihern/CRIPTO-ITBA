# Instrucciones para Criptografia y Seguridad

Estas instrucciones aplican en `/Users/rodri/ITBA/cripto` cuando el usuario pida resolver ejercicios o editar los scripts de `codigos/`.

No son las mismas convenciones que `../metodos`: aca cada cifrado tiene funciones separadas para cifrar y descifrar, y el script se puede importar desde otro.

## Scripts

Los scripts se corren desde `/Users/rodri/ITBA/cripto`.

| Cifrado | Archivo | Funciones | Argumentos principales |
|---|---|---|---|
| Vigenere | `codigos/vigenere.py` | `vigenere_encrypt`, `vigenere_decrypt`, `vigenere_estimate_key_length`, `vigenere_crack` | `-t`, `-k`, `-d`, `-l`, `-v` |

## Convenciones para codigo nuevo

- Usar `argparse` para argumentos CLI.
- Ordenar el archivo siempre igual, de arriba hacia abajo:
  1. `import`s.
  2. Parametros editables (defaults) en mayusculas: `TEXT`, `KEY`, `KEY_LENGTH`, etc.
  3. `<cifrado>_encrypt(plain_text, key, ...)`.
  4. `<cifrado>_decrypt(cipher_text, key, ...)`.
  5. Si el cifrado se puede atacar: `<cifrado>_estimate_key_length(cipher_text, ...)` y `<cifrado>_crack(cipher_text, key_length, ...)`, que devuelve `(key, plain_text)`.
  6. Helpers locales (por ejemplo `shift`, o el nucleo comun que usan encrypt y decrypt).
  7. `parse_args()`.
  8. `main()`.
  9. `if __name__ == "__main__": main()`.
- Nombres en ingles: `encrypt` / `decrypt` (no `encript` / `decript`). Prefijo con el nombre del cifrado: `caesar_encrypt`, `vigenere_decrypt`.
- `encrypt` y `decrypt` son funciones publicas separadas aunque compartan un helper interno. Asi otro script (por ejemplo un ataque) puede hacer `from vigenere import vigenere_decrypt`.
- Nada se ejecuta a nivel de modulo salvo las constantes: todo pasa dentro de `main()`, detras del guard `__main__`.
- `main()` decide el modo y llama a la funcion correspondiente. Las funciones de cifrado no leen `args` ni imprimen el resultado; lo devuelven.
- Por defecto el script cifra; `-d` / `--decrypt` descifra. No hay flag de cifrar.
- Modos de descifrado segun lo que se pase:
  - `-d -k KEY`: descifra con la clave.
  - `-d -l N`: adivina una clave de largo `N` y descifra (`<cifrado>_crack`).
  - `-d` solo: estima el largo (`<cifrado>_estimate_key_length`) y despues adivina la clave.
  - Cifrar sin `-k` es error. `-l` solo vale con `-d` y sin `-k`.
- Cuando la clave se adivina, imprimir `clave: <key>` antes del texto descifrado.
- Los parametros editables son los defaults de `argparse`, para que el script funcione tanto editando el archivo como pasando argumentos.
- Agregar `-v` / `--verbose` para mostrar la tabla paso a paso. Sin `-v`, imprimir solamente el resultado.
- Tablas de ancho fijo con f-strings, alineadas a la izquierda:

```python
print(f"{'i':<3} | {'in':<3} | {'k':<3} | {'out':<3}")
```

- Validar la entrada con `parser.error(...)` (por ejemplo: texto y clave solo con letras `a-z`). Normalizar a minusculas antes de validar.

## Verificacion de codigo nuevo

Despues de crear o editar un script:

- Cifrar un vector de prueba conocido y confirmar el resultado (Vigenere: `attackatdawn` + `lemon` -> `lxfopvefrnhr`).
- Descifrar ese resultado y confirmar que vuelve al texto original.
- Probar con y sin `-v`.
- Probar una entrada invalida y confirmar que sale un mensaje corto sin traceback.

## Como correr los scripts

Vigenere, cifrar:

```bash
python3 codigos/vigenere.py -t attackatdawn -k lemon
```

Vigenere, descifrar con tabla:

```bash
python3 codigos/vigenere.py -d -t lxfopvefrnhr -k lemon -v
```

Vigenere, adivinar la clave sabiendo el largo:

```bash
python3 codigos/vigenere.py -d -t <cipher> -l 5
```

Vigenere, adivinar la clave sin informacion:

```bash
python3 codigos/vigenere.py -d -t <cipher>
```
