# Principios SOLID del Diseño Orientado a Objetos

El acrónimo SOLID, propuesto por Robert C. Martin, representa cinco principios básicos que ayudan a evitar malos diseños y a lograr alta cohesión y bajo acoplamiento.

## 1. Principio de Responsabilidad Única (SRP)
"Una clase debe tener una sola razón para cambiar."

- **Idea:** Una clase debe encargarse de una sola función del software.  
  Si una clase maneja lógica de negocio, base de datos y formato de interfaz al mismo tiempo (por ejemplo, una clase Invoice que calcula totales y también guarda datos), está violando este principio.

- **Beneficios:**  
  Reduce conflictos al trabajar en equipo y evita que un cambio en una parte (como la base de datos) rompa otra (como las reglas de negocio).

---

## 2. Principio Abierto/Cerrado (OCP)
"Un módulo debe estar abierto a extensión, pero cerrado a modificación."

- **Idea:** Se debe poder cambiar el comportamiento de un módulo sin modificar su código fuente.  
  Esto se logra usando abstracciones.

- **Cómo implementarlo:**
  - **Polimorfismo dinámico:** Usar interfaces o clases abstractas.  
    Ejemplo: una función LogOn debe depender de una interfaz Modem, no de implementaciones específicas.
  - **Polimorfismo estático:** Usar genéricos o plantillas para extender sin modificar el código.

---

## 3. Principio de Sustitución de Liskov (LSP)
"Las subclases deben poder reemplazar a sus clases base."

- **Idea:** Una clase hija debe comportarse correctamente cuando se usa en lugar de la clase padre.

- **Ejemplo (Círculo y Elipse):**  
  Si un Círculo hereda de Elipse, puede romper este principio.  
  Una Elipse puede tener dos focos, pero un Círculo solo uno. Esto puede causar errores si el código espera el comportamiento normal de una Elipse.

- **Impacto:**  
  Cuando se viola este principio, se termina usando condiciones como `if` o `switch`, lo que rompe otros principios como OCP.

---

## 4. Principio de Segregación de Interfaces (ISP)
"Los clientes no deben depender de interfaces que no usan."

- **Idea:** Las interfaces grandes (con muchos métodos) deben dividirse en interfaces más pequeñas y específicas.

- **Ejemplo:**  
  Si una clase TimedDoor necesita comportarse como puerta y como temporizador, no se debe agregar todo al mismo interfaz.  
  En su lugar, se crean interfaces separadas y la clase implementa ambas o usa un adaptador.

---

## 5. Principio de Inversión de Dependencias (DIP)
"Depende de abstracciones, no de implementaciones."

- **Idea:**  
  Los módulos importantes no deben depender de detalles.  
  Ambos deben depender de abstracciones.

- **Cómo funciona:**  
  En lugar de que un módulo principal dependa directamente de uno secundario, ambos dependen de una interfaz.

- **Ejemplo:**  
  Un botón no debe depender directamente de una lámpara.  
  En su lugar, el botón depende de una interfaz (ButtonClient), que la lámpara implementa.
