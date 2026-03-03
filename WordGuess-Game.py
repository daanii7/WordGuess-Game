#Programación de nuestro juegoXulo : woʁdＸ
##Proyecto realizado por David Orozco,Francisco Tomas Gilarte y Daniel Brescia

import random

#Variables
db = open("Lista1.txt", "r")  #abrimos el archivo de las palabras
lista1 = db.readlines()  #la lista sera las palabras de el archivo Lista1

palabra = random.choice(lista1)  #La palabra sera elegida aleatoriamente de lista1
#print(palabra)
palabra = palabra.replace('\n', '')

print("Como jugar: Debe introducir una palabra de 4 letras.")
print("Escribe en minuscula y sin usar tildes")
#print("las palabras de la lista son:")
#print(lista1)

#según la palabra elegida, le ofreceremos una pista al jugador
if palabra ==  "pavo": 
    print("Pista: ave que se asocia con las celebraciones de Acción de Gracias")
if palabra == "taco":
    print("Pista:platillo mexicano que consiste en una tortilla doblada o enrollada, rellena de carne, pollo, o vegetales, y se adereza con salsa, cebolla y cilantro.")
if palabra == "pato":
    print("Pista: ave acuática que suele nadar en lagos y ríos, y se caracteriza por su pico plano y su habilidad para volar distancias cortas.")
if palabra == "pure":
    print("Pista: alimento suave y cremoso, generalmente hecho a base de papas, que se machacan o trituran y se mezclan con mantequilla, leche o crema.")
if palabra == "polo":
    print("Pista: Es un deporte que se juega a caballo, donde los jugadores usan un mazo largo para golpear una pelota hacia la meta contraria. También es el nombre de una prenda de ropa cómoda, generalmente de manga corta.")
if palabra == "roca":
    print("Pista: tipo de Pokémon que se asocia con la dureza y la resistencia, y es eficaz contra los Pokémon de tipo fuego, volador y hielo. También es el nombre de un gimnasio que se encuentra en la región de Kanto.")
if palabra == "pino":
    print("Pista: árbol con hojas en forma de aguja, comúnmente asociado con bosques y usado en la fabricación de muebles o madera para construcción.")
if palabra == "olas":
    print("Pista: formaciones de agua que se mueven en el mar, creando un vaivén constante.")
if palabra == "rosa":
    print(" Pista: flor muy popular que puede ser de diferentes colores, y a menudo se asocia con el amor y la amistad.")
if palabra == "luna":
    print("Pista:  satélite natural , visible principalmente durante la noche, y tiene fases como llena, nueva y creciente.")
if palabra == "pele":
    print("Pista:Nombre de un icónico jugador brasileño, también usado coloquialmente para referirse a un genio del fútbol.")
if palabra == "peru":
    print("Pista:Pais con escasos recursos naturales, y es el principal productor de cafe.")
if palabra == "raul":
    print("Pista: Nombre de un legendario jugador del Real Madrid y la selección española.Es una rata se cambio de barsa al madrin")
if palabra == "liga":
    print("Pista:Competición regular de equipos en diversos deportes.")
if palabra == "bola":
    print("Pista:Objeto esférico usado en muchos deportes.")
if palabra == "copa":
    print("Pista: Trofeo otorgado en campeonatos o nombre de torneos importantes (como Copa del Rey).")
if palabra == "club":
    print("Pista: Organización de deportistas.")
if palabra == "lado":
    print("Pista: Parte o costado de algo")
if palabra == "dani":
    print("Pista:Tio muy feo que tiene los ojos feos y es italiano.")
if palabra == "casa":
    print("Pista:Lugar donde vive una familia")
if palabra == "cama":
    print("Pista:Mueble para dormir y descansar.")
if palabra == "toro":
    print("Pista:Animal fuerte y robusto, símbolo de valentía en muchas culturas.")
if palabra == "nube":
    print("Pista:Masa de vapor de agua suspendida en el cielo.")
if palabra == "vaso":
    print("Pista:Recipiente para beber líquidos")
if palabra == "foca":
    print("Pista:Mamífero marino con cuerpo alargado y aletas")
if palabra == "dado":
    print("Pista: objeto cuadrado que se utiliza para jugar al parchís sobretodo")
if palabra == "teta":
    print("Se refiere al pecho o mama femenina, en particular a la parte que produce leche en mujeres o mamíferos. En animales, también hace referencia a las glándulas mamarias.")



for i in range(0,3): #daremos 3 intentos
    intento = input("introduce una palabra: ")

    if intento == palabra: #si la palabra que escribe es la misma que la elegida aleatoriamente has ganado
        print("!Correcto¡,¡Ganaste!")
        break
    #si la palabra que escribe no es la misma que la elegida aleatoriamente puedes volver a intentarlo 
    else:
        print("has fallado, vuelve a intentarlo")
