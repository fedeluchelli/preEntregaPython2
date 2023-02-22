class Producto:
    def __init__(self, producto, tienda, precio, cantidad):
        self.producto = producto
        self.tienda = tienda.title()
        self.precio = precio
        self.cantidad = cantidad
        
    def __str__(self):
        return f"{self.producto}({self.cantidad}) en la tienda {self.tienda} con un precio de ${self.precio} c/u"

