# coding: utf-8
# Programa que imprime en un fichero externo el menú diario

#función que introduce en dos cadenas los platos y precios introducidos
def intromenu(comida, precio):
    while True:
        comida.append(raw_input("Introduzca plato: "))
        precio.append(raw_input("Introduzca precio: "))
        pregunta = raw_input("¿Quiere introducir otro plato? s/n: ")
        if pregunta == "n" or pregunta == "no":
            break

#función que imprime el menú del día en fichero de texto, situándose para escribir a partir de la última posición conocida
def impmenu (comida, precio, tipo):
    menu.write(tipo + "\n")
    for i in range(len(precio)):
        posicion = menu.tell()
        menu.seek(posicion)
        menu.write(comida[i] + " ----------- " + precio[i] + "€" + "\n")

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
menu = open("menu.txt", "w+")
impmenu(primeros, precio_primeros, "Primeros Platos")
impmenu(segundos, precio_segundos, "Segundos Platos")
impmenu(postres, precio_postres, "Postres")
menu.close()



