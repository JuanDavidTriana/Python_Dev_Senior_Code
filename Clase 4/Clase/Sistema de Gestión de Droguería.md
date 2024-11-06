# Sistema de Gestión de Droguería

Este proyecto es una aplicación de consola en Python diseñada para gestionar el inventario y ventas de una droguería. Permite ingresar productos, actualizar el inventario tras las ventas y mostrar el total de ventas acumuladas.

## Funcionalidades

1. **Ingreso de Productos**: Permite al usuario ingresar productos al inventario inicial, incluyendo el nombre, precio y cantidad.
2. **Menú de Gestión**:
   - **Vender Producto**: El usuario puede vender un producto especificando su nombre y la cantidad. El sistema verifica la disponibilidad en el inventario y, de ser posible, realiza la venta, actualiza el inventario y acumula el total en las ventas.
   - **Mostrar Inventario**: Muestra todos los productos en el inventario actual, con su precio y cantidad disponible.
   - **Mostrar Ventas Totales**: Muestra el total acumulado de las ventas realizadas.
   - **Salir**: Cierra la aplicación.

## Uso

1. **Inicializar el Inventario**: Al iniciar el programa, el usuario debe especificar el número de productos a gestionar. A continuación, se ingresan los detalles (nombre, precio y cantidad) de cada producto.

2. **Interfaz de Menú**: El sistema muestra un menú en bucle hasta que el usuario elija salir:
   - **Opción 1** - *Vender Producto*: Permite seleccionar un producto para venta y especificar la cantidad deseada.
   - **Opción 2** - *Mostrar Inventario*: Lista todos los productos, sus precios y cantidades disponibles.
   - **Opción 3** - *Mostrar Ventas Totales*: Muestra el total de ventas acumuladas.
   - **Opción 4** - *Salir*: Finaliza la aplicación.

## Ejemplo de Ejecución

```python
# Inicializar variables
ventasTotales = 0.0

# Solicitar el número de productos
numProductos = int(input('Ingrese el número de productos a gestionar: '))

# Listas para almacenar la información
nombres = []
precios = []
cantidades = []

# Ingreso inicial de productos
for i in range(numProductos):
    nombre = input(f'Producto {i+1} - Nombre: ').lower()
    nombres.append(nombre)
    precio = float(input(f'Producto {i+1} - Precio: '))
    precios.append(precio)
    cantidad = int(input(f'Producto {i+1} - Cantidad: '))
    cantidades.append(cantidad)

# Menú principal de gestión
while True:
    print('\n--- MENU DE GESTIÓN DROGUERÍA ---')
    print('1. Vender Producto')
    print('2. Mostrar Inventario')
    print('3. Mostrar Ventas Totales')
    print('4. Salir')

    opcion = int(input('Seleccione una opción: '))

    if opcion == 1:
        nombreVenta = input('Ingrese el nombre del producto a vender: ').lower()
        cantidadVender = int(input('Ingrese la cantidad a vender: '))
        productoEncontrado = False
        for i in range(len(nombres)):
            if nombres[i] == nombreVenta:
                productoEncontrado = True
                if cantidadVender <= cantidades[i]:
                    totalVenta = cantidadVender * precios[i]
                    ventasTotales += totalVenta
                    cantidades[i] -= cantidadVender
                    print(f'Venta realizada. Total de esta venta: ${totalVenta:.2f}')
                else:
                    print(f'Cantidad insuficiente en inventario. Solo hay {cantidades[i]} unidades disponibles.')
                break
        if not productoEncontrado:
            print('Producto no encontrado en el inventario.')

    elif opcion == 2:
        print('\nInventario de Productos:')
        for i in range(len(nombres)):
            print(f'{nombres[i].capitalize()} - Precio: ${precios[i]:.2f}, Cantidad: {cantidades[i]}')

    elif opcion == 3:
        print(f'\nVentas Totales Acumuladas: ${ventasTotales:.2f}')

    elif opcion == 4:
        print('Gracias por usar el sistema de gestión de droguería.')
        break

    else:
        print('Opción inválida. Por favor ingrese una opción entre 1 y 4.')
```