"""
El IPS quiere clasificar a las personas que se jubilarán en el año 2017. Existen tres tipos de jubilaciones, por edad, por antigüedad joven y por antigüedad adulta. 
Las personas para la jubilación por edad deben tener 60 años o más y una antigüedad en su empleo de menos de 25 años.
Las personas para la jubilación por antigüedad joven deben tener menos de 60 años y una antigüedad en su empleo de 25 años o más.
Las personas para antigüedad adulta deben tener 60 años o más y una antigüedad en su empleo de 25 años o más.
"""

edad = int(input("Ingrese la edad que tiene para su jubilacion: "))
antiguedad = int(input("Ingrese cuanto año de antiguedad tiene: "))



if edad >= 60 and antiguedad < 25:
    print ("Jubilacion por edad")

elif edad < 60 and antiguedad >= 25:
    print ("Jubilacion por antiguedad joven")

elif edad >= 60 and antiguedad >= 25:
    print ("Jubilación por antigüedad adulta")

else:
    print ("No cumple con los requisitos de jubilación")


