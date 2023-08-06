"""
Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, 
el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes 
y el total que recibirá en el mes tomando en cuenta su sueldo base más comisiones.
"""

sueldo_base = int(input("Ingrese el sueldo base: "))
ventas_totales = int(input("Ingrese el trabajo extra de las tres ventas: "))

comision = 10 * ventas_totales
total_mes = sueldo_base + comision

print("El dinero por concepto de comisiones es: ", comision)
print("El total que recibira en el mes es un monto de: ", total_mes)

