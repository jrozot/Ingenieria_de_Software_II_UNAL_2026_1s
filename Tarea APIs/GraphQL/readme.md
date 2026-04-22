# Tarea GraphQL

## Pantallazos de Requests en Postman

### Query 1: Continente con países (anidada)
![x](./Screenshots/q1.png)

### Query 2: País filtrado por código
![x](./Screenshots/q2.png)

### Query 3: Todos los continentes con países
![x](./Screenshots/q3.png)

### Query 4: Idiomas con países
![x](./Screenshots/q4.png)

### Query 5: Países con idiomas
![x](./Screenshots/q5.png)

---

# Respuesta a las preguntas

### ¿Qué diferencia encontraste vs REST?

La principal diferencia es que GraphQL permite obtener exactamente los datos que se necesitan en una sola consulta, mientras que en REST normalmente se requieren múltiples endpoints y se recibe información fija (a veces de más o de menos). Además, GraphQL facilita las consultas anidadas (relaciones) sin necesidad de hacer múltiples llamadas.

---

### ¿Cuántos requests REST necesitarías para reemplazar tu query más compleja?

Para la query más compleja (por ejemplo, continentes con países o países con idiomas), en REST se necesitarían al menos:

- 1 request para obtener los continentes o países
- N requests adicionales para obtener los datos relacionados (países o idiomas)

En total, podrían ser fácilmente entre **5 y 20 requests**, dependiendo de la cantidad de datos. En GraphQL esto se resuelve en **un solo request**.

---

### ¿En qué proyecto real usarías GraphQL?

Usaría GraphQL en aplicaciones donde haya muchas relaciones entre datos y necesidad de optimizar llamadas, por ejemplo:

- Aplicaciones web con frontend dinámico (React, Vue)
- Sistemas de e-commerce (productos, categorías, usuarios)
- Apps móviles donde es clave reducir el número de requests
- Dashboards con múltiples fuentes de datos

GraphQL es especialmente útil cuando el cliente necesita flexibilidad para definir qué datos consumir.
