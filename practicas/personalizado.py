# EJERCICIO 1

nombre = input('Ingrese su nombre')
edad = int(input("Dame tu edad"))
print(f"Hola {nombre}, tu edad es de {edad}")


# EJERCICIO 2

# Leer tres notas de un estudiante y mostrar su promedio.
# Modifícalo para que muestre «Aprueba» si el promedio es ≥ 7
# y «Reprueba» si no. (Necesitas el if del módulo 3).

n = 0
suma = 0

while n < 3:

    nota = float(input(f"Dame la nota {n + 1}: "))

    suma = suma + nota

    n = n + 1

promedio = suma / 3

if promedio >= 7:

    estado = "Aprueba"

else:

    estado = "Reprueba"

print(f"El promedio es: {promedio:.2f}, {estado}")


# EJERCICIO 3

# Leer la base y la altura de un rectángulo y mostrar
# su área y su perímetro. Recuerda: área = base × altura, perímetro = 2 × (base + altura).
# Ampliar para leer el radio de un círculo y mostrar área (π·r²) y perímetro (2·π·r). Usa import math y math.pi.

import math

base = float(input("Dame la base del rectángulo: "))

altura = float(input("Dame la altura del rectángulo: "))

area = base * altura

perimetro = 2 * (base + altura)

print(f"Área del rectángulo: {area:.2f}")

print(f"Perímetro del rectángulo: {perimetro:.2f}")

radio = float(input("Dame el radio del círculo: "))

area_circulo = math.pi * radio ** 2

perimetro_circulo = 2 * math.pi * radio

print(f"Área del círculo: {area_circulo:.2f}")

print(f"Perímetro del círculo: {perimetro_circulo:.2f}")


# EJERCICIO 4

# Leer el precio de un producto sin IVA y mostrar el IVA y el precio final. El IVA en Ecuador es 15%.
# Añadir un descuento del 10% que se aplique antes del IVA. Muestra los tres valores: descuento, IVA, total.

iva = 0.15

descuento = 0.10

producto = float(input("Dame el precio del producto: "))

valor_descuento = producto * descuento

precio_con_descuento = producto - valor_descuento

valor_iva = precio_con_descuento * iva

total = precio_con_descuento + valor_iva

print(f"Descuento: ${valor_descuento:.2f}")

print(f"IVA: ${valor_iva:.2f}")

print(f"Total: ${total:.2f}")


# EJERCICIO 5

# Leer un número entero y determinar si es par o impar.
# Modifícalo para que además diga si es múltiplo de 3, de 5, o de ambos.

n = int(input("Dame un número"))

print("Es par") if n % 2 == 0 else print("Es impar")

if n % 3 == 0 and n % 5 == 0:
    print("Es múltiplo de 3 y de 5")
elif n % 3 == 0:
    print("Es múltiplo de 3")
elif n % 5 == 0:
    print("Es múltiplo de 5")
else:
    print("No es múltiplo de 3 ni de 5")


# EJERCICIO 6

# Leer una cantidad total de segundos y mostrarla como hh:mm:ss.
# Ejemplo: 3725 segundos → 01:02:05.


total = int(input("Dame total de segundos: "))

horas = total // 3600

resto = total % 3600

minutos = resto // 60

segundos = resto % 60

print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")
#  Al revés: leer hh:mm:ss y convertir a segundos totales.
# Tendrás que usar split(":")

tiempo = input("Dame el tiempo hh:mm:ss: ")

horas, minutos, segundos = tiempo.split(":")

horas = int(horas)

minutos = int(minutos)

segundos = int(segundos)

total_segundos = horas * 3600 + minutos * 60 + segundos

print(f"Total de segundos: {total_segundos}")


# EJERCICIO 7

# Un cajero solo tiene billetes de $20, $10, $5 y $1.
# Dado un monto, mostrar cuántos billetes de cada uno se necesitan (usando la mínima cantidad).
# Añadir billete de $50 al inicio. Después probar con monedas de $0.25, $0.10, $0.05 y $0.01
# (necesitas trabajar con centavos).

