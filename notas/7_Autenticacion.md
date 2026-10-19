# Autenticacion


![](attachments/Pasted%20image%2020261017162806.png)

Cuando queremos meter control de acceso tenemos que tener si o si autenticacion

**spoofing**: hacerse pasar por otro

## Sistema de autenticacion

### Componentes

1. $A$ -> Informacion de autenticacion
2. $C$ -> Informacion complementaria
3. $F = \{f: A \rightarrow C\}$ -> Funciones de complementacion
4. $L = \{l: A \times C \rightarrow \{0, 1\}\}$ -> Funciones de autenticacion
5. $S$ -> funciones de seleccion

![](attachments/Pasted%20image%2020261017164904.png)
### Factor

Lo que uso para demostrar que soy quien digo ser

De aca sale lo de 2FA o MFA

pueden ser de tipo
- algo que conozco (una clave)
- algo que tengo (una llave usb)
- algo que soy (una huella digital)
- contexto (red de origen, geolocalizacion)

mas arriba, mas confiable es como factor. Estos factores pueden ser positivos o negativos

Se usan muchos factores y no muchos mecanismos del mismo factor porque las skills/tecnicas que se requieren para vulnerar un mecanismo de "algo que conozco" son parecidos entre si.

Por ejemplo ponele que tengo 2 llaves para entrar a mi casa, un cerrajero con mucha skill, si puede vulnerar una puede vulnerar ambas. En cambio si tengo llave+huella, un cerrajero solo no puede y un falsificador de huellas digitales tampoco, se necesitaria de un cerrajero falsificador de huellas digitales, lo cual es mucho mas dificil.

La seguridad de un sistema es la del peor de los mecanismos que tiene. Por ejemplo si tengo un re sistema pero la manera para recuperar la contraseña es una pregunta de a que colegio fui, es nefasto porque lit que eso lo tenes publico en ig o linkedin o en redes sociales.

## Claves


### Tipos

- secuencias de caracteres
- secuencias de palabras (pass-phrases)
- Algoritmicas (challenge-response, claves de uso unico)
### Almacenamiento

#### En texto plano

NUNCA

#### Archivo cifrado

Requiero de una clave para acceder a las contraseñas, esta clave puede estar en:
- Un archivo de configuracion
- En el mismo ejecutable del sistema
- Ser ingresada una vez se inicia el sistema
- En un dispositivo criptografico especializado

Solo recomendable si es requisito accesar a la clave original, como para reenviarla a un tercer sistema por ejemplo

#### Prueba de conocimiento

Esta es la que va, nada mas necesito saber si conoce la clave, no necesariamente que me mande la clave

La almacenamos en un hash criptografico

Por ejemplo Bcrypt o Argon2 (usan tecnicas como salting para hacerlas mas robustas y resistentes a ataques de tablas de hash, por ejemplo)

## Ataques a un sistema de autenticacion

Quiero hacer spoofing

![](attachments/Pasted%20image%2020261017172156.png)

Una forma es tratar de adivinar la clave tipo fuerza bruta

pero se pueden hacer mejoras porque los humanos somos pesimos tratando de ser aleatorios para las claves usando:
- diccionarios de palabras
- diccionarios de claves descubiertas (por esto no hay que repetir claves)
- transformaciones simples de palabras
- utilizar info de contexto (tipo fechas de nacimiento y esas cosas)


Para prevenir podemos
- Esconder informacion complementaria
- Prevenir el uso a la funcion de autenticacion (tiempos crecientes ante fallas de auth, deshabilitar principales, jailing/honeypot, captchas)
- subir la complejidad de las claves (mas largas, que incluyan numeros y simbolos raros)
- seleccion de claves, tipo claves generadas re complicadas y dificiles de memorizar
- claves pronunciables (mas faciles de memorizar)


Podemos tambien tener una revision proactiva de claves, tipo pentesting. 

Podemos poner expiracion de claves tambien, esto es hacer mitigacion de daños. Si alguien me robo la contraseña, el tiempo de accion para hacerme bosta es acotado

## Salting

Agregarle una perturbacion a la clave, no es secreta onda puede estar en la db pero, la idea basica es que 2 usuarios tengan distinto salt cosa de que si 2 usuarios tienen la misma contraseña no se guarde con el mismo hash. Inutilizando los ataques de rainbow tables

Al atacar una sola cuenta no agrega nada, pero al atarcar masivamente si.

Se pueden repetir pero la idea es que no se repitan mucho

## Algunas implementaciones

### PBKDF2

![](attachments/Pasted%20image%2020261017181108.png)![](attachments/Pasted%20image%2020261017181121.png)

### Challenge response

![](attachments/Pasted%20image%2020261017181320.png)

### Claves de uso unico

![](attachments/Pasted%20image%2020261017181944.png)

HTOP -> usa un contador, pasa que si genere una clave y no la mande, cuando genere la proxima ya el contador en el cliente y en el servidor va a estar desfazada

TOTP -> usa intervalos de tiempo para generar la clave, es la que usa google authenticator por ejemplo

## MFA

![](attachments/Pasted%20image%2020261017182147.png)

## SSO

![](attachments/Pasted%20image%2020261017182252.png)

Por ejemplo cuando una app delega a otra que implementa esto. Tipo iniciar sesion con google en una app

## Conclusion

Es complejo, hoy en dia si estamos haciendo una app, uno busca delegar la autenticacion a algo ya implementado. Aguante auth0 aguante argentina