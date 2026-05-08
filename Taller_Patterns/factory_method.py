from abc import ABC, abstractmethod


# Producto abstracto
class Transporte(ABC):

    @abstractmethod
    def entregar(self):
        pass


# Productos concretos
class Camion(Transporte):

    def entregar(self):
        return "Entrega realizada por camión 🚚"


class Barco(Transporte):

    def entregar(self):
        return "Entrega realizada por barco 🚢"


# Creator (Factory Method)
class Logistica(ABC):

    @abstractmethod
    def crear_transporte(self):
        pass

    def planificar_entrega(self):
        transporte = self.crear_transporte()
        print(transporte.entregar())


# Creadores concretos
class LogisticaTerrestre(Logistica):

    def crear_transporte(self):
        return Camion()


class LogisticaMaritima(Logistica):

    def crear_transporte(self):
        return Barco()


# Aplicación de consola
def main():
    print("Seleccione tipo de logística:")
    print("1. Terrestre")
    print("2. Marítima")

    opcion = input("Opción: ")

    if opcion == "1":
        logistica = LogisticaTerrestre()
    elif opcion == "2":
        logistica = LogisticaMaritima()
    else:
        print("Opción inválida")
        return

    logistica.planificar_entrega()


if __name__ == "__main__":
    main()
