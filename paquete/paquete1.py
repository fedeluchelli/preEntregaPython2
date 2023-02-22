class Cliente:
    def __init__(self, nombre, email, edad, direccion):
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.direccion = direccion
        self.carrito = []
        self.compras = []
        
    def agregar_al_carrito(self, producto):
        self.carrito.append(producto)

    def eliminar_del_carrito(self, producto):
        self.carrito.remove(producto)

    def ver_carrito(self):
        print("Carrito de compras:")
        for producto in self.carrito:
            print("- ", producto)
        
    def comprar_carrito(self):
        self.compras.extend(self.carrito)
        self.carrito.clear()