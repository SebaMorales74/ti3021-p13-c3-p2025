Si están utilizando los computadores de la sede, lo primero que deben hacer es configurar la terminal para utilizar la CMD y que el interpretador de Python sea el de Anaconda. Para esto, deben abrir la terminal y ejecutar el siguiente comando:

Para cambiar la versión de Python, deben de seleccionarlo desde el selector de interprete con la extensión instalada de Python en Visual Studio Code.

<img src="https://lms.inacap.cl/pluginfile.php/19507316/mod_label/intro/venv.png" alt="Selector de interprete de Python en VSCode" width="600"/>

Además, deben de establecer cómo perfil predeterminado la CMD.

<img src="https://lms.inacap.cl/pluginfile.php/19507316/mod_label/intro/default_profile.png" alt="Establecer CMD como perfil predeterminado en VSCode" width="600"/>


Comando para activar manualmente el ambiente recomando para Python actualizado en los computadores de la sede desde la cmd:
```bash
C:\ProgramData\anaconda3\Scripts\activate
```

Deben de crear un archvo .env que debe de quedar al mismo nivel que el script de Python que se conecta a la base de datos. El archivo .env debe de contener las siguientes variables de entorno con los datos correspondientes a su usuario y base de datos:

```env
ORACLE_USER=your_username
ORACLE_PASSWORD=your_password
ORACLE_DSN=your_dsn
```

Posteriormente deben de crear un script de Python que se conecte a la base de datos y cree las tablas necesarias. A continuación se muestra un ejemplo de cómo hacerlo:

```py
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
]
for query in tables:
    create_schema(query)
```