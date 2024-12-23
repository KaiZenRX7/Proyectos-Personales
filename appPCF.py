from datetime import datetime

#Sistema que gestiona inventario y ventas de una tienda 
#Para vender un producto antes debe estar ingresado en el inventario


from datetime import datetime

class Producto:
    def __init__(self, nombre, precio_unitario, cantidad):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad
        self.fecha = datetime.now()

    def costo_total(self):
        return self.precio_unitario * self.cantidad
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Precio unitario: {self.precio_unitario}, Cantidad: {self.cantidad}, Costo total: {self.costo_total()}"

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.nombre in self.productos:
            self.productos[producto.nombre].cantidad += producto.cantidad
        else:
            self.productos[producto.nombre] = producto

    def mostrar_inventario(self):
        print("Inventario actual:")
        for producto in self.productos.values():
            print(producto)

    def calcular_valor_total_inventario(self):
        return sum(producto.costo_total() for producto in self.productos.values())

class Venta:
    def __init__(self):
        self.productos_vendidos = []

    def agregar_venta(self, nombre, precio_unitario, cantidad):
        producto = Producto(nombre, precio_unitario, cantidad)
        self.productos_vendidos.append(producto)

    def mostrar_ventas_hoy(self):
        hoy = datetime.now().date()
        print(f"Fecha: {hoy.strftime('%d/%m/%Y')}")
        print("Lista de productos vendidos hoy:")
        for producto in self.productos_vendidos:
            if producto.fecha.date() == hoy:
                print(f"{producto.nombre}: Cantidad: {producto.cantidad}, Precio unitario: {producto.precio_unitario}, Total: {producto.costo_total()}")

    def calcular_total_con_descuento(self):
        total = sum(producto.costo_total() for producto in self.productos_vendidos)
        descuento = 0

        for producto in self.productos_vendidos:
            if producto.cantidad >= 200:
                descuento += producto.costo_total() * 0.20
            elif producto.cantidad >= 100:
                descuento += producto.costo_total() * 0.10
        
        return total - descuento

    def mostrar_boleta(self):
        hoy = datetime.now().date()
        print("--------------------------------")
        print("Boleta de venta PCFACTORIA:")
        print(f"Fecha: {hoy.strftime('%d/%m/%Y')}")
        print("Los productos vendidos hoy son:")
        for producto in self.productos_vendidos:
            if producto.fecha.date() == hoy:
                print(f" - {producto.nombre}: {producto.cantidad} unidades a ${producto.precio_unitario} c/u, Total: ${producto.costo_total()}")

        print(f"Total de la venta con descuentos aplicados: ${self.calcular_total_con_descuento()}")
        print("Gracias por su compra!")
        print("--------------------------------")

# Ejecución del programa
inventario = Inventario()
venta = Venta()

while True:
    print("Menú de opciones:")
    print("1. Venta")
    print("2. Agregar producto a inventario")
    print("3. Calcular inventario")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        while True:
            nombre = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
            if nombre.lower() == "fin":
                break

            if nombre not in inventario.productos:
                print(f"El producto {nombre} no está en el inventario.")
                continue

            precio_unitario = inventario.productos[nombre].precio_unitario
            cantidad_disponible = inventario.productos[nombre].cantidad
            cantidad = int(input(f"Ingrese la cantidad a vender de {nombre} (Disponible: {cantidad_disponible}): "))

            if cantidad > cantidad_disponible:
                print(f"No hay suficiente cantidad de {nombre}. Solo hay {cantidad_disponible} disponible.")
            else:
                inventario.productos[nombre].cantidad -= cantidad
                venta.agregar_venta(nombre, precio_unitario, cantidad)

        # Mostrar boleta con el resumen de la venta
        venta.mostrar_boleta()
    elif opcion == "2":
        nombre = input("Ingrese el nombre del producto: ")
        precio_unitario = int(input(f"Ingrese el precio unitario de {nombre}: "))
        cantidad = int(input(f"Ingrese la cantidad disponible de {nombre}: "))

        producto = Producto(nombre, precio_unitario, cantidad)
        inventario.agregar_producto(producto)
        print(f"Producto {nombre} agregado al inventario.")
    elif opcion == "3":
        inventario.mostrar_inventario()
        print(f"Valor total del inventario: {inventario.calcular_valor_total_inventario()}")
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")



