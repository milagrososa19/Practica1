#Ejercicio 1
nombre = input ("Ingresa tu nombre")
edad = int (input("Ingresa tu edad"))
materia = input ("Ingresa tu materia favorita")

print("Hola", nombre, "tenes", edad,"y tu materia favorita es", materia)

#Ejercicio 2
if edad > 16:
   print("Podes votar")
else:
   print("Todavia no puede votar")
   
#Ejercicio 3
# Una variable de programacion es el espacio donde se guarda un dato, este tiene un nombre y un tipo.
# El input sirve para ingresar un texto.
# La funcion que cumple el print es imprimir por pantalla.
# Una  condicion if es una estructura condicional que evalua una accion, si es verdadero realiza una accion y si es falsa realiza otra accion.

#Ejercicio 4
alumnos = [
{
"nombre": "Juan",
"materia": "Programacion",
"edad": 16
},
{
"nombre": "Maria",
"materia": "Matematica",
"edad": 17
},
{
"nombre": "Mili",
"materia": "Literatura",
"edad": 19
},
{
"nombre": "Mauro",
"materia": "Geografia",
"edad": 18
},
{
"nombre": "Franco",
"materia": "Biologia",
"edad": 20
}
]

#Ejercicio 6
for alumno in alumnos:
    print(alumno["nombre"])
    
#Ejercicio 7
nombre = input("Ingresa el nombre del alumno: ")
for alumno in alumnos:
    if alumno["nombre"] == nombre:
        print(alumno)
        encontrado = True
if encontrado == False: 
    print("Alumno no encontrado")

#Ejercicio 8
print("Cantidad total de alumnos:", (alumnos))
mayores = 0
for alumno in alumnos:
    if alumno["edad"] > 16:
        mayores = mayores + 1
print("Cantidad de alumnos mayores de 16 años:", mayores)

#Ejercicio 9
def buscar_alumno():
    alumno_buscado = input("Ingresar nombre a buscar")
    for alumno in alumnos: 
        if alumno ["nombre"] == alumno_buscado:
            print(alumno[nombre])

#Ejercicio 10
# Una lista de Python guarda varios datos dentro de una misma variable. Los datos se escriben entre corchetes [].
# Un diccionario permite guardar datos en forma de clave y valor. Se escribe entre llaves {}.
# La diferencia es que los datos de la lista se identifican por su posicion y los datos del diccionario se identifican mediante una clave.
# El for sirve para repetir una accion y recorrer elementos.
# JSON significa JavaScript Object Notation. Es un formato utilizado para guardar y enviar información de una manera organizada. Se usa mucho para intercambiar datos entre aplicaciones, páginas web y servidores.
