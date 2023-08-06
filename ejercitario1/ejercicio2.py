"""
Una empresa quiere hacer una compra de varias piezas 
"""

monto_total = int(input("Ingrese el monto total de la compra: "))
if monto_total > 500000:
    empresa = 55
    banco = 30
    credito = 100 - (empresa + banco) #resultado 15
else:
    empresa = 70
    credito = 30
    banco = 0

print("Empresa paga: ",empresa,"%:", monto_total * (empresa/100))
print("Banco paga: ",banco,"%:", monto_total * (banco/100))
print("Credito (sin recarga): ",credito,"%:", monto_total * (credito/100))
print("Credito (recarga 20%): ",(credito * 1.2),"%:", monto_total * ((credito * 1.2)/100))

cuenta = (empresa + banco + (credito * 1.2)) / 100
a_pagar = monto_total * cuenta
print("Y pago?", a_pagar)