
def menu():
    print("============== MENÚ PRINCIPAL ==============")
    print("1. Stock por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio del producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("============================================")

def leer_opcion():
    while True:
        try:
            opcion=int(input("Qué desea hacer?"))
            if opcion<1 or opcion>6:
                raise ValueError
            else:
                return opcion
        except ValueError
            print("Error. Ingrese un caracter válido")

def stock_categoria(categoria.upper(), dic_product, dict_ventas):
    for key, value in dic_product.items():
        if value[1]==categoria:
            for key2, value2 in dic_ventas.items():
                if value[2]>=1:
                    print("

      
                  






dic_product={
    }

dic_ventas={
    }

    }
