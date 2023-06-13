from cola import Cola
from lista import Lista

class Superheroe:
    def __init__(self, nombre_superheroe, nombre_personaje, grupo, anio_aparicion):
        self.nombre_superheroe = nombre_superheroe
        self.nombre_personaje = nombre_personaje
        self.grupo = grupo
        self.anio_aparicion = anio_aparicion

lista_superheroes = Lista()

lista_superheroes.insert(Superheroe('Mole Man', 'Ben Grimm', 'Los cuatro fantásticos', 1961))
lista_superheroes.insert(Superheroe('Mujer invisible', 'Susan Storm', 'Los cuatro fantásticos', 1961))
lista_superheroes.insert(Superheroe('Sr Fantastico', 'Reed Richards', 'Los cuatro fantásticos', 1961))
lista_superheroes.insert(Superheroe('Antorcha Humana', 'Johnny Storm', 'Los cuatro fantásticos', 1961))
lista_superheroes.insert(Superheroe('Capitana Marvel', 'Carol Danvers', 'Vengadores', 1968))
lista_superheroes.insert(Superheroe('Star-Lord', 'Peter Jason Quill', 'Guardianes de la galaxia', 1976))
lista_superheroes.insert(Superheroe('Groot', 'Groot', 'Guardianes de la galaxia', 1969))
lista_superheroes.insert(Superheroe('Drax', 'Arthur Douglas', 'Guardianes de la galaxia', 1973))
lista_superheroes.insert(Superheroe('Vlanck Widow', 'Natalia Alianovna', 'Los vengadores', 2010))


# a. Determinar si "Capitana Marvel" está en la lista y mostrar su nombre de personaje
capitana_marvel_found = False
nombre_personaje = None

for i in range(lista_superheroes.size()):
    heroe = lista_superheroes.get_element_by_index(i)
    if heroe.nombre_superheroe == 'Capitana Marvel':
        capitana_marvel_found = True
        nombre_personaje = heroe.nombre_personaje
        break

if capitana_marvel_found:
    print(f"A. Capitana Marvel está en la lista. Su nombre de personaje es: {nombre_personaje}")
else:
    print("A. Capitana Marvel no está en la lista.")

# b. Almacenar los superhéroes que pertenezcan al grupo "Guardianes de la galaxia" en una cola e indicar cuántos son
cola_guardianes = Cola()
for indice in range(lista_superheroes.size()):
    heroe = lista_superheroes.get_element_by_index(indice)
    if heroe.grupo == 'Guardianes de la galaxia':
        cola_guardianes.arrive(heroe.nombre_superheroe)

cantidad_guardianes = cola_guardianes.size()
print(f"B. Hay {cantidad_guardianes} superhéroes en el grupo 'Guardianes de la galaxia'.")

# c. Mostrar de manera descendente los superhéroes que pertenecen al grupo "Los cuatro fantásticos" y "Guardianes de la galaxia"
grupos = ['Los cuatro fantásticos', 'Guardianes de la galaxia']
for grupo in grupos:
    print(f"C. Superhéroes del grupo '{grupo}':")
    lista_superheroes.order_by(criterio='nombre_superheroe', reverse=True)
    for indice in range(lista_superheroes.size()):
        heroe = lista_superheroes.get_element_by_index(indice)
        if heroe.grupo == grupo:
            print(heroe.nombre_superheroe)

# d. Listar los superhéroes que tengan nombre de personajes cuyo año de aparición sea posterior a 1960
print("D. Superhéroes con nombres de personajes que aparecieron después de 1960:")
lista_superheroes.order_by(criterio='anio_aparicion')
for indice in range(lista_superheroes.size()):
    heroe = lista_superheroes.get_element_by_index(indice)
    if heroe.nombre_personaje != '' and heroe.anio_aparicion > 1960:
        print(heroe.nombre_superheroe)