monto = int(input("Monto: $"))

resto = monto

b50 = resto // 50

resto = resto % 50

b20 = resto // 20

resto = resto % 20

b10 = resto // 10

resto = resto % 10

b5 = resto // 5

resto = resto % 5

b1 = resto // 1

resto = resto % 1

print(f"$50 × {b50}")

print(f"$20 × {b20}")

print(f"$10 × {b10}")

print(f"$5 × {b5}")

print(f"$1 × {b1}")


# Versión con monedas de $0.25, $0.10, $0.05 y $0.01.
# Trabajamos con centavos para evitar problemas con decimales.

monto = float(input("Monto con centavos: $"))

centavos = round(monto * 100)

resto = centavos

m25 = resto // 25

resto = resto % 25

m10 = resto // 10

resto = resto % 10

m5 = resto // 5

resto = resto % 5

m1 = resto // 1

resto = resto % 1

print(f"$0.25 × {m25}")

print(f"$0.10 × {m10}")

print(f"$0.05 × {m5}")

print(f"$0.01 × {m1}")


# EJERCICIO 8

# Leer un número N y mostrar los números del 1 al N.

n = int(input("N"))

for i in range(1, n + 1):

    print(i)



# Cámbialo para que muestre del N al 1 (hacia atrás). Pista: range(n, 0, -1).

b = int(input("N"))

for i in range(b, 0, -1):

    print(i)


# EJERCICIO 10

# Leer N y calcular la suma de 1 + 2 + 3 + ... + N.

sum = 0

n = int(input("N"))

for i in range(1, n + 1):

    sum = sum + i

print(f"Suma: {sum}")


# Adaptarlo para calcular la suma de los pares del 2 al 100. Pista: range(2, 101, 2).

sum = 0

for i in range(2, 101, 2):

    sum = sum + i

print(f"La suma de los números pares es: {sum}")


# Leer N y calcular el factorial (N! = 1 × 2 × 3 × ... × N).
# Ejemplo: 5! = 120.

n = int(input("N: "))

fact = 1

for i in range(1, n + 1):

    fact = fact * i

print(f"{n}! = {fact}")

# EJERCICIO 

# Leer las notas de N estudiantes (una por una) y contar cuántos aprobaron (nota ≥ 70).
# Añade un contador para reprobados y muestra el porcentaje de aprobación.

n = int(input("Cuántos estudiantes tienes: "))

aprobados = 0
reprobados = 0

for i in range(n):

    a = float(input(f"Dame la nota del estudiante {i + 1}: "))

    if a >= 70:

        aprobados += 1

    else:

        reprobados += 1

porcentaje = aprobados / n * 100

print(f"Cantidad de estudiantes aprobados: {aprobados}")
print(f"Cantidad de estudiantes reprobados: {reprobados}")
print(f"Porcentaje de aprobación: {porcentaje:.2f}%")

# EJERCICIO 

# Leer las notas de N estudiantes y mostrar la nota más alta.
# Adaptarlo para encontrar la menor nota. Cambio: float("inf") y if nota < minima:.

n = int(input("¿Cuántas notas? "))

minima = float("inf")

for i in range(n):

    nota = float(input(f"Nota {i + 1}: "))

    if nota < minima:

        minima = nota

print(f"Mínima: {minima}")

# Leer un número y determinar si es primo (solo divisible entre 1 y él mismo).
n = int(input("Número: "))
es_primo = True                     

if n < 2:
    es_primo = False                
else:
    # Probar divisores del 2 hasta √n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:             
            es_primo = False       
            break                 

if es_primo:
    print(f"{n} es primo")
else:
    print(f"{n} NO es primo")


# Genera una lista de todos los primos entre 2 y 100.

primos = []

