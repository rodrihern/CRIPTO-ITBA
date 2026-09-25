
# MACs y Cifrado Autenticado

## Problema

Supongamos que tengo acceso a la db donde se guarda mi sueldo y esta cifrado con un cifrado CPA secure. Yo puedo modificar mi sueldo siguiendo esto

![](attachments/Pasted%20image%2020260829120439.png)

Mi sueldo es $m = 12345$ y quiero que sea $s = 100000$. Como
$$
d_k(c \oplus x) = m \oplus x
$$

elijo esa $x = m \oplus s$ dado que cuando lo desencripten el resultado va a quedar
$$
m \oplus m \oplus s = s
$$
En la imagen vemos el ejemplo de como cambiamos el cifer text de $2EDF79 \rightarrow 2F69F0$ para que cuando lo desencripten, el sueldo mio quede 100000.

Si tiene este problema/vulnerabilidad se dice que el criptosistema es **maleable**
## Ataque de texto cifrado escogido - CCA

Hagamos una nueva prueba de seguridad para tratar mitigar este problema

![](attachments/Pasted%20image%2020260829121300.png)

Ninguo de los criptosistemas de lo que vimos hasta ahora pasan esta prueba 😱

Es un problema que no se puede resolver con cifrado solamente. El problema en lo de que el chabon cambiaba su sueldo, se resuelve haciendo que el no tenga permisos de escritura sobre su sueldo en la db, (idealmente tampoco de lectura xd).

Requerimos otra herramienta de seguridad

## Control de integridad

**MAC**: message authentication code

![](attachments/Pasted%20image%2020260829130544.png)

Una falla en la seguridad de un mac se llama *falsificacion* o *forge*

### Prueba de seguridad de un un MAC

![](attachments/Pasted%20image%2020260829143829.png)

Unos chinos en 2004 consiguieron vulnerar esto pero no parecia util, despues de muchas optimizaciones a los algoritmos de los chinos, en 2006 ya podia correr en una compu normal y despues en 2008 un tipo logro falsificar certificados de google a modo de prueba de concepto y recien ahi la gente dijo uy. Moraleja, por mas que parezca insignificante o poco util en el momento, hay que darle bola a lo de las pruebas de seguridad y eso. 

### CBC-MAC


![](attachments/Pasted%20image%2020260829150851.png)

Si la definimos para mensajes de longitud fija va, pero sino tiene un problema

![](attachments/Pasted%20image%2020260829151135.png)

![](attachments/Pasted%20image%2020260829151824.png)

>[!note]
>Para mi yo del futuro cuando lea esto y no entienda nada:
>
>hace el CBC pero cambiale los indices 1 y 2 tipo m1 = A, m2 = A||B
>cosa de que t1 = f(m1), t2 = f(m2).

Aca el problema fue que el atacante pudo reconstruir los estados intermedios. La idea es evitar esto para hacerlo seguro

![](attachments/Pasted%20image%2020260829152214.png)

## Funciones de hash criptograficas

no tienen clave

![](attachments/Pasted%20image%2020260905193435.png)

Ojo que el gen no es de claves, la idea es que se tiene un conjuto de funciones de hash y agarramos la $s$ de ese conjunto. En la practica los conjuntos son de una sola funcion de hash xd.

La idea es que aunque cambie 1 caracter de las entradas

Colisiones tiene si o si. Una colision seria:
$$
x_1 \ne x_2 \ y \ h(x_1) = h(x_2)
$$

>[!important]
>La idea principal es que no haya una inversa

>[!note]
>Computacionalmente imposible nos referimos a que no se puede encontrar en tiempo polinomico
### Resistencia a preimagenes

Para todo $y$ es computacionalmente imposible hallar $x$ tal que $y = h(x)$

### Resistencia a segundas preimagenes

Para todo $x$, es computacionalmente imposible hallar $x' \neq x$ tal que $h(x') = h(x)$

### Resistencia a colisiones

Es computacionalmente imposible hallar $x_1, x_2$ tal que $h(x_1) = h(x_2)$

Hay una prueba para esto

![](attachments/Pasted%20image%2020260905194735.png)

Nos centramos en este porque en mensajes y etiquetas grandes, garantiza las otras 2.
### Modelo general iterativo

Permite hacer funciones de hash a partir de funcines de compresion

![](attachments/Pasted%20image%2020260905195726.png)

### algunas funciones de hash conocidas

- md5
- sha-1
- sha-3 (el estandar hoy en dia)

### Seguridad de las funciones de hash

$$
h: A \rightarrow B
$$

Para preimagenes y segundas preimagenes se requieren intentos del orden de $\#B$ 

Mientras que para colisiones se necesitan $\sqrt{\#B}$ 

que bueno que esta esto la concha de mi madre que alto que me queda este escritorio de poronga

### Macs

Se pueden construir macs a partir de una funcion de hash

![](attachments/Pasted%20image%2020260905205151.png)

usa esas 2 constantes pero podria usar otras, lo unico que si es que tienen que ser distintas el inner-pad y el outer-pad

Esto es lo que se suele usar en la practica porque es mas rapido que el CBC-MAC.

de golpe aparecio un problema que no podiamos resolver

## Privacidad e integridad

![](attachments/Pasted%20image%2020260905205529.png)


>[!IMPORTANT]
>1. **Cifrar y autenticar:** La primera es la que no es segura porque como que le estamos dando 2 puertas de entrada al mensaje. t brinda informacion del mensaje
> 2. **Autenticar, luego cifrar**: Puede ser seguro, **no** hay una prueba general.
> 3. **Cifrar, luego autenticar**: tiene una prueba general para claves $k_1$, $k_2$ independientes


`ssh` utiliza el segundo de una forma que es segura. Si hiciesemos `ssh` hoy usariamos el 3ro xd.

## Cifrado autenticado

![](attachments/Pasted%20image%2020260905210106.png)

### Encadenamiento CCM

![](attachments/Pasted%20image%2020260905210654.png)

Es mas lento pero nos da el control de integridad por la misma logitud de la clave.

### GCM

Es el que le gano al CCM

![](attachments/Pasted%20image%2020260905210750.png)

la mayoria de aplicaciones (99% tiro el profe) requieren de esto. Casos muy particulares requeririan de otra cosa

## Aplicaciones practicas

En terminos generales, siempre usar cifrado autenticado.

En general siempre que se quiere confidencialidad, se requiere tambien integridad.

