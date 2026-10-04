# Guia 5 - OpenSSL y JCA

## Ejercicio 1

![](attachments/Pasted%20image%2020261004164239.png)

Para listar los algoritmos de cifrado simetrico hacemos

```sh
openssl enc -list
```

Los diferentes algoritmos son:
- aes  
- aria (Algoritmo Coreano, del año 2003)  
- bf (BlowFish)  
- camellia  
- cast  
- chacha20 (es un algoritmo de cifrado de flujo)  
- des  
- idea  
- des3 (triple des)  
- desX (variante de des)  
- rc2 (Rivest Cipher para cifrado de bloque)  
- rc4 (Rivest Cipher para cifrado de flujo)  
- seed (otro algoritmo coreano, del año 1998)  
- sm4 (algoritmo de origen chino, del año 201

Los modos de cifrado de bloque que soporta son:
- ECB
- CBC
- CFB
- OFB (1 y 8)
- CTR

los aes son los siguietnes

```
-aes-128-cbc               -aes-128-cfb               -aes-128-cfb1             
-aes-128-cfb8              -aes-128-ctr               -aes-128-ecb              
-aes-128-ofb               -aes-192-cbc               -aes-192-cfb              
-aes-192-cfb1              -aes-192-cfb8              -aes-192-ctr              
-aes-192-ecb               -aes-192-ofb               -aes-256-cbc              
-aes-256-cfb               -aes-256-cfb1              -aes-256-cfb8             
-aes-256-ctr               -aes-256-ecb               -aes-256-ofb              
-aes128                    -aes128-wrap               -aes128-wrap-pad          
-aes192                    -aes192-wrap               -aes192-wrap-pad          
-aes256                    -aes256-wrap               -aes256-wrap-pad          
-id-aes128-wrap            -id-aes128-wrap-pad        -id-aes192-wrap           
-id-aes192-wrap-pad        -id-aes256-wrap            -id-aes256-wrap-pad 
```

El IV para empezar un cifrado o se pasa como parametro con `-iv` o se deriva junto con la clave a partir de password y el salt.

El salt es un valor aleatorio de 8 bytes que se mezcla con la password. Se usa para que sea **no** deterministico.

Se puede indicar el salt con la opcion `-S` o `-salt <hex>` o si no queremos salt `-nosalt` 

## Ejercicio 2

![](attachments/Pasted%20image%2020261004165205.png)



```sh
echo "basta de mosquitos" | openssl enc -aes-128-cbc -k "reloj" -pbkdf2 -a
```

- `echo "basta de mosquitos" |` → manda el texto plano por stdin a openssl (ojo: `echo` agrega un `\n` al final, que también se cifra).
- `openssl enc` → subcomando de cifrado/descifrado simétrico. Sin `-d` cifra (equivale a `-e`).
- `-aes-128-cbc` → algoritmo AES con clave de 128 bits en modo CBC. Como CBC es de bloque, aplica padding PKCS#7 por defecto.
- `-k "reloj"` → la password desde la que se derivan clave e IV (no es la clave en sí; para pasar la clave directa en hex se usa `-K`, mayúscula).
- `-pbkdf2` → usa PBKDF2 (por defecto con SHA-256 y 10000 iteraciones) como función de derivación clave+IV a partir de password+salt, en vez del viejo `EVP_BytesToKey`, que es más débil y tira un warning de "deprecated key derivation".
- `-a` → codifica la salida en Base64 para que se pueda imprimir en la terminal (sin esto sale binario).

Como no se pasa `-nosalt` ni `-S`, openssl genera un salt aleatorio de 8 bytes y lo guarda al principio de la salida como `Salted__` + salt. Por eso en Base64 el resultado siempre arranca con `U2FsdGVkX1...`.

ciframos 2 veces y vemos que cambia, luego se uso salt. Para que no haya salt usamos `-nosalt`

Asi podemos encriptar y desencriptar y vemos que sale "basta de mosquitos" a la salida

```sh
echo "basta de mosquitos" | openssl enc -aes-128-cbc -k "reloj" -pbkdf2 -a | openssl enc -aes-128-cbc -d -k "reloj" -pbkdf2 -a
```


Ahora ciframos asi en **ecb** y en cbc. vemos que en ecb, como cada bloque se cifra de forma independiente, **bloques iguales cifran cosas iguales**.

```sh
echo "buen diabuen diabuen dia" | openssl enc -aes-128-ecb -e -k "reloj" -pbkdf2
```

## Ejercicio 3

![](attachments/Pasted%20image%2020261004171131.png)

```sh
echo "UU32ReW9vbs3MyoniaxJpRVnhg6sQ805FoAJzqGi63E=" | openssl enc -aes-128-cbc -d -k "margarita" -a -nosalt -pbkdf2
```
 
 y nos da 

```
ya tenemos la tercera
```

Re nenazo escaloneta el que hizo esta guia
## Ejercicio 4

![](attachments/Pasted%20image%2020261004171605.png)

```sh
echo "OLhfDpOmkHFkujdSbLGIpRvVnBINKPJRVjdq5S8NxkTuiu8kS30QoVuzAo9otQwD" | openssl enc -d -aes-128-cbc -K "1234Ax" -iv "AAFF" -a -p
```

el `-p` es para que nos tire el salt, key y iv que se uso. Esta es la salida

```
hex string is too short, padding with zero bytes to length
hex string is too short, padding with zero bytes to length
salt=0700000000000000
key=1234A000000000000000000000000000
iv =AAFF0000000000000000000000000000
por ahora es fácil Criptografia
```

Podemos observar que una clave y el iv son de 16 bytes. 

## Ejercicio 5

![](attachments/Pasted%20image%2020261004172319.png)

Creamos un archivo lleno de 0s

```sh
head -c 1024 /dev/zero > ceros.txt
```

ahora los encriptamos con cada clavve y vemos que los resultados

```sh
openssl enc -in ceros.txt -aes-128-cbc -k "holamanola" -pbkdf2 -a
```

y la salida

```
U2FsdGVkX1+rtGYqHYZTxPlT9WF1PEDxmF4v4Y89WuUiaY+gelIKYEA6cgvpl8hJ
6WctY6AVAJkqKqodJXjCTkCFADSK1F3d2o7QcjelVVQWcde+wsWmATDdvvfpIVGq
LATA5MJOMDa4PUvWINFDpmXbhQw3Mt3gcM3UWTXE9NdblTDofXmWuz8IBvCrcMVx
aDTsOL5WEQTG0tVfzRX3PEo64Oeh1UajkjtFjKt69EpecwSXmgaRnqiFXiEd8prm
JWwXxv4mbRYmNu4ZzBuQ2R6Td99ujVLlA70vC0Mx/t5RSbBao9xZAIi53WwpzCOo
uLXvY5kFcuesIERrAFug2yxMyia3CEGpXC4kHCKGx3leyrHRy7EBTuUPCCG5Rjuh
zYo1rqnsKAmMWPyAjKbQDPqnxOfhfAzJzNzkoI4cNOCJhO/6hYRXsTFMM+SEG17C
BxrM6vrdpoY3l1l9NYkjf5A1BHc1BxYbGzpnTlTt1COx/bv5AOzTffNuGFgrvDMB
k3yPJImYfwLpOh6JGS01t9Z7UabTKf9bcrf0HHtYs5QYCIWh7DP6CEDRB364Obhk
yXMiDoFgJdhADBZVjEWU2tms+1k58Y7VB70QeUIsQXyByScf+/ED0BR2y2+eHM22
zQtWMF0E0CRhvd3Di/0QH84VWugQ1cab6Zp4449GorJqHxLT4DewbBBdppKXcJda
Z2o0+cs7dZsajAYbFMYGPgfKC1MRgk07xIMGsQIJvRLIf51Av2xKdEIZT0DWfX1l
wOR8439m2/KaHCzxSkteehJSQV1flM1GrAtJdSonu0TUp/mjTJMFGDEdSeAOsArR
Aaju71EXc9SYOmixvBdy91ewRtjArCnxWeoWJooaDpeSu+/W5kVbl4c8xduSLOYY
U1PS7fZMoOQWWw/ohEXmTvOM6vBN/fNO+kErONSmxpJeLzAFK6uTO0cDA1axc/88
H8WDnX7Ypr6X6V/UsWnjhxtzBOSDiV1HQDu/25ooCBO6M2BwX4WJU7sbcD+8PgA1
rrCsTa9wHw3MXoq1JJmxMXbXc7uQgScs9zzte/1S8lHw3QO/hLoKtLyQzaNU5zsX
tzZi97Xd6V74ySRCtEQsirdDTXWwxBT4B3xM5mmBchIusqlfktWzeFOlEMe8/qDc
fwgmZl8D6FZbdck7LWfg0hPncndo034yT2NZaKVK2pTZIlvhPRzsIGCtp8awcWT1
uIGPOWq5BAufvz1ah60Bo8ycFe2IcWd4MJiD+CWOA4zz4WQyqlU91SzVAkSrfU4m
WtFVneU2g0Pg5Vz7sIi7H1YgZPciMiRijp1S9FG9F/ADnJuW2AGHg9/vTfswBxzP
f80V94rv+zlC2UIhPuPrgu5DKYVw0B7cBNeEB27JCSwOhn2NzcpkIkRU6Y46YSBZ
```

Parece todo ok, veamos que onda con ecb

```sh
openssl enc -in ceros.txt -aes-128-ecb -k "holamanola" -pbkdf2 -a
```

y la salida

```sh
U2FsdGVkX18GJhgYQr0SI3P3iiDFrDTz//Em1/fuUBpz94ogxaw08//xJtf37lAa
c/eKIMWsNPP/8SbX9+5QGnP3iiDFrDTz//Em1/fuUBpz94ogxaw08//xJtf37lAa
c/eKIMWsNPP/8SbX9+5QGnP3iiDFrDTz//Em1/fuUBpz94ogxaw08//xJtf37lAa
c/eKIMWsNPP/8SbX9+5QGnP3iiDFrDTz//Em1/fuUBpz94ogxaw08//xJtf37lAa
c/eKIMWsNPP/8SbX9+5QGnP3iiDFrDTz//Em1/fuUBpz94ogxaw08//xJtf37lAa
c/eKIMWsNPP/8SbX9+5QGnP3iiDFrDTz//Em1/fuUBpz94ogxaw08//xJtf37lAa
c/eKIMWsNPP/8SbX9+5QGnP3iiDFrDTz//Em1/fuUBpz94ogxaw08//xJtf37lAa
c/eKIMWsNPP/8SbX9+5QGnP3iiDFrDTz//Em1/fuUBpz94ogxaw08//xJtf37lAa
c/eKIMWsNPP/8SbX9+5QGnP3iiDFrDTz//Em1/fuUBpz94ogxaw08//xJtf37lAa
c/eKIMWsNPP/8SbX9+5QGnP3iiDFrDTz//Em1/fuUBpz94ogxaw08//xJtf37lAa
c/eKIMWsNPP/8SbX9+5QGnP3iiDFrDTz//Em1/fuUBpz94ogxaw08//xJtf37lAa
c/eKIMWsNPP/8SbX9+5QGnP3iiDFrDTz//Em1/fuUBpz94ogxaw08//xJtf37lAa
c/eKIMWsNPP/8SbX9+5QGnP3iiDFrDTz//Em1/fuUBpz94ogxaw08//xJtf37lAa
c/eKIMWsNPP/8SbX9+5QGnP3iiDFrDTz//Em1/fuUBpz94ogxaw08//xJtf37lAa
c/eKIMWsNPP/8SbX9+5QGnP3iiDFrDTz//Em1/fuUBpz94ogxaw08//xJtf37lAa
c/eKIMWsNPP/8SbX9+5QGnP3iiDFrDTz//Em1/fuUBpz94ogxaw08//xJtf37lAa
c/eKIMWsNPP/8SbX9+5QGnP3iiDFrDTz//Em1/fuUBpz94ogxaw08//xJtf37lAa
c/eKIMWsNPP/8SbX9+5QGnP3iiDFrDTz//Em1/fuUBpz94ogxaw08//xJtf37lAa
c/eKIMWsNPP/8SbX9+5QGnP3iiDFrDTz//Em1/fuUBpz94ogxaw08//xJtf37lAa
c/eKIMWsNPP/8SbX9+5QGnP3iiDFrDTz//Em1/fuUBpz94ogxaw08//xJtf37lAa
c/eKIMWsNPP/8SbX9+5QGnP3iiDFrDTz//Em1/fuUBpz94ogxaw08//xJtf37lAa
c/eKIMWsNPP/8SbX9+5QGnP3iiDFrDTz//Em1/fuUBpHMm8xt435AfI4XLa5VzyW
```

nefasto, quedo todo igual

## Ejercicio 6

![](attachments/Pasted%20image%2020261004184821.png)

```sh
openssl genrsa -out priv.key 1024
```
## Ejercicio 7

![](attachments/Pasted%20image%2020261004184901.png)

```sh
openssl rsa -in priv.key -out pub.key -pubout
```

Notamos que la longitud de la clave pribada es mucho mas corta que la clave publica. La clave privada contiene informacion para generar la clave publica.

Para ver los contenidos de las claves

```sh
openssl rsa -in priv.key -text
```

```sh
openssl rsa -in pub.key -text -pubin
```

## Ejercicio 9

![](attachments/Pasted%20image%2020261004190045.png)

Cualquiera puede cifrar con mi clave publica asi que eso no da nada de autentificacion. 

## Ejercicio 10

![](attachments/Pasted%20image%2020261004190056.png)

- Con mi clave publica
- No pues solo yo tengo mi clave privada
- no hay confidencialidad pues cualquiera con mi clave publica y puede desencriptarlo
- Se asegura que el que lo escribio soy yo (quien digo ser) osea autenticidad.

## Ejercicio 11

![](attachments/Pasted%20image%2020261004190248.png)

Usamos como documento el pdf de la guia. Primero sacamos el hash con sha1 y lo guardamos en un archivo

```sh
openssl dgst -sha1 -binary -out guia5.sha1 guia5.pdf
```

el `-binary` es para que guarde los 20 bytes del hash crudos y no el texto `SHA1(guia5.pdf)= ...` que tira por defecto. Si no, firmariamos ese texto en vez del hash.

Ahora ciframos el hash con nuestra clave privada

```sh
openssl rsautl -sign -inkey priv.key -in guia5.sha1 -out guia5.sig
```

Tira un warning de que `rsautl` esta deprecado (el nuevo es `pkeyutl`) pero funciona igual. `guia5.sig` es la firma digital, de 128 bytes (lo mismo que la clave de 1024 bits).

Le mandamos al compañero `guia5.pdf`, `guia5.sig` y `pub.key`. Para chequear la firma, él descifra la firma con nuestra clave publica (eso le devuelve el hash que firmamos) y calcula por su cuenta el hash del pdf

```sh
openssl rsautl -verify -pubin -inkey pub.key -in guia5.sig -out recuperado.sha1
```

```sh
openssl dgst -sha1 -binary -out calculado.sha1 guia5.pdf
```

y los compara

```sh
cmp recuperado.sha1 calculado.sha1 && echo "firma valida"
```

Si son iguales sabe que lo mandamos nosotros, porque la firma solo se puede generar con nuestra clave privada y solo nosotros la tenemos. Ademas sabe que el pdf no se modifico en el camino, porque si cambia un solo byte el hash da distinto (integridad).


## Ejercicio 13

![](attachments/Pasted%20image%2020261004190529.png)

para firmar:

```sh
openssl dgst -sha1 -sign priv.key -out salidafirmada archivo.pdf
```

Para verificar:

```sh
openssl dgst -sha1 -verify pub.key -signature salidafirmada archivo.pdf
```

