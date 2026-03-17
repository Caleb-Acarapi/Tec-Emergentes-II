# ==========================================
# 1. ELEMENTALES Y CONFIGURACIÓN
# ==========================================
# Python es un intérprete.
print("Hola mundo") # Imprimir en consola

# Comentarios
# Una sola línea
"""
Comentario de 
varias líneas
"""

# Declaración de variables y Tipos
name = "Pepe"      # String (Referenciado en Heap)
number = 1234     # Entero
flotante = 3.14   # Flotante
booleano = True   # Booleano
complejo = 3 + 1j # Complejo
CONSTANTE = 3.14  # Constantes en mayúsculas

# Identificar tipo de dato
print(type(name)) # Retorna <class 'str'>

# ==========================================
# 2. OPERADORES
# ==========================================
# Aritméticos
print(3 + 3)   # Suma (6)
print(3 - 3)   # Resta (0)
print(3 * 2)   # Multiplicacion(6)
print(5 / 2)   # Division (2.5)
print(10 // 3) # División entera (3)
print(3 ** 2)  # Potencia (9)
print(10 % 3)  # Módulo/Resto (1)

#Asignacion
# variable = valor
# numero += 2
# numero *= 2
# Precendencia
x = 10 + (3 * 2)
print(x)

# Relacionales >,<,<=,>=,==,!=
print(3 > 4)   # False
print(3 <= 4)  # True
print(3 == 3)  # Igualdad
print(3 != 4)  # Distinto

# Lógicos and or not
print(3 < 4 and "Hola" < "Python") # True AND True
print(5 > 3 or True) #Or
print(not(True)) # False not

# ==========================================
# 3. STRINGS (CADENAS)
# ==========================================
cadena = "Hola Python" # Inmutables

# Concatenación y caracteres especiales
print("Hola" + " ", cadena) # Unión
print("Salto: \n Tab: \t")   # Especiales
print("Repetir " * 2)        # Multiplicar
#Buscar
print(cadena.find("Hola"))
#Reemplazar
print(cadena.replace("Python", "JavaScript"))
#Ver si se encuentra
print("Hola" in cadena)
# Formateo (3 formas)
print("Nombre: {} Edad: {}".format(name, number)) # .format
print("Nombre: %s Edad: %d" % (name, number))     # %
print(f"Nombre: {name} Edad: {number}")           # f-string

# Devanado (Slicing): [inicio:fin:avance]
print(cadena[0:4:1]) # "Hola"
print(cadena[::-1])  # Invertir cadena

# Métodos de Cadenas
print(cadena.upper())      # MAYÚSCULAS
print(cadena.capitalize()) # Primera letra
print(cadena.strip())      # Quitar espacios blanco
print(cadena.split(" "))   # Separar por espacio

# Desempaquetado
languaje = "Python"
a,b,c,d,e,f = languaje # Asigna cada letra

# ==========================================
# 4. INPUT Y CONVERSIÓN
# ==========================================
# Entrada siempre retorna string
nombre_in = input("Ingrese nombre: ") 
edad_in = int(input("Ingrese edad: ")) # Conversión a int

# ==========================================
# 5. CONDICIONALES
# ==========================================
#if simple
if True:
    print("verdad")
else:
    print("Falso")

if edad_in >= 18:
    print("Mayor de edad")
elif edad_in < 0:
    print("Error")
else:
    print("Menor de edad")

# Match (Menú de elección)
opcion = '1'
match opcion:
    case '1': print('Es uno')
    case _: print('Desconocido')

# ==========================================
# 6. CICLOS (BUCLES)
# ==========================================
# While: mientras se cumpla la condición
i = 0
while i < 3:
    print(i)
    i += 1
else: print("Bucle terminado")

i = 1
while i <= 10:
    print(i * "*")
    i += 1

# For: número conocido de iteraciones
for x in range(5): # De 0 a 4
    if x == 2: continue # Salta iteración
    if x == 4: break    # Rompe ciclo
    print(x)

# ==========================================
# 7. ESTRUCTURAS DE DATOS
# ==========================================

# LISTAS: Mutables y ordenadas
mi_lista = [4, 3, "Hola"]
print(mi_lista[2]) #Acceder a elementos
print(mi_lista[-1]) #Acceder a elementos
print(mi_lista[1:]) #Acceder a elementos

mi_lista.append("Python") # Agrega al final
mi_lista.insert(2, "Django") # Agrega en posición
mi_lista[0] = 0 # Modificar
mi_lista.pop() # Elimina último
mi_lista.remove(3) # Elimina valor
del mi_lista[0] # Elimina posición
print(4 in mi_lista) # Verificar existencia
print(len(mi_lista)) #Tamanio de la lista
mi_lista.clear() #Vaciar la lista

#Range se comporta como una lista pero no lo es
for item in range(5, 10):
    print(item)
for item in range(10, 20, 2):
    print(item)

#Iterar elementos
mi_lista = range(1, 11)
for item in mi_lista:
    print(item)
# TUPLAS: Inmutables
mi_tupla = (3, 2.10, "Python")
print(mi_tupla)
print(mi_tupla[2]) # Acceder a elementos
print(mi_tupla.count(3)) # Contar
# mi_tupla[0] = 0 no se permite la asigancion
print(mi_tupla.index(2.10)) # Buscar posición

# CONJUNTOS (SETS): Sin repetidos, desordenado
mi_conjunto = {1, 2, 3, 3} # Queda {1, 2, 3}
otro_conjunto = {3, 4, 5}
print(mi_conjunto, otro_conjunto)
mi_conjunto.add(6) # Agregar
# Operaciones
print(mi_conjunto | otro_conjunto) # Unión
print(mi_conjunto & otro_conjunto) # Intersección
print(mi_conjunto - otro_conjunto) # Diferencia

# DICCIONARIOS: Clave-Valor
persona = {"nombre": "Kali", "edad": 20}
print(persona["nombre"]) # Acceder a un valor
persona["ciudad"] = "La Paz" # Agregar/Actualizar
print(persona.keys())   # Solo claves
print(persona.values()) # Solo valores
print(persona.items())  # Clave y valor

#Verificar existencia
if "ciudad" in persona:
    print("Clave Encontrada")
#recorrido de un diccionario
for clave, valor in persona.items():
    print(f"Clave: {clave} Valor: {valor}")
# ==========================================
# 8. FUNCIONES Y MÓDULOS
# ==========================================
#funcion sin parametros
def funcion_simple():
    print("Estos es una funcion simple")
#Llamada
funcion_simple()

#funcion con parametros y valores por defecto
def saludo(nombre, hoby="Nada"):
    print(f"Hola {nombre}, tu hoby es {hoby}")
#Llamada
saludo("Caleb")
saludo("Kali", "Programacion")

#funcon con retorno de valores
def suma(a, b):
    return a + b
#llamada
print(suma(7, 10))

# *args variables (Tupla) y **kwargs definidos (Diccionario)
def superheroe(nombre, *args, **kwargs):
    print(f"Heroe: {nombre}")
    for poder in args: print(f"Poder: {poder}")
    print(f"Datos extra: {kwargs}")

superheroe("Spiderman", "Telaraña", "Instinto", "Fuerza", edad=25)

# Recursividad (Llamarse a sí misma hasta caso base)
def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

print(factorial(5))

# Módulos
import math # Importar todo
from math import pi # Importar específico