for i in range(2, 101):

    es_primo = True

    for j in range(2, i):

        if i % j == 0:

            es_primo = False
            break

    if es_primo:

        primos.append(i)

print(primos)


#  Lee un número N y muestra su tabla de multiplicar (del 1 al 12).
n = int(input('N'))
for i in range (1,13):
    print(f"{n} × {i} = {n * i}")

    # Lee un número y cuenta cuántos dígitos tiene (sin convertir a string).
num = int(input("Número: "))
n = abs(num)               
digitos = 0

if n == 0:
    digitos = 1          
else:
    while n > 0:
        digitos += 1
        n = n // 10        

print(f"{digitos} dígitos")

# Lee N números y muestra la suma de los pares y la suma de los impares por separado.
n = int(input("¿Cuántos números? "))
suma_pares = 0
suma_impares = 0

for i in range(n):
    x = int(input(f"Número {i+1}: "))
    if x % 2 == 0:
        suma_pares += x
    else:
        suma_impares += x

print(f"Suma pares: {suma_pares}")
print(f"Suma impares: {suma_impares}")

# Pide una edad y valida que esté entre 0 y 120. Si el usuario ingresa algo inválido, vuelve a pedirla.
while True:
    edad = int(input("Edad (0-120): "))
    if 0 <= edad <= 120:
        break                     
    print("Inválida, intenta de nuevo")

print(f"Edad válida: {edad}")

# Genera un número secreto entre 1 y 100. El usuario intenta adivinar. 
# En cada intento le dices si es «mayor» o «menor». Cuenta cuántos intentos usó.

import random

secreto = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("Adivina (1-100): "))
    intentos += 1
    if intento == secreto:
        print(f"¡Correcto en {intentos} intentos!")
        break
    elif intento < secreto:
        print("Es mayor")
    else:
        print("Es menor")
        # Muestra los primeros N números de Fibonacci.
        #  La serie: 0, 1, 1, 2, 3, 5, 8, 13, 21... Cada número es la suma de los dos anteriores.
        n = int(input("Cuantos"))
        a , b = 0, 1
        for _ in range (n):
            print(a, end = "")
            a , b = b , a + b
            print()
# EJERCICIO 

# Escribir una función calcular_iva(precio) que reciba un precio y retorne el
# IVA (15%). Usarla desde el programa principal.
# Amplíala: define calcular_total(precio) que retorne precio + IVA usando la función anterior.

def calcular_iva(precio):

    return precio * 0.15


def calcular_total(precio):

    iva = calcular_iva(precio)

    return precio + iva


precio = float(input("Precio: $"))

iva = calcular_iva(precio)

total = calcular_total(precio)

print(f"IVA de ${precio}: ${iva:.2f}")

print(f"Total: ${total:.2f}")





# Escribir una función que reciba un número y retorne True si es primo, False si no.
# Escribe una función contar_primos(a, b) que cuente cuántos primos hay entre a y b.

def es_primo(n):

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:
            return False

    return True


def contar_primos(a, b):

    contador = 0

    for k in range(a, b + 1):

        if es_primo(k):
            contador += 1

    return contador


num = int(input("Número: "))

if es_primo(num):

    print(f"{num} es primo")

else:

    print(f"{num} no es primo")


print("Primos entre 2 y 30")

for k in range(2, 31):

    if es_primo(k):

        print(k, end=" ")


cantidad = contar_primos(2, 30)

print(f"\nCantidad de primos entre 2 y 30: {cantidad}")


# Escribir una función suma_digitos(n) que retorne la suma de los dígitos de un número.
# Escribe es_narcisista(n): retorna True si el número es igual a la suma de sus dígitos
# elevados al número de dígitos. Ej.: 153 = 1³+5³+3³.

def suma_digitos(n):

    n = abs(n)

    suma = 0

    while n > 0:

        suma += n % 10

        n = n // 10

    return suma


def es_narcisista(n):

    numero = abs(n)

    digitos = len(str(numero))

    suma = 0

    while numero > 0:

        digito = numero % 10

        suma += digito ** digitos

        numero = numero // 10

    return suma == abs(n)



