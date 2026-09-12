# Cifrado asimetrcio y firma digital

## Problema

En un criptosistema de clave simetrica, hay que transmitir la clave.

como compartimos la clave?

Si quiero comunicar n cosas, voy a necesitar $n\choose2$ $= \frac{n(n-1)}{2}$ claves. Escala cuadraticamente
## KDC - key distribution centers

Entidades (third party) que comarten clave con cada entidad que participa. Si a quiere comunicarse con b, primero tiene que enviarle un pedido a kdc. Escala linealmente

Medio que este es alto blanco de ataque. 2 mecanismos populares

![](attachments/Pasted%20image%2020260912182853.png)

## Criptografia asimetrica

Quiero cifrar con una clave y descifrar con otra. La clave que cifra la podria tener un atacante y no pasa nada.

### Intercambio de claves

![](attachments/Pasted%20image%2020260912183847.png)

Idea, intercambio mensajes entre a y b para ver que calculos tienen que hacer y cada uno calcula una clave por su cuenta. El chiste es que ambos terminan llegando a la misma clave y que un atacante que vea todos los mensajes en el medio, no la pueda calcular.

### Expreimento de intercambio de claves

![](attachments/Pasted%20image%2020260912184013.png)

### Itercaambio Diffie-Hellman

Es **el** esquema de intercambio de claves (es de hace 40 años)

![](attachments/Pasted%20image%2020260912184314.png)

Se basa en el **problema del logaritmo discreto**. Que no tiene solucion eficiente.

**Conjetura de decision de DH**: dados $g, g^x, g^y$ no se puede distinguir $g^{xy}$ de un valor aleatorio.

resolver cualquiera de estos 2 es un problema np-hard. 

>[!IMPORTANT]
>En la practica el canal por donde se transimten los mensajes tiene que ser autenticado. Osea esta todo bien si un atacante puede leer esos mensajes, pero esta todo mal si el atacante puede alterar esos mensajes (man in the middle).

## Criptosistema asimetrico
![](attachments/Pasted%20image%2020260912191537.png)

Se encripta con la **clave publica** y se descifra con la **clave privada**

### Prueba de indistinguibilidad

![](attachments/Pasted%20image%2020260912191645.png)

## "Textbook" RSA

![](attachments/Pasted%20image%2020260912192116.png)

>[!IMPORTANT]
>**Problema**: El cifrado es determinisitco

Luego **no** es el RSA que se usa en la practica


## PKCS 1 V1.5

![](attachments/Pasted%20image%2020260912193722.png)

Siempre fue una cosa fea que no sea CCA-Secure y que no se este seguro de que sea CPA-Secure.

Osea porque no se sabe si hay otra forma de vulnerarlo que no sea la de la factorizacion.
## Elgamal (basado en DH)

Es el mas usado

![](attachments/Pasted%20image%2020260912194129.png)

Recordemos que G es un grupo. 

## Firma digital

![](attachments/Pasted%20image%2020260912194606.png)

Es como un mac asimetrico. Pero esta piola y parece como la firma de una persona

Solo el que tiene la calve privada puede firmar pero cualquiera puede verificar.

### Seguridad de una firma digital

Sig-forge

![](attachments/Pasted%20image%2020260912194739.png)