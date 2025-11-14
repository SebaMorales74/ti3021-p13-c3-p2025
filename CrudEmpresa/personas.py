from .db import get_connection

from datetime import datetime
def create_persona(id: int, rut: str, nombres: str, apellidos: str, fecha_nacimiento: str):
    sql = (
    "INSERT INTO personas (id, rut, nombres, apellidos, fecha_nacimiento) "
    "VALUES (:id, :rut, :nombres, :apellidos, :fecha_nacimiento)"
    )
    bind_fecha = None
    if fecha_nacimiento:
        bind_fecha = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")

        parametros = {
                "id": id,
                "rut": rut,
                "nombres": nombres,
                "apellidos": apellidos,
                "fecha_nacimiento": bind_fecha
                }
        
        print(parametros)

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()

    print(f"Persona con RUT={rut} creada.")
