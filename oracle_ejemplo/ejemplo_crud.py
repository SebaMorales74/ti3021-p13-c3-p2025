from datetime import datetime
import oracledb
import os
from dotenv import load_dotenv
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
        "CREATE TABLE DEPARTAMENTO("
        "id INTEGER PRIMARY KEY,"
        "nombre VARCHAR(32),"
        "fecha_creacion DATE"
        ")"
    ),
    (
        "CREATE TABLE EMPLEADO ("
        "id INTEGER PRIMARY KEY,"
        "sueldo INTEGER,"
        "idPersona INTEGER NOT NULL UNIQUE,"
        "idDepartamento INTEGER NOT NULL,"
        "FOREIGN KEY (idPersona) REFERENCES PERSONAS(id),"
        "FOREIGN KEY (idDepartamento) REFERENCES DEPARTAMENTO(id)"
        ")"
    )
]

for query in tables:
    create_schema(query)

# CREATE - Inserción de datos
def create_persona(
    id: int,
    rut: str,
    nombres: str,
    apellidos: str,
    fecha_nacimiento: str
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
        "fecha_nacimiento": datetime.strptime(fecha_nacimiento, '%d-%m-%Y')
    }

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Inserción de datos correcta")
    except oracledb.DatabaseError as error:
        print(
            f"No se pudo insertar el dato \n {error} \n {sql} \n {parametros}")

def create_departamento(
    id,
    nombre,
    fecha_creacion
):
    sql = (
        "INSERT INTO DEPARTAMENTO(id,nombre,fecha_creacion)"
        "VALUES (:id,:nombre,:fecha_creacion)"
    )

    parametros = {
        "id": id,
        "nombre": nombre,
        "fecha_creacion": datetime.strptime(fecha_creacion, '%d-%m-%Y')
    }

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Inserción de datos correcta")
    except oracledb.DatabaseError as error:
        print(
            f"No se pudo insertar el dato \n {error} \n {sql} \n {parametros}")

def create_empleado(
    id,
    sueldo,
    idPersona,
    idDepartamento
):
    sql = (
        "INSERT INTO EMPLEADO(id,sueldo,idPersona,idDepartamento)"
        "VALUES (:id,:sueldo,:idPersona,:idDepartamento)"
    )

    parametros = {
        "id": id,
        "sueldo": sueldo,
        "idPersona": idPersona,
        "idDepartamento": idDepartamento
    }

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Inserción de datos correcta")
    except oracledb.DatabaseError as error:
        print(
            f"No se pudo insertar el dato \n {error} \n {sql} \n {parametros}")

# READ - Lectura de datos
def read_personas():
    sql = (
        "SELECT * FROM PERSONAS"
    )

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
    sql = (
        "SELECT * FROM PERSONAS WHERE id = :id"
    )
    parametros = {"id" : id}

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

def read_departamentos():
    sql = (
        "SELECT * FROM DEPARTAMENTOS"
    )

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
    sql = (
        "SELECT * FROM DEPARTAMENTOS WHERE id = :id"
    )
    parametros = {"id" : id}

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
    sql = (
        "SELECT * FROM EMPLEADOS"
    )

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
    sql = (
        "SELECT * FROM EMPLEADOS WHERE id = :id"
    )
    parametros = {"id" : id}

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
