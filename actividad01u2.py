"""
Declarar las clases y atributos del diagrama
fabricado para la evaluación sumativa
de la unidad 1 de programacion orientada a objetos
"""


class Cliente:
    def __init__(self, rut: str, nombre: str, email: str):
        self.__rut: str = rut
        self.__nombre: str = nombre
        self.__email: str = email


class Producto:
    def __init__(self, cod_barra: str, nombre: str, precio: float, stock: int):
        self._cod_barra: str = cod_barra
        self._nombre: str = nombre
        self._precio: float = precio
        self._stock: int = stock


class Venta:
    def __init__(self, cliente: Cliente, productos: list[Producto]):
        self._cliente: Cliente = cliente
        self._productos: list[Producto] = productos
