# Codigo de ejemplo para el menu del CRUD

```py
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
```