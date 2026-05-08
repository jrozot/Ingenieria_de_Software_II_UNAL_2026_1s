class Configuracion:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            print("Creando instancia única...")
            cls._instancia = super().__new__(cls)
            cls._instancia.modo = "Producción"
        return cls._instancia

    def mostrar_configuracion(self):
        print(f"Modo actual: {self.modo}")


def main():
    config1 = Configuracion()
    config2 = Configuracion()

    config1.mostrar_configuracion()

    config2.modo = "Desarrollo"

    config1.mostrar_configuracion()
    config2.mostrar_configuracion()

    # Verificación
    if config1 is config2:
        print("Singleton funcionando: ambas variables son la misma instancia")


if __name__ == "__main__":
    main()