num = int(input("Número: "))

print(f"Suma: {suma_digitos(num)}")

if es_narcisista(num):

    print(f"{num} es narcisista")

else:

    print(f"{num} no es narcisista")



for x in [123, 4783, 999]:

    print(f"{x} → {suma_digitos(x)}")


# Rediseñar el menú de saludar/despedir del módulo 3,
# pero esta vez con cada opción como función separada.
# Añade una función calcular() que pida dos números
# y muestre suma, resta, multiplicación y división. Nueva opción del menú.

def saludar():

    nombre = input("Nombre: ")

    print(f"¡Hola, {nombre}!")


def despedir():

    nombre = input("Nombre: ")

    print(f"¡Adiós, {nombre}!")


def calcular():

    num1 = float(input("Primer número: "))

    num2 = float(input("Segundo número: "))

    print(f"Suma: {num1 + num2}")
    print(f"Resta: {num1 - num2}")
    print(f"Multiplicación: {num1 * num2}")

    if num2 != 0:
        print(f"División: {num1 / num2}")
    else:
        print("No se puede dividir para cero")


def mostrar_menu():

    print("\n--- MENÚ ---")

    print("1. Saludar")

    print("2. Despedir")

    print("3. Calcular")

    print("4. Salir")


while True:

    mostrar_menu()

    opcion = input("Opción: ")

    if opcion == "1":

        saludar()

    elif opcion == "2":

        despedir()

    elif opcion == "3":

        calcular()

    elif opcion == "4":

        print("Adiós")

        break

    else:

        print("Opción inválida")

        # Función area_rectangulo(base, altura) que retorne el área.
def area_rectangulo(base, altura):
    return base * altura

print(area_rectangulo(5.7, 2))    
print(area_rectangulo(4, 1))  

# Función maximo(a, b, c) que retorne el mayor de tres números.
def maximo(a, b, c):
    return max(a, b, c)         

def maximo_manual(a, b, c):
    mayor = a
    if b > mayor: mayor = b
    if c > mayor: mayor = c
    return mayor

print(maximo(5, 9, 3))           
print(maximo_manual(5, 9, 3))   

# Un año es bisiesto si es divisible entre 4 y no entre 100, O si es divisible entre 400.
def es_bisiesto(anio):
    if anio % 400 == 0:
        return True
    if anio % 100 == 0:
        return False
    if anio % 4 == 0:
        return True
    return False

def es_bisiesto_corta(anio):
    return anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0)

for y in [2004, 2033, 1887, 1900]:
    print(f"{y}: {es_bisiesto(y)}")

    # Función factorial(n) y luego combinatoria(n, k) = n! / (k! · (n-k)!).
def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

def combinatoria(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

print(factorial(5))           
print(combinatoria(5, 2))      

# Programa que use funciones separadas para cada operación 
# (sumar, restar, multiplicar, dividir) y un menú que llame a la correcta
def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b):
    if b == 0:
        return None            
    return a / b

while True:
    print("\n1.Sumar 2.Restar 3.Multiplicar 4.Dividir 5.Salir")
    op = input("Opción: ")
    if op == "5":
        break
    a = float(input("a: "))
    b = float(input("b: "))
    if op == "1": r = sumar(a, b)
    elif op == "2": r = restar(a, b)
    elif op == "3": r = multiplicar(a, b)
    elif op == "4":
        r = dividir(a, b)
        if r is None:
            print("No se puede dividir entre 0")
            continue
    else:
        print("Opción inválida"); continue
    print(f"Resultado: {r}")

# Pide una frase al usuario y cuenta cuántas vocales (a, e, i, o, u) tiene. Ignora mayúsculas/minúsculas.
frase = input("Frase: ").lower()
vocales = {"a", "e", "i", "o", "u"}
total = 0
for ch in frase:
    if ch in vocales:
        total += 1
