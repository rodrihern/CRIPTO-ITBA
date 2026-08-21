# Introduccion

Criptografia = escritura secreta 

## Criptosistema

Se usan dos funciones:
- una para cifrar/encriptar
- una para desencriptar

![](attachments/Pasted%20image%2020260808115239.png)

**Ejemplo:** hola -> asljkdgbnlaksjdhflasdj -> hola

### Clave

Bloque arbitrario de informacion que vamos a *presuponer que esta protegida*

>[!Principio de Kerckhoffs]
El sistema debe ser seguro incluso si se conoce *todo* sobre el sistema menos la *clave
### Funcion de cifrado

$$
Mensaje \times clave \rightarrow mensaje\ cifrado
$$
$$
 e(k, p) = e_k(p) = enc_k(p) = \{p\}_k = c
$$


### Funcion de descifrado

$$
Mensaje\ cifrado \times clave \rightarrow mensaje\ cifrado
$$
$$
d(c, k) = d_k(c) = dec_k(c) = \{c\}^{-1} = p
$$
### Uso basico

La idea es que un mensaje cifrado no tenga valor alguno y que cualquiera que lo vea no le sirva, entonces lo puedo transferir por cualquier medio

La idea es poder controlar quien puede acceder a la información

### Ejemplos

#### Cifrado por rotacion

Podemos tener un alfabeto y desfazar las letras

por ejemplo $e('prueba', 4) = 'tvyife'$

**Debilidad:** hay pocas claves -> se puede sacar por fuerza bruta

igual para un ataque por fuerza bruta tengo que poder saber si el resultado tiene sentido, si por ejemplo me cifran con esto un mensaje de 1 letra, no tengo forma de saber que letra era la original por mas que lo haga por fuerza bruta.

#### Cifrado por sustitucion

Reemplaza un simbolo por otro del alfabeto

**Debilidad**: preserva la distribucion estadistica del lenguaje original, tipo la 'a' y la 'e' son las que más aparecen. Con heuristicas lo podes sacar, hasta un nene jugando en una revista lo saca

#### Cifrado Vigenere

Tenemos una clave numerica que nos dice cuanto hay que rotar a cada simbolo, y se repite

![](attachments/Pasted%20image%2020260808142922.png)

La e **no** termina en un mismo simbolo

Para atacarlo se busca separar en los bloques (sacar la longitud de la clave) y una vez lo tengo separado en bloques ahi probar. Para ello buscamos patrones que se repiten (suponemos que pasa cuando la misma palabra cayo en el mismo lugar del bloque), nos fijamos cada cuanto aparecen y sacamos el mcd de esas distancias. Tambien podemos mirar todos en la posicion $i$ del bloque y puedo ver la estadistica porque ahi si mantienen la distribucion estadistica del lenguaje. De base que entre mas largo es el mensaje, mas data para descifrarlo hay. Medio que sacando la longitud del bloque y fijandome en la posicion $i$ dentro del bloque, ahi tengo una de rotacion

#### Sustitucion polialfabetica

Como la de la maquina enigma, son los de rotores. Es un quilombo pero cada rotor mapea un simbolo con otro y van rotando, la letra pasa por todos los rotores (por la mecanica de la maquina la hacian ida y vuelta)

![](attachments/Pasted%20image%2020260808143909.png)

Como en la segunda guerra lo crackearon con la primera computadora fue corte -> uy esto no es tan seguro como pensabamos... Hay que pensar de vuelta la criptografia. (Medio algo parecido a lo de las computadoras cuanticas xd)

### Definicion moderna

Es uan terna de algoritmos:

| Algoritmo                       | Funcion            |
| ------------------------------- | ------------------ |
| Gen: $() \rightarrow K$         | generador de clave |
| Enc: $K \times P \rightarrow C$ | cifrado            |
| Dec: $K \times C \rightarrow P$ | descifrado         |

tal que para todo $m$ y $k$ validos: $d_k(e_k(m)) = m$

- K conjunto de claves
- P conjunto de mensajes posibles
- C conjunto de mensajes cifrados

## Seguridad

El criptosistema **secreto perfecto** sipara toda distribucion de probabilidades en M, cada mensaje $m$ y cada mensaje cifrado $c$ tal que $P(C = c) > 0$:
$$
P(M=m | C=c) = P(M=m)
$$

osea que conocer el texto cifrado no me da mas informacion de $m$

>[!note]
>**La paradoja del secreto perfecto:**
>Notar que $c=e_k(m)$, asi que las variables aleatorias discretas C y M son dependientes. Sin embargo, la propiedad de secreto perfecto interpretada probabilisticamente dice que son VAD independientes

