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

from datetime import datetime
def create_persona(
    id,
    rut,
    nombres,
    apellidos,
    fecha_nacimiento
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
