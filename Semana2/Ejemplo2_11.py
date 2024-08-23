#Ejemplo2.11


"""----------------------------------------------------------
DatosEntrada
----------------------------------------------------------"""
largo = float(input("Ingrese el largo (L) de la alberca: "))
ancho = float(input("Ingrese el ancho (A) de la alberca: "))
profundidad = float(input("Ingrese la profundidad (P) de la alberca: "))
pago = float(input("Ingrese la pago por metro cúbico de agua: "))

"""----------------------------------------------------------
Calculos
----------------------------------------------------------"""
volumen = largo * ancho * profundidad
costoTotal = volumen * pago

"""----------------------------------------------------------
DatosSalida
----------------------------------------------------------"""
print(f"Cantidad de metro cubicos: {volumen:.2f} ")
print(f"El costo total a pagar es: ${costoTotal:.2f}")


#CDBC