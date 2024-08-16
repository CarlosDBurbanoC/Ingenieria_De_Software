#EjemploCubo


"""----------------------------------------------------------
Metodos
----------------------------------------------------------"""
def AreaCubo(lado):
    area = lado ** 3 
    return area


"""----------------------------------------------------------
DatoEntrada
----------------------------------------------------------"""
    
ladoL = float(input("Ingrese la longitud de un lado del cubo: "))


"""----------------------------------------------------------
DatosSalida
----------------------------------------------------------"""

areaCubo = AreaCubo(ladoL)
print("El área del cubo es: ", round(areaCubo, 2))

#CDBC