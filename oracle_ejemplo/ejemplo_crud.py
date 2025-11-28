from datetime import datetime
import oracledb
import os
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

username = os.getenv("ORACLE_USER")
dsn = os.getenv("ORACLE_DSN")
password = os.getenv("ORACLE_PASSWORD")


def get_connection():
    return oracledb.connect(user=username, password=password, dsn=dsn)


def create_schema(query):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                print(f"Tabla creada \n {query}")
    except oracledb.DatabaseError as error:
        print(f"No se pudo crear la tabla: {error}")


def create_all_tables():
    tables = [
        (
            "CREATE TABLE PERSONAS ("
            "id INTEGER PRIMARY KEY,"
            "rut VARCHAR(8),"
            "nombres VARCHAR(64),"
            "apellidos VARCHAR(64),"
            "fecha_nacimiento DATE"
            ")"
        ),
        (
            "CREATE TABLE DEPARTAMENTOS("
            "id INTEGER PRIMARY KEY,"
            "nombre VARCHAR(32),"
            "fecha_creacion DATE"
            ")"
        ),
        (
            "CREATE TABLE EMPLEADOS ("
            "id INTEGER PRIMARY KEY,"
            "sueldo INTEGER,"
            "idPersona INTEGER NOT NULL UNIQUE,"
            "idDepartamento INTEGER NOT NULL,"
            "FOREIGN KEY (idPersona) REFERENCES PERSONAS(id),"
            "FOREIGN KEY (idDepartamento) REFERENCES DEPARTAMENTOS(id)"
            ")"
        ),
    ]

    for query in tables:
        create_schema(query)


# CREATE - Inserción de datos
def create_persona(
    id: int, rut: str, nombres: str, apellidos: str, fecha_nacimiento: str
):
    sql = (
        "INSERT INTO PERSONAS(id,rut,nombres,apellidos,fecha_nacimiento)"
        "VALUES (:id,:rut,:nombres,:apellidos,:fecha_nacimiento)"
    )

    parametros = {
        "id": id,
        "rut": rut,
        "nombres": nombres,
        "apellidos": apellidos,
        "fecha_nacimiento": datetime.strptime(fecha_nacimiento, "%d-%m-%Y"),
    }

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Inserción de datos correcta")
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error} \n {sql} \n {parametros}")


def create_departamento(id, nombre, fecha_creacion):
    sql = (
        "INSERT INTO DEPARTAMENTOS(id,nombre,fecha_creacion)"
        "VALUES (:id,:nombre,:fecha_creacion)"
    )

    parametros = {
        "id": id,
        "nombre": nombre,
        "fecha_creacion": datetime.strptime(fecha_creacion, "%d-%m-%Y"),
    }

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Inserción de datos correcta")
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error} \n {sql} \n {parametros}")


def create_empleado(id, sueldo, idPersona, idDepartamento):
    sql = (
        "INSERT INTO EMPLEADOS (id,sueldo,idPersona,idDepartamento)"
        "VALUES (:id,:sueldo,:idPersona,:idDepartamento)"
    )

    parametros = {
        "id": id,
        "sueldo": sueldo,
        "idPersona": idPersona,
        "idDepartamento": idDepartamento,
    }

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Inserción de datos correcta")
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato \n {error} \n {sql} \n {parametros}")


# READ - Lectura de datos
def read_personas():
    sql = "SELECT * FROM PERSONAS"

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                print(sql)
                resultados = cursor.execute(sql)
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as error:
        print(f"No se pudo ejecutar la query {error} \n {sql}")


def read_persona_by_id(id: int):
    sql = "SELECT * FROM PERSONAS WHERE id = :id"
    parametros = {"id": id}

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                print(sql, parametros)
                resultados = cursor.execute(sql, parametros)
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as error:
        print(f"No se pudo ejecutar la query {error} \n {sql} \n {parametros}")


def read_departamentos():
    sql = "SELECT * FROM DEPARTAMENTOS"

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                print(sql)
                resultados = cursor.execute(sql)
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as error:
        print(f"No se pudo ejecutar la query {error} \n {sql}")


