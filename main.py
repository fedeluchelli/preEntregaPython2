from paquete.paquete3 import Funciones

while True:
    print("""
        ********************************
        
        1- Agregar cliente
        2- Agregar producto
        3- Ver lista de clientes
        4- Ver lista de productos
        5- Agregar producto al carrito
        6- Eliminar producto del carrito
        7- Ver carrito de compras
        8- Comprar carrito
        9- Detalle del cliente 
        10- Salir
        
        ********************************
    """)
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        Funciones.agregar_cliente()
    elif opcion == "2":
        Funciones.agregar_producto()
    elif opcion == "3":
        Funciones.ver_clientes()
    elif opcion == "4":
        Funciones.ver_productos()
    elif opcion == "5":
        Funciones.agregar_al_carrito()
    elif opcion == "6":
        Funciones.eliminar_del_carrito()
    elif opcion == "7":
        Funciones.ver_carrito()
    elif opcion == "8":
        Funciones.comprar_carrito()
    elif opcion == "9":
        Funciones.detalle_cliente()
    elif opcion == "10":
        Funciones.salir()