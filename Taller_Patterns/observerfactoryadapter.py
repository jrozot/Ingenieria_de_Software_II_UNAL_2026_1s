from abc import ABC, abstractmethod

# =========================
# PATRÓN CREACIONAL: FACTORY METHOD
# =========================

# Producto abstracto
class Transporte(ABC):

    @abstractmethod
    def entregar(self):
        pass


# Productos concretos
class Camion(Transporte):

    def entregar(self):
        return "Entrega realizada por camión"


class Barco(Transporte):

    def entregar(self):
        return "Entrega realizada por barco"


# Creator (Factory Method)
class Logistica(ABC):

    @abstractmethod
    def crear_transporte(self):
        pass

    def planificar_entrega(self):
        transporte = self.crear_transporte()
        return transporte.entregar()


# Creadores concretos
class LogisticaTerrestre(Logistica):

    def crear_transporte(self):
        return Camion()


class LogisticaMaritima(Logistica):

    def crear_transporte(self):
        return Barco()


# =========================
# PATRÓN ESTRUCTURAL: ADAPTER
# =========================

# Servicio externo con interfaz incompatible
class ServicioEnvioExterno:

    def enviar_paquete(self):
        return "Entrega realizada por servicio externo"


# Adapter
class EnvioAdapter(Transporte):

    def __init__(self, servicio_externo):
        self.servicio_externo = servicio_externo

    def entregar(self):
        return self.servicio_externo.enviar_paquete()


# =========================
# PATRÓN DE COMPORTAMIENTO: OBSERVER
# =========================

class Observador(ABC):
    @abstractmethod
    def actualizar(self, mensaje):
        pass


class Cliente(Observador):
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, mensaje):
        print(f"[Notificación para {self.nombre}]: {mensaje}")


class Entrega:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def notificar_clientes(self, mensaje):
        for cliente in self.clientes:
            cliente.actualizar(mensaje)

    def realizar_entrega(self, transporte: Transporte):
        resultado = transporte.entregar()
        self.notificar_clientes(resultado)


# =========================
# APLICACIÓN DE CONSOLA
# =========================

def main():
    print("Seleccione tipo de logística:")
    print("1. Terrestre")
    print("2. Marítima")
    print("3. Servicio externo (Adapter)")

    opcion = input("Opción: ")

    if opcion == "1":
        logistica = LogisticaTerrestre()
    elif opcion == "2":
        logistica = LogisticaMaritima()
    elif opcion == "3":
        servicio_externo = ServicioEnvioExterno()
        logistica = EnvioAdapter(servicio_externo)
    else:
        print("Opción inválida")
        return

    # Crear entrega y registrar clientes (Observer)
    entrega = Entrega()
    cliente1 = Cliente("Alice")
    cliente2 = Cliente("Bob")
    entrega.agregar_cliente(cliente1)
    entrega.agregar_cliente(cliente2)

    # Realizar entrega
    if isinstance(logistica, Logistica):
        transporte = logistica.crear_transporte()
    else:
        transporte = logistica  # Adapter ya es un Transporte

    entrega.realizar_entrega(transporte)


if __name__ == "__main__":
    main()
