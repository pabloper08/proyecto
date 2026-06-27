import random

print("--- ¡EL REY DEL CHISTE! ---")

# --- LEER EL ARCHIVO DE CHISTES (FORMA BÁSICA) ---
archivo = open("chistes.txt", "r", encoding="utf-8")
chistes = []

for linea in archivo:
    chiste_limpio = linea.strip()#linea.strip() elimina los espacios en blanco al inicio y al final de la línea
    if chiste_limpio != "":
        chistes.append(chiste_limpio)

archivo.close()

# Seleccionar un chiste al azar usando random.randint
indice_aleatorio = random.randint(0, len(chistes) - 1)
chiste_elegido = chistes[indice_aleatorio]

# Separar la pregunta del remate usando el guion bajo (_)
if "_" in chiste_elegido:
    partes = chiste_elegido.split("_")
    pregunta = partes[0].strip()
    remate = partes[1].strip()
else:
    pregunta = chiste_elegido
    remate = "¡Jajaja!"

# Mostrar la pregunta del chiste
print("\nPregunta: " + pregunta)

# El usuario escribe lo que quiera (no importa el contenido)
input("\nEscribe tu respuesta (o presiona Enter para ver el final): ")

# Mostrar el desenlace del chiste
print("\n" + "="*40)
print("RESPUESTA: " + remate)
print("="*40 + "\n")