# Consulta rápida - Agenda de contactos
# Permite listar todos los nombres registrados en orden alfabético

contactos = {
    "Juan Perez": "099123456",
    "Maria Rodriguez": "098765432",
    "Andres Gomez": "091234567",
    "Lucia Fernandez": "097654321",
    "Carlos Diaz": "096543210"
}

# Sacamos los nombres del diccionario y los ordenamos
nombres = list(contactos.keys())
nombres.sort()

print("Lista de contactos registrados (orden alfabetico):")
print("-------------------------------------------------")

for nombre in nombres:
    numero = contactos[nombre]
    print(nombre + " - " + numero)