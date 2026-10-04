---
materia: cripto
tipo: apuntes
---

# Seguridad en aplicaciones

No hay una definición única de seguridad. En cada contexto (aplicación, servicio, empresa) la **política de seguridad** define qué modos y usos se consideran seguros.

> [!IMPORTANT] Sistema seguro
> Un sistema es seguro mientras sus estados queden dentro de la política de seguridad.

![](attachments/Pasted%20image%2020261004000001.png)

---

## Conceptos de control de acceso

| Concepto | Qué es |
|---|---|
| **Sujeto** | Persona o servicio que trata de acceder a un objeto |
| **Objeto** | Recurso (dato, servicio) que puede ser leído, modificado o accionado por un sujeto |
| **Acceso** | Forma de interacción entre un sujeto y los objetos |

En Linux: sujeto = proceso/usuario, objeto = archivo, acceso = `rwx`.

La **identidad del sujeto** es lo que lo identifica unívocamente dentro del universo de sujetos posibles. Es requisito para la autenticación.

### La tríada desde los accesos

Las políticas de seguridad se implementan **controlando cómo los sujetos acceden a los objetos**. La CIA (ver [[1_Introduccion]]) se reformula así:

| Propiedad | Visto como acceso |
|---|---|
| Confidencialidad | Existen sujetos que **no** pueden acceder a ciertos objetos |
| Integridad | Existen objetos que solo pueden ser modificados por ciertos sujetos confiables |
| Disponibilidad | Existen objetos que pueden ser accedidos por ciertos sujetos cuando lo requieran |

---

## Modelos

Un **modelo de seguridad** es un modelo formal lógico que define las reglas e interacciones que implementan mecanismos de control de acceso. Están especializados (confidencialidad, integridad o disponibilidad). Evitan reinventar la rueda, pero solos no alcanzan para un sistema real.

Pensamos al sistema como un grafo con nodos y transiciones. Es seguro si todas las transiciones de un nodo (estado) seguro van a otro nodo seguro. Medio que una vez que se estuvo en un estado inseguro es muy dificil volver a un estado seguro

### Bell-Lapadula

Confidecialidad

Es el militar

Read down, write up

- La información se clasifica por nivel de confidencialidad y cada sujeto tiene un nivel de acceso (de los mismos niveles posibles).
- **No read up**: no leo nada más secreto que mi nivel.
- **No write down**: no puedo filtrar información escribiéndola en un nivel más bajo.

**Lattice**: agrega etiquetas (compartimentos) para implementar el **need-to-know**. Un general que se encarga de criptografía no tiene por qué conocer los secretos de los misiles, sin importar su nivel.

> [!TIP]
> Para acceder hace falta nivel suficiente **y** la etiqueta del compartimento.

### Modelo Biba

integridad, ver los niveles en google. Se basa en la confianza

El documento tiene la confianza del que lo escribio o menor

Read up, write down

- Creado por Kenneth J. Biba. Es el **dual** de Bell-LaPadula: misma estructura de niveles pero de integridad.
- **No read down**: no me "contamino" leyendo información menos confiable.
- **No write up**: no puedo ensuciar información más confiable que yo.

> [!WARNING] No confundir las direcciones
> | Modelo | Protege | Lectura | Escritura |
> |---|---|---|---|
> | Bell-LaPadula | Confidencialidad | Read down | Write up |
> | Biba | Integridad | Read up | Write down |

### Modelo Clark-Wilson

Tambien pensado en la integridad

El input del usuario siempre es no confiable, tiene que haber un proceso para convertirla en segura. Incluso un usuario confiable, su input es no confiable porque podria estar encañado (palabras del profe)

- Los datos pueden ser **restringidos** (CDI, *constrained data item*) o **sin restricción** (UDI, *user data input*).
- Los CDI solo se modifican a través de un **proceso de transformación (TP)**, que es responsable de validar la integridad.
- Los sujetos nunca tocan los CDI directamente, solo vía TPs.
- **Separation of duty**: quien modifica los datos no puede ser el mismo que verifica la integridad.

![](attachments/Pasted%20image%2020261002165613.png)

De este modelo surgen cosas como:
- kernel vs user space
- maker checker

### Más allá de los modelos teóricos

No se aplican directamente, pero son la base de muchas implementaciones:

| Modelo | Dónde aparece |
|---|---|
| Bell-LaPadula (compartimentos) | Sistemas de información médica |
| Biba | Clasificación y archivo en prensa, legajos judiciales, declaraciones fiscales |
| Clark-Wilson | Kernel space / user space de los SO |

---

## Control de acceso

> [!IMPORTANT] Control de acceso
> Mecanismo de seguridad que regula **quién** puede acceder a **qué** recursos de la aplicación y **bajo qué condiciones**.

### MAC vs DAC

| | **MAC** (Mandatory) | **DAC** (Discretionary) |
|---|---|---|
| Quién decide | Se aplica obligatoriamente a todos los accesos | El dueño del objeto o un administrador |
| Qué controla | Todos los accesos, cambios en las reglas y el intercambio de info entre sujetos | Permisos sobre los objetos que crea cada sujeto |
| Ejemplos | Bell-LaPadula lattice, SELinux, Squid, API gateway | File systems, object storage |

### Por extension

tipo la matriz, no escala. Hay con n sujetos y m objetos $n \times m$ entradas y cada vez que doy de alta un usuario tengo que agregar $m$ entradas y cada vez que doy de alta un objeto tengo que agregar $n$ entradas

- **ACL** (*Access Control List*): lista de reglas asociada a un recurso que dice qué sujetos pueden hacer qué acciones sobre él.
- **Matriz de accesos**: sujetos en las filas, objetos en las columnas, acciones permitidas en cada celda.
- Problemas: escalabilidad, eficiencia de búsqueda, mantenimiento propenso a errores, espacio, y se adapta mal a entornos dinámicos.
- Para achicarla se usan **permisos por defecto** y **patrones** para objetos (`/users/*`, `/home/**/*.tmp`).

### Por comprension

Reglas descentralizadas que definen cómo los principales accionan sobre los objetos. Pueden definir lo permitido o lo denegado, y guardarse centralizadas o junto a los objetos. El criterio de agrupación define el mecanismo:

RBAC -> role based access control
RuBAC -> rule based access control
ABAC -> attribute based access control

- **RBAC**: los permisos se asignan **solo a roles**, y los roles a sujetos o grupos. Suelen reflejar funciones de la organización (gestor de pacientes, analista de compras, DBA).
- **RuBAC**: cada regla tiene en su forma básica (principal, objeto, tipo de acceso, permitido/bloqueado). Pueden aplicar muchas a la vez, así que hace falta una política de resolución.

### Resolucion de multiples reglas

- First match
- Best match
- Deny over allow

| Política | Cómo resuelve |
|---|---|
| **First match** | Las reglas tienen orden; se aplica la primera que matchea |
| **Best match** | Se aplica la regla más específica |
| **Deny over allow** | Cualquier deny explícito gana sobre los allow |

Aca es donde en general ocurren las macanas

Un bug cuando toca un aspecto de seguridad es una **vulnerabilidad**

> [!EXAMPLE]+ Mismas reglas, distintas resoluciones (firewall de la clase)
> | No. | Source IP | Destination IP | Port | Action |
> |---|---|---|---|---|
> | 1 | 10.1.1.1 | 20.1.1.1 | 80 | Accept |
> | 2 | 10.1.1.2 | 20.1.1.1 | 80 | Deny |
> | 3 | 10.1.1.0/24 | 20.1.1.1 | 80 | Deny |
> | 4 | 10.1.1.3 | 20.1.1.1 | 80 | Accept |
> | 5 | 10.2.2.0/24 | 20.2.2.5 | 80 | Deny |
> | 6 | 10.2.2.5 | 20.2.2.0/24 | 80 | Deny |
> | 7 | 10.3.3.0/24 | 20.3.3.9 | 80 | Accept |
> | 8 | 10.3.3.9 | 20.3.3.0/24 | 80 | Deny |
> | 9 | 0.0.0.0/0 (IP) | 0.0.0.0/0 | 0-65535 | Deny |
>
> **First match**, `10.1.1.1 => 20.1.1.1:80`: matchean la 1 (Accept) y la 3 (Deny, colisión). Recorro en orden → la primera es la 1 → **Accept**.
>
> **Best match**, `10.3.3.9 => 20.3.3.9:80`: matchean la 7 (`10.3.3.0/24`, Accept) y la 8 (`10.3.3.9` exacto, Deny). La 8 es más específica en el origen → **Deny**.
>
> **Deny over allow**, `10.1.1.1 => 20.1.1.1:80`: matchean la 1 (Accept) y la 3 (Deny) → hay un deny explícito → **Deny**.
>
> Mismo paquete, mismo set de reglas: con first match pasa y con deny over allow no. De ahí las macanas.

