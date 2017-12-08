# coding: utf-8
# Programa que imprime en un fichero externo el menú diario

#función que introduce en dos cadenas los platos y precios introducidos
def intromenu(comida, precio):
    while True:
        comida.append(raw_input("Introduzca plato: "))
        precio.append(raw_input("Introduzca precio: "))
        pregunta = raw_input("¿Quiere introducir otro primer plato? s/n: ")
        if pregunta == "n" or pregunta == "no":
            break

#función que imprime el menú del día en fichero de texto, situándose para escribir a partir de la última posición conocida
def impmenu (comida, precio):
    menu = open("menu.txt", "w+")
    posicion = menu.tell()
    for i in range(len(precio)):
        menu.seek(posicion)
        menu.write("\n" + comida[i] + " ----------- " + precio[i] + "€")
    menu.close()


#primeros platos
print ("Introduzca primeros platos y sus precios")
primeros = []
precio_primeros = []
intromenu (primeros, precio_primeros)


#segundos platos
print ("Introduzca segundos platos y sus precios")
segundos = []
precio_segundos = []
intromenu (segundos, precio_segundos)

#postres
print ("Introduzca postres y sus precios")
postres = []
precio_postres = []
intromenu (postres, precio_postres)


#Impresión
impmenu(primeros, precio_primeros)
impmenu(segundos, precio_segundos)
impmenu(postres, precio_postres)




