# Uso de colecciones y cadenas
# Determina la palabra mas larga y cuantas palabras hay en total

palabras = ["programacion", "python", "variable", "lista", "diccionario", "funcion", "codigo"]

# Contamos cuantas palabras hay en la lista
total_palabras = len(palabras)

# Buscamos la palabra mas larga
palabra_mas_larga = palabras[0]

for palabra in palabras:
    if len(palabra) > len(palabra_mas_larga):
        palabra_mas_larga = palabra

print("Lista de palabras:")
print(palabras)
print("")
print("Cantidad total de palabras:", total_palabras)
print("La palabra mas larga es:", palabra_mas_larga, "con", len(palabra_mas_larga), "letras")