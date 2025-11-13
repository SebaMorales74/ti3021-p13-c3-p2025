import oracledb
import os
from dotenv import load_dotenv
load_dotenv()

username = os.getenv("ORACLE_USER")
dsn = os.getenv("ORACLE_DSN")
password = os.getenv("ORACLE_PASSWORD")


def get_connection():
    return oracledb.connect(user=username, password=password, dsn=dsn)


def create_schema():

    tables = [
        (
            "CREATE TABLE"
            "PERSONAS ("
            "id INTEGER PRIMARY KEY,"
            "rut VARCHAR(8),"
            "nombres VARCHAR(64),"
            "apellidos VARCHAR(64),"
            "fecha_nacimiento DATE"
            ")"
        ),
        (
            "CREATE TABLE"
            "DEPARTAMENTO("
            "id INTEGER PRIMARY KEY,"
            "nombre VARCHAR(32),"
            "fecha_creacion DATE,"
            "habilitado BOOLEAN"
            ")"
        ),
        (
            "CREATE TABLE"
            "EMPLEADO ("
            "id INTEGER PRIMARY KEY,"
            "sueldo INTEGER,"
            "idPersona INTEGER NOT NULL,"
            "idDepartamento INTEGER NOT NULL,"
            "FOREIGN KEY (idPersona) REFERENCES PERSONAS(id),"
            "FOREIGN KEY (idDepartamento) REFERENCES DEPARTAMENTO(id)"
            ")"
        )
    ]

    for query in tables:
        try:
            with get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    print(f"Tabla creada \n {query}")
        except oracledb.DatabaseError as error:
            print(f"No se pudo crear la tabla: {error}")
