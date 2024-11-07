#inicializar variables
ventasTotales = 0.0

#solicitar el numero de productos
numProductos = int(input('Ingrese el numero de productos a gestionar: '))

#listas para almacenar la informacion
nombres = []
precios = []
cantidades = []

print('Ingreso inicial de productos a la tienda: ')
for i in range(numProductos):
    print(f'Producto {i+1}: ')
    nombre = input('Ingrese el nombre del producto: ').lower()
    nombres.append(nombre)
    precio = float(input('Digite el precio del producto: '))
    precios.append(precio)
    cantidad = int(input('Digite el cantidad del producto: '))
    cantidades.append(cantidad)
    
#ciclo principal menu
while True:
    print('\n ---MENU DE GESTION DROGUERIA---')
    print('1. Vender Producto')
    print('2. Mostrar Inventario')
    print('3. Mostrar Ventas Totales')
    print('4. Salir')
    
    
    #leer la opcion del usuario
    opcion = int(input('Ingrese una opcion: '))
    
    #vender producto
    if opcion == 1:
        print('\nVender Producto')
        nombreVenta = input('Ingrese el nombre del producto a vender: ').lower()
        cantidadVender = int(input('Ingrese la cantidad a vender: '))
        productoEncontrado = False
        #recorrer la lista de productos
        for i in range(len(nombres)):
            if nombres[i] == nombreVenta:
                #verificar si hay suficiente cantidad en inventario
                productoEncontrado = True
                if cantidadVender <= cantidades[i]:
                    #calcular el total de la venta
                    totalVenta = cantidadVender * precios[i]
                    #agregar el total a las ventas totales
                    ventasTotales += totalVenta
                    #restar la cantidad vendida al inventario
                    cantidades[i] -= cantidadVender
                    print(f'Venta realizada. total de esta venta ${totalVenta:.2f}')
                    print(f'Quedan { cantidades[i]} unidades de {nombres[i]} en el inventario')
                else:
                    print(f'cantidad insuficiente en inventario. ya que en stock solo tenemos {cantidades[i]}')
                break
        #si no se encontro el producto
        if not productoEncontrado:
            print('Producto no encontrado en el inventario')
    
    #mostrar inventario
    elif opcion == 2:
        print('\nInventario de Productos')
        for i in range(len(nombres)):
            print(f'Producto {i+1}: {nombres[i].capitalize()}, Precio: ${precios[i]:.2f}, Cantidad: {cantidades[i]}')

    #mostrar ventas totales
    elif opcion == 3:
        print(f'\nVentas totales acumuladas: ${ventasTotales:.2f}')
    #salir del programa
    elif opcion == 4:
        print('gracias por usar el sistema de gestion drogueria dev senior')
        break
    
    else:
        print('opcion invalida. ingresar entre (1-4)')


