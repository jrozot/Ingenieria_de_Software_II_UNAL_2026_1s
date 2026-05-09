
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


# Adapter para que funcione con nuestra interfaz Transporte
class EnvioAdapter(Transporte):

    def __init__(self, servicio_externo):
        self.servicio_externo = servicio_externo

    def entregar(self):
        # Llama al método del servicio externo
        return self.servicio_externo.enviar_paquete()


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
        print(logistica.planificar_entrega())
    elif opcion == "2":
        logistica = LogisticaMaritima()
        print(logistica.planificar_entrega())
    elif opcion == "3":
        servicio_externo = ServicioEnvioExterno()
        transporte_adaptado = EnvioAdapter(servicio_externo)
        print(transporte_adaptado.entregar())
    else:
        print("Opción inválida")


if __name__ == "__main__":
    main()
