---
materia: cripto
tipo: apuntes
---

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

![](attachments/Pasted%20image%2020260829125609.png)

## Pruebas de seguridad

Prueban las caracteristicas de un criptosistema 

prueban a un algoritmo que representa un ataque, se repite muchas veces y lo que interesa ver es la probabilidad de exito del atacante

### Prueba de indistinguibilidad

![](attachments/Pasted%20image%2020260829125023.png)
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

### Counter - CTR

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

## Comparacion de modos

> [!NOTE]
> Esto no esta en las slides de la Clase 02: se deriva de la formula de descifrado de cada modo.
> Cayo en la Guia 4, asi que conviene tenerlo escrito.

### Formulas de descifrado

Todo lo demas sale de aca. En los modos que encadenan, $C_0 = IV$.

| Modo | Cifrado | Descifrado |
| ---- | ------- | ---------- |
| ECB | $C_i = e_k(M_i)$ | $M_i = d_k(C_i)$ |
| CBC | $C_i = e_k(M_i \oplus C_{i-1})$ | $M_i = d_k(C_i) \oplus C_{i-1}$ |
| CFB | $C_i = M_i \oplus e_k(C_{i-1})$ | $M_i = C_i \oplus e_k(C_{i-1})$ |
| OFB | $C_i = M_i \oplus O_i$, con $O_i = e_k(O_{i-1})$ y $O_0 = IV$ | $M_i = C_i \oplus O_i$ |
| CTR | $C_i = M_i \oplus e_k(\text{nonce} \Vert i)$ | $M_i = C_i \oplus e_k(\text{nonce} \Vert i)$ |

> [!IMPORTANT]
> **OFB y CTR nunca usan $d_k$**. La secuencia de clave depende solo de $(k, IV)$ y de la posicion,
> no del criptograma, asi que cifrar y descifrar son la misma operacion. Son criptosistemas de
> **flujo** construidos sobre una primitiva de bloque. CBC en cambio consume $C_{i-1}$ al descifrar.
>
> De esta diferencia salen todas las comparaciones de abajo.

### Propagacion de errores

Hay que separar dos tipos de error de transmision, porque dan resultados opuestos.

**Bits alterados** (se mantiene el largo). Un bit dado vuelta en $C_j$ afecta:

| Modo | Alcance | Que pasa exactamente |
| ---- | ------- | -------------------- |
| ECB | 1 bloque | $M_j$ entero ilegible |
| CBC | 2 bloques | $M_j$ entero ilegible, y en $M_{j+1}$ se da vuelta **exactamente el mismo bit** |
| CFB | 2 bloques | en $M_j$ se da vuelta ese mismo bit, y $M_{j+1}$ queda entero ilegible |
| OFB | 1 bit | en $M_j$ se da vuelta ese bit y nada mas |
| CTR | 1 bit | en $M_j$ se da vuelta ese bit y nada mas |

**Bits perdidos** (se pierde la sincronizacion):

| Modo | Se recupera? |
| ---- | ------------ |
| ECB, CBC, CFB | Si, son **autosincronizantes**: el estado que necesita el descifrado esta en el criptograma mismo. Se pierden 1 o 2 bloques y despues vuelve a descifrar bien. Solo vale si la perdida es de bloques enteros; si se pierde una cantidad de bytes que no es multiplo del bloque, se pierde todo lo que sigue. |
| OFB, CTR | No, nunca. La secuencia de clave esta atada a la posicion: perder un solo bit corre todo y el resto queda ilegible. |

### Confidencialidad

Todos son CPA-secure bajo las condiciones de la tabla de [[2_Cifrado#Seguridad de cifrado por bloques|mas arriba]] (menos ECB, que no lo es nunca). La diferencia real esta en **que tan grave es equivocarse con el IV**:

| Modo | Si se repite el IV con la misma $k$ |
| ---- | ----------------------------------- |
| CBC | Dos mensajes con el mismo prefijo dan el mismo prefijo de criptograma. Se filtra hasta donde son iguales, bloque a bloque. Malo, pero acotado. |
| OFB, CTR | **Catastrofico**: misma secuencia de clave, entonces $C \oplus C' = M \oplus M'$ y se filtran los dos textos claros. |

> [!WARNING]
> Lo de OFB y CTR es exactamente el problema de reusar la clave del [[2_Cifrado#One time pad (OTP)|OTP]].
> Que esten construidos sobre AES no los salva: un $(k, IV)$ repetido los reduce a un OTP con clave
> reusada.

Ademas CBC pide un IV **aleatorio e impredecible**, no solo distinto. CTR se conforma con que no se
repita el par $(k, \text{nonce})$ — por eso ahi si sirve un contador.

> [!NOTE]
> OFB tiene un problema propio que CTR no tiene: como $O_i = e_k(O_{i-1})$ itera una permutacion, la
> secuencia de clave **cicla** en algun momento y ahi se repite. CTR no, porque el contador le
> garantiza entradas distintas a $e_k$.

> [!WARNING] Trampa de parcial
> "Propaga menos errores" suena a ventaja, pero es justo lo que hace a OFB y CTR **maleables**: el
> atacante da vuelta un bit del criptograma y da vuelta exactamente ese bit del texto claro, sin
> romper nada mas. Es el ataque del sueldo con el que arranca [[3_MACs-cifrado-autenticado#Problema]].
> Ningun modo de encadenamiento da integridad: para eso hace falta un MAC.


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

