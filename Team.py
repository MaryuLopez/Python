#2. Escribe un programa que le pida al usuario un número entero y diga si es: Positivo y par, Positivo e impar, Negativo , Cero( con este ultimo, el cero, se debe de mostrar numero neutro y par),
variable = int(input("Ingrese un número: ")) 
print(variable)
if variable > 0 and variable % 2 == 0:
    print("El número es positivo y par")
elif variable > 0 and variable % 2 !=0:
    print("el numero es positivo e impar")
elif variable < 0 and variable % 2 != 0:
    print("El número es negativo e impar")
elif variable < 0 and variable % 2 == 0:
    print("El número es negativo y par")
elif variable == 0:
    print("El número es neutro y par")
else:
    print("El número es neutro y impar")
