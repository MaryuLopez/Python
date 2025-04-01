#EJERCICIOS

#1. relizar una tabla de multiplicar, el ejercicio consta de Pedir al usuario un determininado numero este numero debe ser unicamente numero positivo del 1 al 10 y ,de lo contrario muestra prints invalidos, y de este numero se va a mostrar una tabla de multiplicar desde el 1 hasta el 10 de ese numero.
#Ejemplo:
#Numero ingresado por consola => 7
#SALIDA DEL CODIGO
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# .
# .
# .
# 7 x 10 = 70 :)

#num = int(input("Ingrese un numero del 1 al 10: "))
#for num2 in range(1,10+1):
#    print(f"{num} * {num2} = {num*num2}")






#2. Suma de numeros, pedir al usuario un numero, se va a recorrer esos numeros de tal manera que con condiconales se separan los impares de los pares, y se realizan una suma de todos los pares y una suma de todos los impares.
#EJEMPLO
# numero = 5
#Salida del codigo
#Suma de pares: 6 => (Porque se sumo 2 y 4)
#suma de impares: 9 => (Porque se sumo el 1,3,5)

#n = int(input("Ingrese un numero: "))
#par = 0
#impar = 0
#for n2 in range(1, n+1):
#    if n2 % 2 == 0:
#        par += n2
#    else:
#        impar += n2
#print(f"Suma de pares: {par}")
#print(f"Suma de impares: {impar}")





#3. Ejercicio de asterisco, debe pedir al usuario un numero positivo unicamente, de ese numero se va a imprimir una piramide de asteriscos de la siguiente manera
#EJEMPLO:
#numero = 5
#SALIDA DEL CODIGO:
#*
#**
#**
#***
#****
#*****

#numero = int(input("Ingrese un numero positivo: "))
#for n in range(1,numero+1):
#    print("*" * n)







#NUEVOS EJERCICIOS
#4.  Le van a pedir al usuario 3 numeros, y esos numeros deben organizalor de menor a mayor, de tal manera que por consola me va a mostrar los 3 numeros organizados de mayor a menor (Usando condicionales)

#n1 = int(input("Ingrese un numero: "))
#n2 = int(input("Ingrese otro numero: "))
#n3 = int(input("Ingrese un numero diferente: "))

#if n1 > n2 and n1 > n3:
#    if n2>n3:
#        print(n3, n2, n1)
#elif n1 > n2 and n1 > n3:
#    if n3>n2:
#        print(n2, n3, n1)
#elif n2> n1 and n2>n3:
#    if n1>n3:
#        print(n3, n1, n2)
#elif n2 > n1 and n2 >n3:
#    if n3>n1:
#        print(n1, n3, n2)
#elif n3>n1 and n3>n2:
#    if n1>n2:
#        print(n2, n1, n3)
#else:
#        print(n1, n2, n3)





#5.  Crea un programa que determine si un triagnulo es Equilatero(todos sus lados son iguales), isosceles(Dos lados igaules) o escaleno (No tiene lados iguale ), reglas, usar input y condicionales 

#lado1 = float(input("Ingrese el valor de un lado del triangulo: "))
#lado2 = float(input("Ingrese el valor del otro lado del triangulo: "))
#lado3 = float(input("Ingrese el ultimo valor del triangulo: "))

#if lado1 == lado2 and lado1 == lado3:
#    print("El triangulo es equilatero.")
#elif lado1 == lado2 or lado1 == lado3 or lado3 == lado2:
#    print("El triangulo es isoceles.")
#else:
#    print("El triangullo es escaleno.")





#6.  Escribe un programa que solicite al usuario un número entero .Luego, el programa debe recorrer(range(), for) los números del 1 hasta numero e imprimir:
# "Fizz" si el número es divisible por 3.
# "Buzz" si el número es divisible por 5.
# "FizzBuzz" si es divisible por ambos (3 y 5).
# El número mismo si no es divisible por ninguno.

#num = int(input("Ingrese un numero entero: "))
#for n in range(1, num+1):
#    if n % 3 == 0 and n%5 ==0:
#        print('{}= FizzBuzz' .format(n))
#    elif n % 3==0:
#        print('{}= Fizz'.format(n))
#    elif n % 5 == 0:
#        print('{}= Buzz' .format(n))
#    else:
#        print('{}= no es divisible por 3 ni por 5' .format(n))


#7. Escribe un programa que le pida al usuario un número entero y diga si es: Positivo y par, Positivo e impar, Negativo , Cero( con este ultimo, el cero, se debe de mostrar numero neutro y par), 

#num = int(input("Ingrese un numero entero: "))

#if num >0 and num %2 ==0:
#    print("El numero es positivo y par")
#elif num >0 and num %3 ==0:
#    print("El numero es positivo e impar")
#elif num <0:
#    print("El numero es negativo")
#else:
#    print("El cero es neutro y par")