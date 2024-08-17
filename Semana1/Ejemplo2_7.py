#Ejemplo2.7


"""----------------------------------------------------------
Metodos
----------------------------------------------------------"""
def ConvertirLitros(litros):
    galones = (litros / 3785)
    return galones

def CalcularPago(galones, PagoPorGalon):
    pago = round(galones * PagoPorGalon, 2)
    return pago


"""----------------------------------------------------------
DatosEntrada
----------------------------------------------------------"""
    
litros = float(input("Ingrese la producción de litros: "))
PagoPorGalon = float(input("Ingrese el costo por galon: "))


"""----------------------------------------------------------
DatosSalida
----------------------------------------------------------"""

galones = ConvertirLitros(litros)
pago = CalcularPago(galones, PagoPorGalon)

print("La cantidad de galones es:", round(galones, 2))
print("El pago a cobrar por galones es :", round(pago, 2))


#CDBC