print(f"{total} vocales")

# Dada una lista fija de notas [7, 8.5, 6, 9, 10, 5.5],
#  calcula el promedio, la nota máxima y la mínima. Imprime los tres valores con 2 decimales.

notas = [7, 8.5, 6, 9, 10, 5.5]
promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio:.2f}")
print(f"Máximo:   {max(notas):.2f}")
print(f"Mínimo:   {min(notas):.2f}")

# Dada la lista ["a", "b", "a", "c", "b", "d"], retorna una nueva lista sin duplicados 
# respetando el orden de la primera aparición. (Con set se pierde el orden — hay que combinar set + list.

datos = ["a", "b", "a", "c", "b", "d"]
vistos = set()
resultado = []
for x in datos:
    if x not in vistos:
        vistos.add(x)
        resultado.append(x)
print(resultado)  

# Dado un texto, retorna un diccionario con la
#  frecuencia de cada palabra (ignora mayúsculas). Al final, imprime la palabra que más se repite.


texto = "te amo emanuella te amo mucho"
conteo = {}
for palabra in texto.lower().split():
    conteo[palabra] = conteo.get(palabra, 0) + 1

print(conteo)

mas = max(conteo, key=conteo.get)
print(f"Más repetida: '{mas}' ({conteo[mas]} veces)")

# Añade un método cumplir_anios() que sume 1 a la edad.

class Pasajero:

    def __init__(self, nombre, cedula, edad):

        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad

    def __str__(self):

        return f"{self.nombre} ({self.cedula}) - {self.edad} años"

    def cumplir_anios(self):

        self.edad += 1



p1 = Pasajero("emanuella", "0941325635", 18)

p2 = Pasajero("puala", "0987634522", 19)

p3 = Pasajero("roosevelt", "0923456789", 21)

print(p1)

print(p2)

print(p3)

p1.cumplir_anios()

print(p1)
# Crear CuentaBancaria con métodos depositar,
# retirar, saldo y __str__. El saldo empieza en 0.
# No se puede retirar más de lo que hay.
#
# Añade historial: una lista donde cada operación
# añade un string tipo '+100', '-30'.
# Método ver_historial()

class CuentaBancaria:

    def __init__(self, numero):

        self.numero = numero
        self._saldo = 0
        self.historial = []

    def depositar(self, monto):

        if monto <= 0:
            print("Monto inválido")
            return

        self._saldo += monto
        self.historial.append(f"+{monto}")

        print(f"Depósito de ${monto}. Saldo: ${self._saldo}")

    def retirar(self, monto):

        if monto <= 0:
            print("Monto inválido")
            return

        if monto > self._saldo:
            print(f"Saldo insuficiente (tiene ${self._saldo})")
            return

        self._saldo -= monto
        self.historial.append(f"-{monto}")

        print(f"Retiro de ${monto}. Saldo: ${self._saldo}")

    def saldo(self):

        return self._saldo

    def ver_historial(self):

        return self.historial

    def __str__(self):

        return f"Cuenta {self.numero}: ${self._saldo}"



c = CuentaBancaria("025")

c.depositar(250)

c.retirar(80)

c.depositar(120)

c.retirar(50)

c.retirar(500)

print(c)

print(c.saldo())

print(c.ver_historial())

# Clase Producto con nombre, precio y stock. Métodos:
# vender(cantidad) (reduce stock si hay), reabastecer(cantidad),
# valor_inventario() (precio × stock)
#
# Amplíalo con un método de clase total_inventario(productos)
# que sume los valores de una lista de productos