def read_departamento_by_id(id: int):
    sql = "SELECT * FROM DEPARTAMENTOS WHERE id = :id"
    parametros = {"id": id}

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                print(sql, parametros)
                resultados = cursor.execute(sql, parametros)
                if len(resultados) == 0:
                    return print(f"No hay registros con el ID {id}")
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as error:
        print(f"No se pudo ejecutar la query {error} \n {sql} \n {parametros}")


def read_empleados():
    sql = "SELECT * FROM EMPLEADOS"

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                print(sql)
                resultados = cursor.execute(sql)
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as error:
        print(f"No se pudo ejecutar la query {error} \n {sql}")


def read_empleado_by_id(id: int):
    sql = "SELECT * FROM EMPLEADOS WHERE id = :id"
    parametros = {"id": id}

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                print(sql, parametros)
                resultados = cursor.execute(sql, parametros)
                if len(resultados) == 0:
                    return print(f"No hay registros con el ID {id}")
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as error:
        print(f"No se pudo ejecutar la query {error} \n {sql} \n {parametros}")


# UPDATE - Actualización de datos
def update_persona(
    id: int,
    rut: Optional[str] = None,
    nombres: Optional[str] = None,
    apellidos: Optional[str] = None,
    fecha_nacimiento: Optional[str] = None,
):
    modificaciones = []
    parametros = {"id": id}

    if rut is not None:
        modificaciones.append("rut =: rut")
        parametros["rut"] = rut
    if nombres is not None:
        modificaciones.append("nombres =: nombres")
        parametros["nombres"] = nombres
    if apellidos is not None:
        modificaciones.append("apellidos =: apellidos")
        parametros["apellidos"] = apellidos
    if fecha_nacimiento is not None:
        modificaciones.append("fecha_nacimiento =: fecha_nacimiento")
        parametros["fecha_nacimiento"] = datetime.strptime(fecha_nacimiento, "Y%-m%-d%")
    if not modificaciones:
        return print("No has enviado datos por modificar")

    sql = f"UPDATE PERSONAS SET { ", ".join(modificaciones) } WHERE id =: id"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
        conn.commit()
        print(f"Dato con ID={id} actualizado.")


def update_departamento(
    id: int, nombre: Optional[str] = None, fecha_creacion: Optional[str] = None
):
    modificaciones = []
    parametros = {"id": id}

    if nombre is not None:
        modificaciones.append("nombre =: nombre")
        parametros["nombre"] = nombre
    if fecha_creacion is not None:
        modificaciones.append("fecha_creacion =: fecha_creacion")
        parametros["fecha_creacion"] = datetime.strptime(fecha_creacion, "Y%-m%-d%")
    if not modificaciones:
        return print("No has enviado datos por modificar")

    sql = f"UPDATE DEPARTAMENTOS SET { ", ".join(modificaciones) } WHERE id =: id"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
        conn.commit()
        print(f"Dato con ID={id} actualizado.")


def update_empleado(
    id: int,
    sueldo: Optional[int],
    idPersona: Optional[int],
    idDepartamento: Optional[int],
):
    modificaciones = []
    parametros = {"id": id}

    if sueldo is not None:
        modificaciones.append("sueldo =: sueldo")
        parametros["sueldo"] = sueldo
    if idPersona is not None:
        modificaciones.append("idPersona =: idPersona")
        parametros["idPersona"] = idPersona
    if idDepartamento is not None:
        modificaciones.append("idDepartamento =: idDepartamento")
        parametros["idDepartamento"] = idDepartamento
    if not modificaciones:
        return print("No has enviado datos por modificar")

    sql = f"UPDATE EMPLEADOS SET { ", ".join(modificaciones) } WHERE id =: id"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
        conn.commit()
        print(f"Dato con ID={id} actualizado.")


