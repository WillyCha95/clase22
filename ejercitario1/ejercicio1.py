"""
En una tienda se ha establecido la siguiente oferta: 
por compras menores a 100.000 se hace un descuento de 8%, 
pero para compras a partir de 100.000 el descuento es de 10%. 
Se pide ingresar la cantidad y el precio del producto que se compra y 
determinar cuánto se descontará y cuanto se cobrará.
"""

cantidad_total = int(input("Ingrese la cantidad que desea: "))
compra_total = int(input("Ingrese el precio de la compra: "))

if compra_total < 100000:
    descuento = 8 / 100

if compra_total < 100000: 
    descuento = 10 / 100

monto_total = compra_total * cantidad_total
monto_descontado = monto_total * descuento
monto_a_cobrar = monto_total - monto_descontado

print("Monto total: ", monto_total)
print("Descuento: ", descuento)
print("Monto descontado: ", monto_descontado)
print("Monto a cobrar: ", monto_a_cobrar)