"""
Declarar las clases y atributos del diagrama
fabricado para la evaluación sumativa
de la unidad 1 de programacion orientada a objetos
"""
# import re


class Persona:
    def __init__(self, rut: str, nombre: str, email: str):
        self._rut: str = rut
        self._nombre: str = nombre
        self._email: str = email

    @property
    def rut(self):
        return self._rut

    @property
    def nombre(self):
        return self._nombre

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email: str):
        if not email:
            raise ValueError("Tienes que ingresar un email")

        # En caso de querer validar el formato del correo:
        # esValido = re.match(
        #     r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
        # if not esValido:
        #     raise ValueError("El correo no es valido")

        self._email = email


class Cliente:
    def __init__(self):
        self.__puntos_cmr: int = 0

    @property
    def puntos_cmr(self):
        return self.__puntos_cmr
    
    def __str__(self):
        return f"{self.__puntos_cmr}"


class Vendedor:
    def __init__(self, region: str, departamento: str):
        self.__region = region
        self.__departamento = departamento

    @property
    def region(self):
        return self.__region

    @property
    def departamento(self):
        return self.__departamento
    
    def __str__(self):
        return f"{self.__region} {self.__departamento}"


class Producto:
    def __init__(self, cod_barra: str, nombre: str, precio: float, stock: int):
        self._cod_barra: str = cod_barra
        self._nombre: str = nombre
        self._precio: float = precio
        self._stock: int = stock

    @property
    def cod_barra(self):
        return self._cod_barra

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @property
    def stock(self):
        return self._stock
    
    def __str__(self):
        return f"{self._cod_barra} {self._nombre} {self._precio}"


class Venta:
    def __init__(self, cliente: Cliente, vendedor: Vendedor, productos: list[Producto]):
        self.__cliente: Cliente = cliente
        self.__vendedor: Vendedor = vendedor
        self.__productos: list[Producto] = productos

    @property
    def cliente(self):
        return self.__cliente

    @property
    def vendedor(self):
        return self.__vendedor

    @property
    def productos(self):
        return self.__productos
    
    def imprimir_a_pdf(self):
        print(f"Cliente: {self.__cliente}")
        print(f"Vendedor: {self.__vendedor}")
        print("Lista de productos:")
        for producto in self.__productos:
            print(f"{producto}")


# Ejemplo práctico utilizando las clases
if __name__ == "__main__":
    # Crear cliente
    cliente1 = Cliente()
    print(f"Cliente creado con puntos CMR: {cliente1.puntos_cmr}")
    
    # Crear vendedor
    vendedor1 = Vendedor("Región Metropolitana", "Electrónica")
    print(f"Vendedor de {vendedor1.departamento} en {vendedor1.region}")
    
    # Crear productos
    producto1 = Producto("1234567890", "Laptop Dell", 850000.0, 5)
    producto2 = Producto("0987654321", "Mouse Inalámbrico", 25000.0, 20)
    producto3 = Producto("1122334455", "Teclado Mecánico", 75000.0, 10)
    
    print("\nProductos disponibles:")
    productos = [producto1, producto2, producto3]
    for prod in productos:
        print(f"- {prod.nombre}: ${prod.precio:,.0f} (Stock: {prod.stock})")
    
    # Crear venta
    productos_venta = [producto1, producto2]  # Cliente compra laptop y mouse
    venta1 = Venta(cliente1, vendedor1, productos_venta)
    
    # Ejemplo de impresión a PDF (simulado)
    print(f"\n--- IMPRESIÓN A PDF ---")
    venta1.imprimir_a_pdf()
    