# DELETE - Eliminacion de datos
def delete_persona(id: int):
    sql = "DELETE FROM PERSONAS WHERE id = :id"
    parametros = {"id": id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato eliminado \n {parametros}")
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")


def delete_departamento(id: int):
    sql = "DELETE FROM DEPARTAMENTOS WHERE id = :id"
    parametros = {"id": id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato eliminado \n {parametros}")
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")


def delete_empleado(id: int):
    sql = "DELETE FROM EMPLEADOS WHERE id = :id"
    parametros = {"id": id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"Dato eliminado \n {parametros}")
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")


def menu_personas():
    while True:
        os.system("cls")
        print(
            """
                ====================================
                |         Menu: Personas           |
                |----------------------------------|
                | 1. Insertar un dato              |
                | 2. Consultar todos los datos     |
                | 3. Consultar dato por ID         |
                | 4. Modificar un dato             |
                | 5. Eliminar un dato              |
                | 0. Volver al menu principal      |
                ====================================
            """
        )
        opcion = input("Elige una opción [1-5, 0]: ")
        if opcion == "1":
            os.system("cls")
            print("1. Insertar un dato")
            id = input("Ingrese id de la persona: ")
            rut = input("Ingrese rut de la persona: ")
            nombres = input("Ingrese nombres de la persona: ")
            apellidos = input("Ingrese apellidos de la persona: ")
            fecha_nacimiento = input("Ingrese fecha de nacimiento de la persona: ")
            create_persona(id, rut, nombres, apellidos, fecha_nacimiento)
            input("Ingrese ENTER para continuar...")
        elif opcion == "2":
            os.system("cls")
            print("2. Consultar todos los datos")
            read_personas()
            input("Ingrese ENTER para continuar...")
        elif opcion == "3":
            os.system("cls")
            print("3. Consultar dato por ID ")
            id = input("Ingrese id de la persona: ")
            read_persona_by_id(id)
            input("Ingrese ENTER para continuar...")
        elif opcion == "4":
            os.system("cls")
            print("4. Modificar un dato")
            id = input("Ingrese id de la persona: ")
            print("[Sólo ingrese los datos a modificar de la persona]")
            rut = input("Ingrese rut de la persona (opcional): ")
            nombres = input("Ingrese nombres de la persona (opcional): ")
            apellidos = input("Ingrese apellidos de la persona (opcional): ")
            fecha_nacimiento = input("Ingrese fecha de nacimiento de la persona (opcional): ")
            if len(rut.strip()) == 0: rut = None
            if len(nombres.strip()) == 0: nombres = None
            if len(apellidos.strip()) == 0: apellidos = None
            if len(fecha_nacimiento.strip()) == 0: fecha_nacimiento = None
            update_persona(id, rut, nombres, apellidos, fecha_nacimiento)
            input("Ingrese ENTER para continuar...")
        elif opcion == "5":
            os.system("cls")
            print("5. Eliminar un dato")
            id = input("Ingrese id de la persona: ")
            delete_persona(id)
            input("Ingrese ENTER para continuar...")
        elif opcion == "0":
            os.system("cls")
            print("Volviendo al menú principal...")
            break
        else:
            os.system("cls")
            print("Opción incorrecta, intente nuevamente.")
            input("Ingrese ENTER para continuar...")


def main():
    while True:
        os.system("cls")
        print(
            """
                ====================================
                |     CRUD: Oracle + Python        |
                |----------------------------------|
                | 1. Crear todas las tablas        |
                | 2. Gestionar tabla Personas      |
                | 3. Gestionar tabla Departamentos |
                | 4. Gestionar tabla Empleado*     |
                | 0. Salir del sistema             |
                |----------------------------------|
                | * La tabla empleado necesita al  |
                | menos un registro creado en la   |
                | tabla Personas y Departamentos.  |
                ====================================
            """
        )
        opcion = input("Elige una opción [1-4, 0]: ")

        if opcion == "1":
            os.system("cls")
            create_all_tables()
            input("Ingrese ENTER para continuar...")
        elif opcion == "2":
            menu_personas()
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "0":
            pass
        else:
            os.system("cls")
            print("Opción incorrecta, intente nuevamente.")
            input("Ingrese ENTER para continuar...")


if __name__ == "__main__":
    main()
