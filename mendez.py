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
# 7 x 10 = 70


#2. Suma de numeros, pedir al usuario un numero, se va a recorrer esos numeros de tal manera que con condiconales se separan los impares de los pares, y se realizan una suma de todos los pares y una suma de todos los impares.
#EJEMPLO
# numero = 5
#Salida del codigo
#Suma de pares: 6 => (Porque se sumo 2 y 4)
#suma de impares: 9 => (Porque se sumo el 1,3,5)


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


n = int(input("pon el numero: "))
for a in range(1,11):
    print (n ," * " , a ,"=", n * a)
# tabla de multiplicaichon


# ejercicio raro de pares y impares

#x = int(input("pon tu numero: "))
#par = 0
#ipar = 0
#for x in range(1,x+1):
#    if x % 2 == 0:
#        par += x
#    else:
#        ipar += x
#print (par, "   ", ipar)

# asteriscos

# x = int(input("pon tu numero: "))
# for a in range(1,x+1):
#     print ("*" * a)

# #terminado