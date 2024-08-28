from myfunctions import operAritmetic
from myfunctions import calcIva

print("Hola Mundo desde Python")
'''
Este es un comentario de varias lineas
'''
# Este es un comentario de una línea
# Definición de variables
firstName = "Pedro"
lastName = "Gomez"
print(type(firstName)) 
salaryEmployee = 5000000
gender = False
# lista
numbers = [1, 2, 3, 4, 5, 6, 7]
# tupla
todd = (1,3,5,7,9)
# set
tpair = {10, 20, 30,40}
# diccionario
person = {"cc":"1214","name":"John Doe","phone":"3105632147","gender":False,"salary":3200000}
# arreglo de objetos
persons = [
    {"id":3,"firstName":"Jane Doe","address":"Calle 8 # 8-8"},
    {"id":4,"firstName":"Peter Parker","address":"Kra 8 # 8-8"},
    {"id":6,"firstName":"Simone Biles","address":"Trans 8 # 8-8"},
]
# Condicional
'''
if not gender:
    print("El empleado es hombre")
else:
    print("El empleado es Mujer")
'''
# Operador ternario u operador condicional
print("Es Hombre" if not gender else "Es Mujer")
comission = salaryEmployee * 10/100 if gender and salaryEmployee > 4000000 else salaryEmployee * 2/100
print(f"Comision: {comission}")
print("Comision otra vez: ",comission)
category = "B"
valuePay = 0
if category == "A":
    valuePay = 5000
elif category == "B":
    valuePay = 10000
elif category == "C":
    valuePay = 20000
elif category == "D":
    valuePay = 30000
else:
    valuePay = 1000

print(f"Valor a pagar: {valuePay}")
# Ciclo para (for)
initial = 1
limit = 6

for i in range(initial,limit):
    '''
    if i < limit - 1:
        print(i,end=",")
    else:
        print(i)
    '''
    print(i, end=", " if i < limit - 1 else "")
# ciclos para recorrer objetos iterables
print("Iteración en listas, tuplas, diccionario, etc")
for nro in numbers:
    print(nro)
print("______________")
for i in range(0,len(numbers)):
    print(numbers[i])
# Cantidad de numeros pares e impares

countEven = 0
countOdd = 0
for num in numbers:
    if num % 2 == 0:
        countEven += 1
    else:
        countOdd += 1
print(f"Cantidad de numeros pares: {countEven} e impares: {countOdd}")
print("Recorrer una tupla")
for n in todd:
    print(n)
print("Recorrer un set")
for num in tpair:
    print(num)

# Ciclo para recorrer un diccionario person
print("Mostrar datos del diccionario person")
for key, value in person.items():
    print(f"{key}: {value}")
print("Mostrar datos del diccionario person de otra forma")
for item in person:
    print(f"{item}: {person[item]}")
print(person["cc"])
print("Mostrando los datos de la lista de diccionarios")
for person in persons:
    print(f"ID: {person['id']}, Nombre: {person['firstName']}, Dirección: {person['address']}")
print("Buscando el id del diccionario la lista persons")
idSearch = int(input("Ingrese el id de la persona: "))
found = False
for per in persons:
    if per['id'] == idSearch:
        #print(f"ID: {per['id']}, Nombre: {per['firstName']}, Dirección: {per['address']}")
        personFind = per
        found = True
        break
if found:
    print(personFind["firstName"])
else:
    print("No se encuentra el id de la persona")
    
# Funciones
def sum(a,b):
    return a + b

def message(text):
    print(text)
    
# Llamando a las funciones
message("Hola Mundo desde Python con métodos")
message("Bienvenido al sistema")
a = "Buenos días"
message(a)
print(sum(5,9))
num1 = int(input("Ingrese valor 1: "))
num2 = int(input("Ingrese valor 2: "))
resultado = sum(num1,num2)
if sum(num1,num2) > 20:
    message("El resultado es mayor a 20")

print(operAritmetic(34,0,"/"))
valIva = calcIva(100000)
print(f"El valor del iva de 100000 es {valIva}")
    




