from datetime import datetime

#Variables temporales
inventario = [
    ["pelota", "Juguete", 500, 20, "2023-05-15"],
    ["bola espacial", "Juguete", 300, 30, "2023-05-16"],
    ["correa", "Accesorio", 400, 10, "2023-05-17"]
]

ventas = []
ventas_totales_acumuladas = 0

while True:
    print("--- MENU DE GESTION DE MASCOTAS DEVSENIOR ---")
    print("1. Agregar un producto al inventario *")
    print("2. Vender un producto *")
    print("3. Mostrar el inventario detallado *")
    print("4. Historia de ventas")
    print("5. Mostar Ventas Totales")
    print("6. Salir")
    
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        
        print("AGREGAR UN PRODUCTO AL INVENTARIO")
        nombre = input("Ingrese el nombre del producto:").lower()
        categoria = input("Ingrese la categoria del producto: ").lower()
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto:"))
        fecha_ingreso = datetime.now().strftime("%Y-%m-%d")
        
        producto = [nombre, categoria, precio, cantidad, fecha_ingreso]
        inventario.append(producto)
        print("El producto ha sido agregado al inventario.")
        
    elif opcion == "2":
        print("VENTAS DE PRODUCTO")
        nombre = input("Ingrese el nombre del producto:").lower()
        
        producto_encontrado = False
        for producto in inventario:
            if producto[0] == nombre:
                producto_encontrado = True
                cantidad_vender = int(input("Ingrese la cantidad a vender: "))
                if producto[3] >= cantidad_vender:
                    total = producto[2] * cantidad_vender
                    producto[3] -= cantidad_vender
                    fecha_venta = datetime.now().strftime("%Y-%m-%d")
                    ventas.append([nombre, cantidad_vender, fecha_venta, total])
                    ventas_totales_acumuladas += total
                    print("Se ha vendido el producto.")
                else:
                    print("No hay suficientes productos en inventario.")
                break
        if not producto_encontrado:
            print("El producto no se encuentra en inventario.")
            
    elif opcion == "3":
        if inventario:
            print("--------------------")
            print("Inventario")
            print("--------------------")
            for producto in inventario:
                print(f"Nombre: {producto[0]}")
                print(f"Categoria: {producto[1]}")
                print(f"Precio: {producto[2]}")
                print(f"Cantidad: {producto[3]}")
                print(f"Fecha de ingreso: {producto[4]}")
                print("--------------------")
        else:
            print("El inventario esta vacio.")
    elif opcion == "4":
        if ventas:
            print("--------------------")
            print("Historia de ventas")
            print("--------------------")
            for venta in ventas:
                print(f"Nombre: {venta[0]}")
                print(f"Cantidad vendida: {venta[1]}")
                print(f"Fecha de venta: {venta[2]}")
                print(f"Total vendido: {venta[3]}")
                print("--------------------")
        else:
            print("no hay ventas registradas")
    elif opcion == "5":
        if ventas_totales_acumuladas > 0:
            print(f"Las ventas totales son: {ventas_totales_acumuladas}")
        else:
            print("No hay ventas registradas")
    elif opcion == "6" or opcion == "salir":
        print("Gracias por usar el sistema de gestion de mascotas dev senior")
        break
    else:
        print("Opcion invalida. Por favor ingrese una opcion entre 1 y 6.")