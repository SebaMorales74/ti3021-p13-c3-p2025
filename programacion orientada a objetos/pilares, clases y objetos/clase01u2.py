class Participante:
    def __init__(self, rut: str, nombre: str, edad: int):
        self._rut: str = rut
        self._nombre: str = nombre
        self._edad: int = edad

    def presentarse(self) -> str:
        return f"Hola mi nombre es {self._nombre} y mi edad es {self._edad}"

    def __str__(self):
        return f"{self._rut} {self._nombre} {self._edad}"


participante1 = Participante(
    rut="19567387-K",
    nombre="Felipe Villaroel",
    edad=24
)

participante2 = Participante(
    rut="9845627-K",
    nombre="Cesar Silva",
    edad=19
)


print(
    participante1.presentarse()
)

print(
    participante2.presentarse()
)

