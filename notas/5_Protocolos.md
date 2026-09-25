
# Protocolos

**Problema:** Con *man in the middle* se cae lo que vimos hasta ahora para el tema de compartir las claves.

### Infraestructura de claves publicas (PKI)

**Objetivo**: asociar identidad a las claves

La solucion son los **certificados** (bloque de informacion de identidad y clave publica). Estos estan firmados digitalmente por una autoridad competente.

Tiene un intervalo de validez

### Uso de certificado

![](attachments/Pasted%20image%2020260920105248.png)



Aca hay como una **cadena de firmas** porque las autoridades certificantes tienen a su vez un certificado!! y quien valida ese certificado? otra autoridad competente!!

Se termina cuando se llega a una autoridad firmate raiz, y esas se autofirman.

Medio que ahi ya tenes que confiar. Las autoridades firmantes raices ya vienen precargadas en los sistemas operativos como ok en esta voy a confiar.

Se suele mandar todo el paquete de certificados de una para evitar el hecho de tener que hacer todas las consultas

### Revocacion de claves

Por algun motivo, ya sea hackeo, alguien se fue de la empresa y no confio mas que esa clave este en control de la empresa, lo que sea. 

Revocar la clave es invalidar una clave ANTES de su expiracion

Hay entidades/urls de servidores que uno les puede pegar para ver si el certificado esta revocado o no. 

El problema tambien es no revocar claves que no deben ser revocadas.

Una solucion para ver que el que la quiere revocar es realmente el dueño, es pedirle que me pase su clave privada (si total se te filtro y la queres revocar no? pasala entonces si te da).

Ese seria el camino feliz. Si hasta yo perdi la clave privada porque me hicieron bosta el servidor donde la tenia guardada o lo que sea, hay otros medios para certificar la identidad de que realmente vos queres revocar tu clave.

Se pueden mandar *pruebas de vida*. Esto se llama OCSP (online certificate status protocol). Solo lo hacen sitios con mucho trafico esto.

### Resumen

![](attachments/Pasted%20image%2020260920113118.png)


Los navegadores son los que hacen todo este malavares del protocolo este de certificados para validar todo.


## Protocolo Needham-Schroeder

Requiere un servicio centralizado (KDC). Genera claves de sesion entre pares.

### Primera aproximacion

![](attachments/Pasted%20image%2020260920114647.png)

A recibe la clave de sesion y un **token** para reenviar a B

Esta primera aproximacion tiene **problemas**

![](attachments/Pasted%20image%2020260920114840.png)

Estas claves se usan por poco tiempo. Duracion corta.

### Segunda aproximacion

![](attachments/Pasted%20image%2020260920115207.png)

El problema de esto es que un atacante podria despues de muchos años, averiguar la clave $k_s$ e impersonar a A asi

![](attachments/Pasted%20image%2020260920115751.png)

### Modificacion Demming-Sacco

![](attachments/Pasted%20image%2020260920115813.png)

>[!note]
>Los **nonce** y los **timestamp** son los mejores recursos para evitar los problemas de repeticion


## Canal seguro TLS

Transport layer security (TLS) es **EL** protocolo con el que se securizan las comunicaciones. Es la abstracción de un canal seguro a partir de un canal inseguro.

**Confidencialidad** e **integridad** aseguradas.

![](attachments/Pasted%20image%2020260920120315.png)

### Concepto

![](attachments/Pasted%20image%2020260920120354.png)

![](attachments/Pasted%20image%2020260920120507.png)

![](attachments/Pasted%20image%2020260920120544.png)

La gran complejidad esta en el **handshake**

La idea era hacerlo future proof, por eso se hace negociacion de los protocolos criptograficos que se van a utilizar.

### Handshake

![](attachments/Pasted%20image%2020260920120851.png)![](attachments/Pasted%20image%2020260920120857.png)![](attachments/Pasted%20image%2020260920120906.png)![](attachments/Pasted%20image%2020260920120917.png)![](attachments/Pasted%20image%2020260920120928.png)![](attachments/Pasted%20image%2020260920120952.png)

El overhead esta principalmente aca, una vez hecho el handshake, la comunicacion es transparente

## Criptografia de umbrales

![](attachments/Pasted%20image%2020260920122513.png)