class Producto:

    def __init__(self, nombre, precio, stock):

        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):

        if cantidad > self.stock:
            print(f"Sin stock suficiente ({self.stock} disponibles)")
            return False

        self.stock -= cantidad

        print(f"Vendidas {cantidad} de {self.nombre}. Stock: {self.stock}")

        return True

    def reabastecer(self, cantidad):

        self.stock += cantidad

        print(f"Nuevo stock de {self.nombre}: {self.stock}")

    def valor_inventario(self):

        return self.precio * self.stock

    @classmethod
    def total_inventario(cls, productos):

        total = 0

        for producto in productos:

            total += producto.valor_inventario()

        return total

    def __str__(self):

        return f"{self.nombre} - ${self.precio:.2f} - stock: {self.stock}"



leche = Producto("Leche", 1.20, 10)

pan = Producto("Pan", 0.50, 30)

arroz = Producto("Arroz", 2.00, 15)

print(leche)

leche.vender(3)

print(f"Valor: ${leche.valor_inventario():.2f}")

leche.vender(20)

leche.reabastecer(5)

productos = [leche, pan, arroz]

total = Producto.total_inventario(productos)

print(f"Valor total del inventario: ${total:.2f}")
# Clase Rectangulo con base y altura. Métodos area(), perimetro() y __str__.
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def __str__(self):
        return f"Rectángulo {self.base}×{self.altura}, área={self.area()}, perímetro={self.perimetro()}"

r = Rectangulo(8, 2)
print(r)
print(r.area())

# Clase con radio y métodos area() (π·r²) y circunferencia() (2·π·r). Usa math.pi.
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def circunferencia(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return f"Círculo r={self.radio}, área={self.area():.2f}"

c = Circulo(5)
print(c)                         

# Clase Estudiante con nombre y 
# una lista de notas. Métodos: agregar_nota(n), promedio(), aprobado() (True si promedio ≥ 7).
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []          # lista vacía inicial

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def aprobado(self):
        return self.promedio() >= 7

    def __str__(self):
        return f"{self.nombre}: {self.notas} → prom={self.promedio():.2f}"

emanuella = Estudiante("Emanuella")
for n in [8, 6, 9]:
    emanuella.agregar_nota(n)
print(emanuella)
print(f"Aprobado: {emanuella.aprobado()}")
# Clase Vehiculo con marca, modelo y km recorridos (inicialmente 0). 
# Método recorrer(km) que suma al odómetro. Método necesita_mantenimiento() que retorna True cada 10 000 km.
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.km = 0
        self._ultimo_mantenimiento = 0

    def recorrer(self, distancia):
        self.km += distancia

    def necesita_mantenimiento(self):
        return (self.km - self._ultimo_mantenimiento) >= 10000

    def hacer_mantenimiento(self):
        self._ultimo_mantenimiento = self.km
        print(f"Mantenimiento hecho a los {self.km} km")

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.km} km"

auto = Vehiculo("Toyota", "Corolla")
auto.recorrer(15000)
print(auto)                                     
print(f"Necesita mantenimiento: {auto.necesita_mantenimiento()}")
auto.hacer_mantenimiento()                        
print(f"Necesita mantenimiento: {auto.necesita_mantenimiento()}")












# Modela una empresa aérea con Persona
#  como clase base y Pasajero y Empleado como hijas. Cada hija añade su propio atributo y método.
class Persona:

    def __init__(self, nombre, cedula):

        self.nombre = nombre
        self.cedula = cedula

    def presentarse(self):

        print(f"Soy {self.nombre}, cédula {self.cedula}")

    def __str__(self):

        return f"{self.nombre} ({self.cedula})"


class Pasajero(Persona):

    def __init__(self, nombre, cedula, codigo_reserva):

        super().__init__(nombre, cedula)
        self.codigo_reserva = codigo_reserva
        self.millas = 0

    def sumar_millas(self, m):

        self.millas += m

    def __str__(self):

        return f"Pasajero {self.nombre} [reserva: {self.codigo_reserva}] · {self.millas} millas"


class Empleado(Persona):

    def __init__(self, nombre, cedula, codigo_emp, salario):

        super().__init__(nombre, cedula)
        self.codigo_emp = codigo_emp
        self.salario = salario

    def aumentar_salario(self, porcentaje):

        self.salario *= (1 + porcentaje / 100)

    def __str__(self):

        return f"Empleado {self.nombre} [{self.codigo_emp}] · ${self.salario:.2f}"


