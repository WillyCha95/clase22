"""
En una tienda se efectúa una promoción en la cual se hace un descuento sobre el valor de la cuenta total, según el color de la bolilla que el cliente saque al pagar en caja. Si la bolilla es de color blanco no se hará descuento alguno, si es verde se le hará un 10% de descuento, si es amarilla un 25%, si es azul un 50% y si es roja un 100%. Determinar la cantidad final que el cliente deberá pagar por su compra. Se sabe que sólo hay bolillas de los colores mencionados.
"""

cuenta_total = int(input("Ingrese el valor total de la compra: "))
bolilla = input("Ingresa el color de la bolilla: [blanco, verde, amarilla, azul o roja] ")
descuento = 0

if bolilla == "blanco":
    descuento = 0
elif bolilla == "verde":
    descuento = 10
elif bolilla == "amarilla":
    descuento = 25
elif bolilla == "azul":
    descuento = 50
elif bolilla == "roja":
    descuento = 100
else:
    print("Color de bolilla inadmisible")
    exit 

"""
a_pagar = cuenta_total - (cuenta_total * (descuento / 100))
a_pagar = cuenta_total - (cuenta_total * (0,1))
a_pagar = cuenta_total - (1 - (1 * (0,1)))
a_pagar = cuenta_total - (1 - 0,1)
a_pagar = cuenta_total * (0.9)
"""
a_pagar = cuenta_total * (1 - (descuento/100))

print("Monto compra:", cuenta_total)
print("Color de bolilla:", bolilla)
print("Porcentaje de descuento:", descuento)
print("A pagar:", a_pagar)