# e. Corregir el nombre del superhéroe "Vlanck Widow" a "Black Widow"
posicion_vlanck = lista_superheroes.search('Vlanck Widow', criterio='nombre_superheroe')
if posicion_vlanck is not None:
    lista_superheroes.get_element_by_index(posicion_vlanck).nombre_superheroe = 'Black Widow'

# f. Agregar los personajes de la lista auxiliar a la lista principal si no están cargados
lista_auxiliar = [
    ('Black cat', 'Felicia Sara Hardy', 'Vengadores', 1979),
    ('Hulk', 'Bruce Banner', 'Vengadores', 1962),
    ('Loki', 'Loki Laufeyson', 'Gigantes de Hielo', 1949),
    ('Rocket Raccoon', 'Rocket Raccoon', 'Guardianes de la galaxia', 1979)
]
for personaje in lista_auxiliar:
    nombre_superheroe = personaje[0]
    if lista_superheroes.search(nombre_superheroe, criterio='nombre_superheroe') is None:
        lista_superheroes.insert(Superheroe(*personaje))

# g. Mostrar todos los personajes que comienzan con C, P o S
print("G. Personajes que comienzan con C, P o S:")
lista_superheroes.order_by(criterio='nombre_personaje')
for indice in range(lista_superheroes.size()):
    heroe = lista_superheroes.get_element_by_index(indice)
    nombre_personaje = heroe.nombre_personaje
    if nombre_personaje != '' and nombre_personaje[0] in ['C', 'P', 'S']:
        print(nombre_personaje)

# h. Cargar al menos 20 superhéroes a la lista
lista_superheroes.insert(Superheroe('Chamber', 'Vincent Fabron', 'Centinelas', 2021))
lista_superheroes.insert(Superheroe('Viper', 'Sabine Callas', 'Controladores', 2022))
lista_superheroes.insert(Superheroe('Omen', 'Wraith', 'Controladores', 2021))
lista_superheroes.insert(Superheroe('Raze', 'Tayane Alves', 'Duelistas', 2022))
lista_superheroes.insert(Superheroe('Gekko', 'Mateo Armendáriz De la Fuente', 'Iniciadores', 2023))
lista_superheroes.insert(Superheroe('Yoru', 'Ryo Kiritani', 'Duelistas', 2022))
lista_superheroes.insert(Superheroe('Skye', 'Kirra Foster', 'Iniciadores', 2021))
lista_superheroes.insert(Superheroe('Sage', 'Lingying Wei ', 'Centinelas', 2022))
lista_superheroes.insert(Superheroe('Brimstone', 'Liam Byrne', 'Controladores', 2021))
lista_superheroes.insert(Superheroe('Breach', 'Erik Torsten', 'Iniciadores', 2022))
lista_superheroes.insert(Superheroe('Phoenix', 'Jamie Adeyemi', 'Duelistas', 2021))
lista_superheroes.insert(Superheroe('Reyna', 'Zyanya Mandrogón', 'Duelistas', 2022))
lista_superheroes.insert(Superheroe('Killjoy', 'Klara Böhringer', 'Centinelas', 2021))
lista_superheroes.insert(Superheroe('Sova', 'Sasha Novikov ', 'Iniciadores', 2022))
lista_superheroes.insert(Superheroe('Jett', 'Sunwoo Han', 'Duelistas', 2021))
lista_superheroes.insert(Superheroe('Neon', 'Tala Nicole Dimaapi Valdez', 'Duelistas', 2022))
lista_superheroes.insert(Superheroe('Astra', 'Efia Danso', 'Controladores', 2021))
lista_superheroes.insert(Superheroe('Harbour', 'Varun Batra', 'Controladores', 2022))
lista_superheroes.insert(Superheroe('Cypher', 'Amir El Amari ', 'Centinelas', 2021))
lista_superheroes.insert(Superheroe('Kay-O', '', 'Iniciadores', 2022))

print(f"H. La lista contiene {lista_superheroes.size()} Superheroes.")
