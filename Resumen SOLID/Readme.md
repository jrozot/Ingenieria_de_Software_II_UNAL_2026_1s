# Principios SOLID

El video una guía completa sobre los cinco principios SOLID, los cuales son recomendaciones diseñadas para hacer el código más legible, limpio, mantenible y escalable. Estos principios permiten a los desarrolladores modificar el código sin "demasiado trauma" y demuestra su aplicación tanto en Angular como en React, evidenciando que no están limitados a la programación orientada a objetos.

---

## 1. Principio de Responsabilidad Única (SRP)

**Definición:** Cada módulo, clase o función debe tener una única razón para cambiar.

**Ejemplos:**
Un componente no debería encargarse simultáneamente de realizar peticiones HTTP, filtrar datos y manejar la interfaz de usuario. En su lugar, estas tareas deben separarse en servicios o hooks independientes.

**Cómo detectar una violación:**

* Si necesitas modificar un componente de UI para cambiar lógica de negocio.
* Si una clase maneja múltiples responsabilidades no relacionadas (por ejemplo, enviar correos y conectarse a una base de datos).
* Si necesitas múltiples mocks para probar una sola función.

---

## 2. Principio Abierto/Cerrado (OCP)

**Definición:** El software debe estar abierto a extensión, pero cerrado a modificación.

El nuevo comportamiento debe añadirse sin modificar el código existente que ya funciona.

**Ejemplo:**
En lugar de usar múltiples estructuras `if/else` o `switch` para manejar diferentes tipos de notificaciones (correo, SMS, etc.), se debe usar un objeto manejador o configuración que permita agregar nuevos tipos sin cambiar la lógica principal.

**Cómo detectar una violación:**

* Si cada nuevo requerimiento obliga a modificar lógica condicional existente.

---

## 3. Principio de Sustitución de Liskov (LSP)

**Definición:** Las subclases o implementaciones deben poder sustituir a sus clases base o interfaces sin romper el comportamiento de la aplicación.

**Ejemplo:**
Si un servicio espera que un método retorne un "observable", una versión mock no debería devolver un arreglo simple, ya que rompe el contrato establecido y genera errores. En React, este contrato suele mantenerse mediante validación de props.

**Cómo detectar una violación:**

* Errores de tipo.
* Excepciones por implementaciones incompletas.
* Comportamientos incorrectos al reemplazar una clase por otra (por ejemplo, un mock por un servicio real).

---

## 4. Principio de Segregación de Interfaces (ISP)

**Definición:** El código no debe depender de interfaces que no utiliza.

Es mejor tener varias interfaces pequeñas y específicas que una sola interfaz grande y sobrecargada.

**Ejemplo:**
En lugar de un componente `UserCard` masivo que recibe todas las propiedades y acciones posibles del usuario (aunque no las use), se debería dividir en componentes más pequeños como `UserInfo` y `UserActions`, cada uno con datos específicos.

**Cómo detectar una violación:**

* Interfaces muy grandes con muchas propiedades opcionales.
* Componentes con props sin usar.
* Funciones que reciben objetos de los cuales solo utilizan unas pocas propiedades.

---

## 5. Principio de Inversión de Dependencias (DIP)

**Definición:** El código debe depender de abstracciones (interfaces), no de implementaciones concretas.

**Ejemplo:**
En lugar de que un servicio instancie directamente un `EmailClient` usando `new`, debería recibir una interfaz genérica como `Notifier` a través de su constructor. Esto permite cambiar fácilmente la implementación (por ejemplo, usar un mock o otro servicio) sin modificar el código dependiente.

**Cómo detectar una violación:**

* Instanciaciones directas dentro de clases (`new X`).
* Creación manual de dependencias en lugar de inyección.
* Necesidad de reconfigurar módulos completos solo para ejecutar pruebas.

---

## Código Legacy

En el mundo real, los desarrolladores frecuentemente trabajan con código legacy que no sigue estos principios.

Recomienda aplicar la **"regla del scout"**: siempre dejar el código un poco mejor de como se encontró. Aunque no siempre es posible refactorizar un sistema completo debido a limitaciones de tiempo y presupuesto, se debe priorizar la entrega de valor mientras se implementan estos principios de forma incremental cuando sea posible.
