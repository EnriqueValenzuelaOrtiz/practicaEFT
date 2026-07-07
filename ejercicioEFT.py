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

def stock_categoria(categoria, dic_productos, dict_ventas):
    total_stock=0
    for key, value in dic_productos.items():
        if value[1]==categoria.lower():
            for key2, value2 in dic_ventas.items():
                if value2[2]!=0:
                    total+=dic_ventas[key][1]                  
    print(f"El total de stock disponible es: {total_stock}  \n")

def busqueda_precio(precio_min, precio_max, dic_ventas, dic_productos):
    lista_producto_correcto=[]
    for key, value in dic_ventas.items():
        if value[0]>=precio_min and value[0]<=precio_max and value[1]!=0:            
            producto_correcto=dic_productos[key][0]
            lista_producto_correcto.append(f"{producto_correcto}--{key}")

    if len(lista_producto_correcto)==0:
        print("No hay productos en ese rango de precios.")

    else:
        lista_producto_correcto_ordenado= sorted(lista_producto_correcto)
        print(f"Los productos encontrados son: {lista_producto_correcto_ordenado}")
    


    
def actualizar_precio(codigo, nuevo_precio, dic_ventas):
    if buscar_codigo(codigo, dic_ventas):
        dic_ventas[codigo][0]=nuevo_precio
        return True
    else:
        return False


    






def buscar_codigo(codigo, dic_ventas):
    return codigo in ventas


def agregar_producto


def validar_codigo(codigo, dic_productos):
    if codigo.strip()!="" and codigo in dic_productos:
        return True
    else:
        return False
    


        
                  





#Código principal
dic_productos = {


}

dic_ventas = {


}
