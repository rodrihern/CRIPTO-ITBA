# Cifrado

> [!cite] Bibliografía de referencia
> Katz, J., & Lindell, Y. (2020). *Introduction to Modern Cryptography* (3.ª ed.). Chapman & Hall/CRC.

3 objetivos:
- disponibilidad de la informacion
- confidecialidad de la informacion
- integridad de la infromacion

>[!note]
>**Principio**: lo unico que se asume privado es la clave. Se asume que el algoritmo sea publico (aunque no lo sea)

## One time pad (OTP)

![](attachments/Pasted%20image%2020260816160018.png)

Cumple el secreto perfecto, pero si se usa mas de una vez la misma clave se pierde el secreto perfecto

![](attachments/Pasted%20image%2020260816161004.png)

Si la clave no es aleatoria uniforme, nos da pistas de que hay mas probabilidades de que el mensaje sea alguno en particular.

>[!important]
>criptosistema con secreto perfecto $\iff$ reducible al OTP


## Seguridad computacional

Es un trade-off, no va a ser secreto perfecto

Hay niveles de seguridad, y segun el nivel, distinta probabilidad de exito para el atacante (there are levels to this shit)

## Generadores pseudoaleatorios

Algoritmos determinisitcos que expanden una entrada llamada *seed* y la salida *parece* aleatoria

![](attachments/Pasted%20image%2020260816162912.png)

## Criptosistemas de flujo

Intercambian la clave del OTP por la salida de un generador pseudoaleatorio

## Pruebas de seguridad

Prueban las caracteristicas de un criptosistema 

prueban a un algoritmo que representa un ataque, se repite muchas veces y lo que interesa ver es la probabilidad de exito del atacante

### Prueba de indistinguibilidad

Eavesdropping Indistinguishability test

Lo unico que tiene acceso el atacante A del criptosistema $\Pi$ es al cifer text
1. A genera $m_0$ y $m_1$ arbitrariamente
2. se genera una clave $k$
3. Se genera $b \in \{0, 1\}$
4. A recibe $c = e_k(m_b)$
5. A emite $b' \in \{0, 1\}$ 

si $b = b'$ A gana

