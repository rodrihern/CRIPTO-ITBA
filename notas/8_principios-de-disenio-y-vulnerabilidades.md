
# Principios de diseño y vulnerabilidades

## Principios

1. **Least privilige**: Se debe asegurar que los sujetos solo tengan acceso a lo minimo y necesario para hacer su trabajo
2. **Fail-safe defaults**: whitelists >> blacklists. No hay cuentas de usuario por defecto con cuentas conocida. No abrir puertos por defecto porque si. Se quiere fallar de forma segura. (es un principio de diseño, a veces hay que ir en contra, en general seguridad vs funcionalidad es medio como que van en contra)
3. **Economy of mechanism**: simplicidad. Se debe evitar el uso de arquitecturas muy sofisticadas o sistemas muy complejos cuando hacemos segurdiad porque un bug en un sistema de seguridad es una vulnerabilidad. Mejor muchos mecanismos simples a uno complejo
4. **Complete mediation**: si hay un control, este se debe aplicar a todas las interacciones alcanzadas.
5. **open design**: no debe basarse la seguridad en mantener el diseño coulto
6. **separation of privilege**: toda tarea critica no debe quedar bajo el control de un solo sujeto. Se aplica muchas veces el principio de *control por oposicion de intereses*
7. **Defense in Depth**: evitar distintos mecanismos compartan recursos, algoritmos o hardware. Queremos minimizar el impacto de una falla, cosa de que si rompo un mecanismo no haya roto todos. Medio como hacer la defensa en capas, cosa de que haya que vulnerar varias capas
8. **psychological acceptability**: el peor enemigo es el usuario no compliant. Los mecanismos de seguridad tienen que ser lo suficientemente simples para que los usuarios lo usen y les deberia poder dejar hacer su trabajo con normalidad (onda que no quiera el usuario bypassearlo)
## Amenazas y vulnerabilidades

$$
Threat + Vulnerability = Risk
$$

- **Amenaza**: cualquier elemento que pueda afectar la confidencialidad, integridad o disponibilidad. A new incident with potential to harm a system
- **Vulnerabilidad**: Es una debilidad en un activo o grupo de activos que permite que un atacante pueda aprovechar para lograr un acceso que no tiene permitido. Known weakness that hackers could exploit
- **Risk**: the potential for damage when a threat exploits a vulnerability

### Tipos de amenazas

Internas o externas

segun su agente amenazante:
- humanos (hacker o admin que comete un error)
- ambientales (una inundacion)
- teconologicos (servidor que se le quema la fuente)

maliciosos o no (tipo nos lo pueden hacer sin querer)

Segun el impacto:
- destruccion de info (disponibilidad)
- corrupcion de info (integridad)
- revelar info (confidencialidad)
- robo del servicio (sin afectar el uso de otros usuarios, fraude)
- denegacion de servicio (DOS disponibilidad)
- elevacion de privilegios (bypass de ACL)
- uso ilegal (para lograr otros objetivos)

### Tipos de vulnerabilidades

![](attachments/Pasted%20image%2020261018213748.png)

### CVE - Common vulnerabilities and exposures

Mitre es una organizacion que publica todos los CVE, osea todas las vulnerabilidades

### Zero-day

un **exploit** es un programa que permite usar una vulnerabilidad para generar una brecha de seguridad

No todas las vulnerabilidades pueden ser *explotadas* facilmente

Hasta que son reportadas y publicadas estas vulnerabilidades, se las conoce como *zero-day*

Los exploits zero-day tienen un alto valor en el mercado poruqe permite aprovechar vulnerabilidades para las cuales no hay prevencion (corte que casi nadie sabe que existe)

### CWE - common weakness enumeration

Es un registro de las debilidades en el software que dan lugar a que las vulnerabilidades sucedan

Son como categorias para agrupar los distintos CVE, algo asi como tipos de vulnerabilidades.

las mas comunes son

![](attachments/Pasted%20image%2020261019001722.png)

### OWASP 10

OWASP es una orcanizacion focalizada en combatir los problemas de seguridad en las aplicaciones.

Regularmente publica las vulnarabilidades de la web mas comunes y las buenas practicas para prevenirlas

### Threat modeling

Tecnica de ingenieria que se aplica para entender las amenazas, ataques, vulnerabilidades y contramedidas que uno puede hacer.

La hizo microsoft y la compartio al mundo, introduciendo la clasificacion STRIDE

![](attachments/Pasted%20image%2020261019002728.png)

![](attachments/Pasted%20image%2020261019003029.png)![](attachments/Pasted%20image%2020261019003047.png)

Desp OWASP tambien tiene uno pero mas generico apuntando a que sea tambien aplicable a aplicaciones web

![](attachments/Pasted%20image%2020261019003200.png)