class Tripulante(Empleado):

    def __init__(self, nombre, cedula, codigo_emp, salario, rol):

        super().__init__(nombre, cedula, codigo_emp, salario)
        self.rol = rol
        self.horas_vuelo = 0

    def sumar_horas_vuelo(self, horas):

        self.horas_vuelo += horas

    def __str__(self):

        return f"Tripulante {self.nombre} [{self.rol}] · {self.horas_vuelo} horas de vuelo"


p = Pasajero("Elkin", "0912345678", "AB-1234")

e = Empleado("Roosevelt", "0987654321", "EMP-01", 1200)

t = Tripulante("Emanuella", "0923456789", "TRIP-01", 1800, "piloto")

p.sumar_millas(500)

e.aumentar_salario(10)

t.sumar_horas_vuelo(120)

p.presentarse()

e.presentarse()

t.presentarse()

print(p)

print(e)

print(t)


# Clase base Figura con método area(). Clases hijas Rectangulo, Circulo, Triangulo que la implementan.
import math

class Figura:
    def area(self):
        raise NotImplementedError("Cada figura debe implementar area()")

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return math.pi * self.radio ** 2

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base * self.altura) / 2

figuras = [
    Rectangulo(5, 3),
    Circulo(5),
    Triangulo(4, 3)
]

for f in figuras:
    print(f"{type(f).__name__}: {f.area():.2f}")

Rectangulo: 15.00
Circulo: 78.54
Triangulo: 6.00

total = sum(f.area() for f in figuras)
print(f"Área total: {total:.2f}")



# Base Vehiculo(marca, modelo). 
# Hija Auto con puertas. Hija Moto con cilindraje. Ambas tienen __str__ propio
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"{self.marca} {self.modelo}"

class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def __str__(self):
        return f"{self.marca} {self.modelo} — {self.puertas} puertas"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindraje):
        super().__init__(marca, modelo)
        self.cilindraje = cilindraje

    def __str__(self):
        return f"{self.marca} {self.modelo} — {self.cilindraje}cc"

auto = Auto("Toyota", "Corolla", 4)
moto = Moto("Honda", "CBR", 600)
for v in [auto, moto]:
    print(v)


# Base Animal(nombre) con método hablar() que dice «(sonido)». Cada hija sobrescribe con su propio sonido.

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre}: (sonido)")

class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre}: ¡Guau!")

class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre}: Miau")

class Ave(Animal):
    def hablar(self):
        print(f"{self.nombre}: Pío pío")

animales = [Perro("Rex"), Gato("Felix"), Ave("Piolín")]
for a in animales:
    a.hablar()

    # Base Empleado(nombre) con método abstracto sueldo_mensual(). 
    # EmpleadoPorHoras calcula sueldo por horas trabajadas × tarifa. EmpleadoFijo tiene sueldo fijo.
    class Empleado:
     def __init__(self, nombre):
        self.nombre = nombre

    def sueldo_mensual(self):
        raise NotImplementedError

    def __str__(self):
        return f"{self.nombre}: ${self.sueldo_mensual():.2f}"


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, horas, tarifa):
        super().__init__(nombre)
        self.horas = horas
        self.tarifa = tarifa

    def sueldo_mensual(self):
        return self.horas * self.tarifa


class EmpleadoFijo(Empleado):
    def __init__(self, nombre, sueldo):
        super().__init__(nombre)
        self.sueldo = sueldo

    def sueldo_mensual(self):
        return self.sueldo


empleados = [
    EmpleadoPorHoras("Ana", 160, 8),
    EmpleadoFijo("Luis", 1500)
]

nomina = 0
for e in empleados:
    print(e)
    nomina += e.sueldo_mensual()

print(f"Total nómina: ${nomina:.2f}")