si $P(b=b') = 0.5$ para todo adversario A, tiene secreto perfecto
## Nivel de seguridad

Esta dado por una variable que relaciona la cota en el poder de un adversario y la probabilidad de exito que tendra

![](attachments/Pasted%20image%2020260816164636.png)

$\epsilon$ tiene que ser tan chico que el tiempo de procesamiento con la computacion actual, la idea es que de milenios. 

n es un numero que se asocia a la capacidad de computo

## Multiples cifrados

![](attachments/Pasted%20image%2020260816175133.png)

Los criptosistemas de flujo **NO** son seguros bajo multiples cifrados

## Necesidad de crifado probabilistico

Si una funcion de cifrado es deterministica, **NO** es segura bajo multiples cifrados

## Ataques de texto plano escogido (CPA)

![](attachments/Pasted%20image%2020260816180200.png)

si es deterministico el cifrado, los experimentos anteriores no tienen ningun tipo de sentido. Usa la f(x) esta para saber cual es. Necesitamos una cosa mas piola que agregue un poco mas de aleatoreidad.

Un criptosistema que es CPA-Secure para un tamaño limitado de mensajes (de hasta n bits) lo podemos extender arbitrariamente.
## Evitar reutilizar la clave

>[!important]
Si un criptosistema es CPA secure para un mensaje, tambien lo es para multiples mensajes
>

*nonce*: numeros que se usan una sola vez.

Se usa un nonce (IV: valor inicial). este junto con k, generan la seed, luego la seed nunca es la misma porque IV nunca es el mismo. Este IV se comparte, podria hasta ser un contador

![](attachments/Pasted%20image%2020260816191715.png)

## Extension y encadenamiento

>[!Definition] Primitivas de cifrado en bloque
>Estan definidas para mensajes de tamaño fijo, son funciones pseudoaleatorias que podria usarse como criptosistema pero son deterministicas. Pero lo bueno es que las podemos combinar

La idea basica es que dividimos el mensaje en bloques y a cada bloque le usamos este sistema, si el largo del mensaje no es multiplo del tamaño del bloque, agregamos *padding*

![](attachments/Pasted%20image%2020260816192204.png)

## Tipos de encadenamiento

### ECB

Trata al mensaje original como un conjunto de bloques independientes

![](attachments/Pasted%20image%2020260816192257.png)

### CBC

Utiliza la salida de un bloque como entrada para el proximo

Disminuye el traspaso de informacion, requiere un IV aleatorio

![](attachments/Pasted%20image%2020260816192341.png)

### CFB

Utiliza solo la funcion Enc

Menor complejidad para dispositivos embebidos

Permite generar una transformacion de flujo a partir de una de bloque

![](attachments/Pasted%20image%2020260816192425.png)

### OFB

Construye una transformacion de flujo a partir de una de blque

Permite calcular los bits de la transformacion por adelantado

![](attachments/Pasted%20image%2020260816192459.png)

### Counter

Utiliza un *contador* para generar secuencias de bits de clave

Permite acceso aleatorio

Muy util en ambientes con capacidad de procesamiento paralelo

![](attachments/Pasted%20image%2020260816192552.png)

## Seguridad de cifrado por bloques

Al final terminan siendo tan buenas como la primitiva subyacente

Requieren que la primitiva se comporte como una funcion pseudoaleatoria

Osea que no se puede distinguir $f(x) = Enc_k(x)$ de una funcion tomada al azar

>[!note]
>No esta demostrado que existan las funciones pseudoaleatorias

En la practica usamos funciones que parecen pseudoaleatorias.


| Tipo de encadenamiento | CPA-Secure?                    |
| ---------------------- | ------------------------------ |
| CBC, OFB, CFB          | con IVs aleatorios             |
| Counter                | con si no se repite (k, nonce) |

## DES - Data Encryption Standard

metodo de encripcion desarrollado por IBM

### Caracteristicas

- trabaja con textos binearios
- entrada y salida de 64 bits
- como ascii era de 7 bits tenia 56 bits ejectivos

![](attachments/Pasted%20image%2020260821115840.png)

[implementacion en java del profe](https://github.com/faturita/JavaToolBox/blob/master/src/org/security/README.md)

bueno con el tiempo y el computo se fue haciendo mas brute-forceable

Despues salio 3-DES que es hacerlo 3 veces jashjahs

![](attachments/Pasted%20image%2020260821124333.png)

tambien hoy en dia no es muy fuerte

un paper que hizo el profe con un alumno el año pasado llegaron a que con 1.2M de dolares en AWS lo podian romper en 1 dia.

con hardware propio tipo gpus piolas y qsy por ahi lo rompes hasta en menos, pero bueno te sale mas plata creo.


## AES - Advanced Encryption Standard

Reemplazo actual de DES

![](attachments/Pasted%20image%2020260821124954.png)

![](attachments/Pasted%20image%2020260821125153.png)

No entramos en detalle porque TLT

>[!note] Lo que hay que saber
Esta basado en una resolucion matricial en un campo de gaolois

[implementacion en java del profe](https://github.com/faturita/Advanced-Encryption-Standard-Algorithm)

## Criptosistemas en proyectos

Full mala practica desarrollar un criptosistema nuevo para un proyecto (o usar uno vibecodeado) porque es muy dificil que lo hagas bien.

Hay que usar implementaciones de gente que se dedican a la ciberseguridad. Ademas, costo beneficio nefasto. Te montas sobre cosas que ya existen

La libreria mas comun es **openssl**

## Seguridad de un criptosistema

Cumple con las expectativas de su modelo de seguridad

En general la idea es que la mejor manera de romperlo sea fuerza bruta

Se considera **debilitado** si existen adversarios con probabilidades no despreciables de exito, Pero el esfuerzo es muy alto. 

Si esta debilitado **no** hay que usarlo para proyectos nuevos

Los criptosistemas de **flujo** recomendados hoy (21/08/2026):
- Salsa20
- Rabbit

Los criptosistemas de **bloque** recomendados hoy (21/08/2026):
- IDEA
- 3DES: yo no lo usaria para un proyecto nuevo
- AES: recomendado para proyectos nuevos


Todos estos que vimos hasta ahora son **simetricos** (misma clave para encriptar y desencriptar)

Estos algoritmos no son tan paralelizables por lo que gpus o workers no ayudan demasiado.

