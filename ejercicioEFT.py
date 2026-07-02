#Funciones
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
            opcion=int(input("Ingrese opción: \n"))
            if opcion<1 or opcion>6:
                raise ValueError
            else:
                return opcion
        except ValueError
            print("Error. Ingrese un caracter válido")

def stock_categoria(categoria.lower(), dic_productos, dict_ventas):
    total_stock=0
    for key, value in dic_productos.items():
        if value[1]==categoria:
            for key2, value2 in dic_ventas.items():
                if value2[2]!=0:
                    total+=dic_ventas[key][1]                  
    print(f"El total de stock disponible es: {total_stock}  \n")

def busqueda_precio(precio_min, precio_max, dic_ventas):
    producto_correcto=[]
    for key, value in dic_ventas.items():
        if value[0]>=precio_min and value[0]<=precio_max and value[1]!=0:            
            producto_correcto.append(key)
    print(f"Los productos encontrados son: {producto_correcto}")
        
                  





#Código principal
dic_productos = {


}

dic_ventas = {


}
