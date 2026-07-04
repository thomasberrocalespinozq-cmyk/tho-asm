# Lista de deportistas y sus puntajes obtenidos
deportistas = ["Ana", "Carlos", "María", "Luis", "Sofía"]
puntajes = [85, 92, 78, 95, 88]

# Encontrar el mejor puntaje y a quién pertenece
mejor_puntaje = max(puntajes)
indice_mejor = puntajes.index(mejor_puntaje)
mejor_deportista = deportistas[indice_mejor]

# Mostrar los resultados
print("Resultados de la competencia:")
for i in range(len(deportistas)):
    print("{}: {} puntos".format(deportistas[i], puntajes[i]))

print("\nEl deportista con el mejor resultado es: {} con {} puntos".format(mejor_deportista, mejor_puntaje))