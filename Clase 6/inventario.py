from prettytable import PrettyTable

inventario = {
    "23232DX" : {
        "nombre_producto" : "Kit arrastre",
        "modelo": "125",
        "cantidad": 5,
        "fecha de ingreso": "2023-05-15",
        "fecha de ultima venta" : "2024-11-12"
    },
    "23232D2" : {
        "nombre_producto" : "Kit arrastre 2",
        "modelo": "123",
        "cantidad": 1,
        "fecha de ingreso": "2023-05-15",
        "fecha de ultima venta" : "2024-11-12"
    },
}

def crear_producto():
    pass

def mostar_inventario():
    if inventario:
        table = PrettyTable()
        table.field_names = ["Serial", "modelo", "cantidad", "fecha de ingreso","fecha de ultima venta"]
        print("=========Inventario========")
        for producto in inventario:
            table.add_row([producto, 
                        inventario[producto]["modelo"], 
                        inventario[producto]["cantidad"],
                        inventario[producto]["fecha de ingreso"],
                        inventario[producto]["fecha de ultima venta"],
                        ], divider=True)
        print(table)
    else:
        print("El inventario esta vacio")

def actualizar_inventario():
    pass

def eliminar_producto():
    mostar_inventario()
    opcionEliminar = input("Ingrese serial a eliminar:")
    if opcionEliminar in inventario:
        del inventario[opcionEliminar]

def main():
    
    while True:
        print("Bienvenido al inventario")
        print("1. Mostar inventario")
        print("2. Crear producto")
        print("3. Actualizar inventario")
        print("4. Eliminar producto")
        print("5. Salir")
        opcion = input("Seleccione una opcion:")
        
        if opcion == "1":
            mostar_inventario()
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            break
        else:
            print("Opcion invalida.")

main()