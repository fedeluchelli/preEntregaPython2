from paquete.paquete1 import Cliente
from paquete.paquete2 import Producto
import json


clientes = []
productos = []

class Funciones:
    def agregar_cliente():
        nombre = input("\nIngrese el nombre del cliente: ")
        email = input("Ingrese el email del cliente: ")
        edad = input("Ingrese la edad del cliente: ")
        direccion = input("Ingrese la dirección del cliente: ")
        cliente = Cliente(nombre, email, edad, direccion)
        clientes.append(cliente)
        print(f"\n\nSe ha agregado al cliente - {nombre} - al sistema.")

    def ver_clientes():
        print("\nLista de clientes:")
        for cliente in clientes:
            print(f"\n_ {cliente.nombre} - {cliente.email}")          
            
    def agregar_producto():
        producto = input("\nIngrese el nombre del producto: ")
        tienda = input("Ingrese el nombre de la tienda: ")
        precio = input("Ingrese el precio del producto: ")
        cantidad = input("Ingrese la cantidad del producto: ")
        producto = Producto(producto, tienda, precio, cantidad)
        productos.append(producto)
        print(f"\nSe ha agregado al sistema {producto}.")

    def ver_productos():
        print("\nLista de productos:\n")
        for producto in productos:
            print(f"\n_ {producto.producto}({producto.cantidad}) / {producto.tienda}")

    def agregar_al_carrito():
        cliente = input("\nIngrese el nombre del cliente: ")
        for c in clientes:
            if c.nombre == cliente:
                producto = input("\nIngrese el nombre del producto: ")
                for p in productos:
                    if p.producto == producto:
                        c.agregar_al_carrito(p)
                        print(f"\n\nSe ha agregado el producto {producto} al carrito de {cliente}")
                        return
                print("\nProducto no encontrado.")
                return
        print("\n\nCliente no encontrado.")

    def eliminar_del_carrito():
        cliente = input("\nIngrese el nombre del cliente: ")
        producto = input("Ingrese el nombre del producto: ")
        for c in clientes:
            if c.nombre == cliente:
                for p in c.carrito:
                    if p.producto == producto:
                        c.eliminar_del_carrito(p)
                        print(f"\nSe ha eliminado el producto {producto} del carrito de {cliente}.")
                        return
                print("Producto no encontrado en el carrito.")
                return
        print("Cliente no encontrado.")

    def ver_carrito():
        cliente = input("\nIngrese el nombre del cliente: ")
        for c in clientes:
            if c.nombre == cliente:
                c.ver_carrito()
                return
        print("Cliente no encontrado.")

    def comprar_carrito():
        cliente = input("\nIngrese el nombre del cliente: ")
        for c in clientes:
            if c.nombre == cliente:
                confirmar = input(f"\n{c.nombre} querés confirmar la compra de los productos en tu carrito? \n\n1 = SÍ / 2 = NO\n")
                if confirmar == "1":
                    print(f"\n\nCompra realizada con éxito!\nEnviaremos la factura a {c.email}\n\nMuchas gracias!")
                else:
                    print("Compra no finalizada.") 
                return
        print("Cliente no encontrado.")
        
    def detalle_cliente():
        cliente = input("\nIngrese el nombre del cliente: ")
        for c in clientes:
            if c.nombre == cliente:
                print(f"""
          -Nombre:    {c.nombre}
          -Edad:      {c.edad}
          -Dirección: {c.direccion}
          -Email:     {c.email}
                      """)
                break    
            else:
                print("Cliente no encontrado.")
                

    def salir():
        print("\n\nSaliendo del programa...")
        exit()