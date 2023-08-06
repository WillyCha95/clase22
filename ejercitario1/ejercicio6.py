"""
Leer dos numeros, si son iguales que se multipliquen, si el primero es mayor que el segundo que se resten y sino que se sumen.
"""

numero1 = int(input("Ingrese un valor numérico: "))
numero2 = int(input("Ingrese un valor numérico: "))

if numero1 == numero2: 
    print("El numero1:",numero1, "por numero2:", numero2, "=",numero1*numero2)

elif numero1 > numero2:
    print(numero1,"-", numero2,"=", numero1-numero2)

else: #if numero1 < numero2: opcional que podemos utilizar
    print(numero1,"+", numero2,"=", numero1+numero2)


"""
if numero1 == numero2:
    res = numero1*numero2

elif numero1 > numero2:
    res = numero1-numero2

else:
    res = numero1+numero2
print("El resultado es:", res)
"""