### Reglas basadas en contexto

El **contexto** son todos los datos asociados al sujeto, al objeto, al momento o al lugar del acceso, y cambian independientemente de las reglas: hora del día, ubicación de origen, departamento, si el usuario está de vacaciones, confiabilidad de la máquina del DBA.

Sirven para detectar anomalías: alguien se loguea desde China y desde Argentina con 5 minutos de diferencia, una usuaria de licencia por maternidad entra a una base del datacenter, dos VPNs en menos de 5 minutos con IPs distintas.

> [!NOTE]
> El problema es que muchas veces hay que **programar** la lógica, y hay sistemas que no se pueden modificar. En **Zero-Trust** se define una entidad externa al Policy Engine que evalúa todas las condiciones de contexto.

### Open Policy Agent (OPA)

Framework estándar que **desacopla** la política de control de acceso del sistema que la aplica. Las políticas se escriben en **Rego**.

Flujo: el servicio manda el requerimiento (input) → OPA evalúa la política (definida fuera del servicio) + datos contextuales (actualizados regularmente u on-demand) → devuelve la decisión.

```rego
default allow := false
allow if {
    creditor_is_valid
    debtor_is_valid
    period_is_valid
    amount_is_valid
}
creditor_is_valid if
  data.account_attributes[input.creditor_account].owner == input.creditor
debtor_is_valid if
  data.account_attributes[input.debtor_account].owner == input.debtor
period_is_valid if
  input.period <= 30
amount_is_valid if
  data.account_attributes[input.debtor_account].amount >= input.amount
```

> [!TIP]
> `input` es lo que viene en el requerimiento, `data` es la información contextual. Por defecto se deniega y solo se permite si todas las condiciones dan verdadero.

---

## Ejemplos de control de acceso

| Sistema | Tipo | Lo importante |
|---|---|---|
| **Unix FS** | DAC | Permisos `rwx` owner/group/others, `umask` |
| **SELinux** | MAC (encima del DAC) | Procesos y recursos tienen un *SELinux context* (`/var/www/html: t_web_html`). Las reglas se generan con macros. Dos procesos con UID 0 pueden tener restringido el acceso entre sí |
| **Windows FS** | DAC | Sujetos cuentas o grupos; herencia de permisos que **persiste después de la creación** (a diferencia de Unix). Calcula permisos efectivos: deny > allow, y reglas locales > heredadas |
| **PostgreSQL** | RBAC + DAC | Roles asociados a usuarios, grupos u otros roles; `LOGIN` permite abrir sesión; el owner del objeto es el rol que lo creó. **Row Level Security** = need-to-know a nivel de fila |
| **Squid proxy** | MAC (reglas ordenadas) | "ACL" mal llamada; filtra por dominio, protocolo, URL, headers, blacklists. Así bloquea streaming la facultad |
| **AWS IAM** | MAC + DAC | Policies asociadas al principal (MAC) y al recurso (DAC) |
| **API gateway** | MAC + contexto | Reglas por URL, dominio, headers, method; rate limit y ancho de banda por IP o SessionID |
| **OAuth 2.0 scopes** | DAC | El usuario consiente qué scopes otorga |

```sql
ALTER TABLE clients ENABLE ROW LEVEL SECURITY;
CREATE POLICY salesperson_clients ON clients USING (salesperson_id::text = current_user);
```

### OAuth 2.0

Estándar de **autorización** para que una aplicación acceda a recursos de un usuario en una plataforma **sin que el usuario le comparta sus credenciales**. Funciona con **tokens de acceso** temporales y específicos (se renuevan con un refresh token).

![](attachments/Pasted%20image%2020261004000002.png)

El **scope** define el nivel de acceso que pide la app (ej. solo el mail vs. todos los contactos). Se le muestra al usuario en la pantalla de consentimiento, el token queda limitado a los scopes otorgados, y cada servicio que recibe el token verifica que su scope esté en la lista.

> [!WARNING]
> OAuth es de **autorización**, no de autenticación.

---

Lectura recomendada: Bishop, *Computer Security: Art and Science*, caps. 4, 5.1–5.4, 6.1–6.2, 7.1, 8.1.
