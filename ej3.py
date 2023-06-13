from pila import Pila

pila = Pila()

# Agregar las misiones a la pila
pila.push({"planeta": "Marte", "capturado": "Jabba the Hutt", "recompensa": 500})
pila.push({"planeta": "Pluton", "capturado": "Lando Calrissian", "recompensa": 300})
pila.push({"planeta": "Saturno", "capturado": "No hubo capturas", "recompensa": 0})
pila.push({"planeta": "Jupiter", "capturado": "Han Solo", "recompensa": 3000})
pila.push({"planeta": "Venus", "capturado": "Yoda", "recompensa": 100})
pila.push({"planeta": "Urano", "capturado": "Luke Skywalker", "recompensa": 1000})
pila.push({"planeta": "Neptuno", "capturado": "Mace Windu", "recompensa": 400})
pila.push({"planeta": "Mercurio", "capturado": "No hubo capturas", "recompensa": 0})

# a. Mostrar los planetas visitados en el orden de las misiones
print("A. Planetas visitados:")
pila_temp = Pila()
while pila.size() > 0:
    mision = pila.pop()
    print(mision["planeta"])
    pila_temp.push(mision)
pila = pila_temp

# b. Determinar cuántos créditos galácticos recaudó en total
total_creditos = 0
pila_temp = Pila()
while pila.size() > 0:
    mision = pila.pop()
    total_creditos += mision["recompensa"]
    pila_temp.push(mision)
pila = pila_temp
print("B. Total de créditos galácticos recaudados:", total_creditos)

# c. Determinar el número de la misión en la que capturó a Han Solo y en qué planeta fue
numero_mision = None
planeta_captura = None
pila_temp = Pila()
while pila.size() > 0:
    mision = pila.pop()
    if mision["capturado"] == "Han Solo":
        numero_mision = pila_temp.size() + 1
        planeta_captura = mision["planeta"]
    pila_temp.push(mision)
pila = pila_temp

if numero_mision is not None:
    print("C. Han Solo fue capturado en la misión número", numero_mision)
    print("Planeta de la captura:", planeta_captura)
else:
    print("C. No se encontró la misión en la que capturó a Han Solo.")
