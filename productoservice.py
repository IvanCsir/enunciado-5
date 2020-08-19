from repository import Repository
from producto import Producto 

class ProductoService ():
    
    def get_productosList(self):
        return Repository.productosList

    def crear_Producto(self):

        print("\n     Agregando producto"    )
        descripcion = input('Ingrese descripción: ')
        precio = int(input('Ingrese un precio: '))
        tipo = input('Ingrese el tipo de producto: ')
        return Producto(descripcion, precio, tipo)

    def add_producto(self, producto = None):
        if producto is None:
            producto.crearProducto()
        lastKey = -1
        for productKey in Repository.productosList:
            lastKey = productKey
        lastKey = lastKey + 1
        Repository.productosList[lastKey] = producto.__dict__
        return lastKey

    def update_producto(self, key):
        num = 1
        while num != 0:
            num2 = 1
            if num2 == 1:
                print("-----Modificando-----")

                descripcion = input('Introduzca la nueva descripcion: ')
                Repository.productosList[key]["_descripcion"] = descripcion
                print(Repository.productosList)

                precio = int(input('Introduzca el nuevo precio: '))
                Repository.productosList[key]["_precio"] = precio
                print(Repository.productosList)

                tipo = input('Introduzca el nuevo tipo de producto: ')
                Repository.productosList[key]["_tipo"] = tipo
                print(Repository.productosList)
            terminar = str(input("Quiere volver a corregirlo: "))
            if terminar == "no":
                break
        
    def delete_producto(self, key):
        if key not in Repository.productosList:
            raise ValueError("El producto a eliminar no existe")
        del Repository.productosList[key]