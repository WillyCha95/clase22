"""
Una tienda ofrece un descuento del 15% sobre el total de la compra, y un cliente desea saber cuánto deberá pagar finalmente sobre su compra.
"""

descuento = 15 / 100

compra_total = int(input("Ingrese el monto total de su compra: "))
descuento = compra_total * descuento
monto_descuento = compra_total - descuento

print("La compra final que debe abonar con el descuento de 15 porciento es: ", monto_descuento)