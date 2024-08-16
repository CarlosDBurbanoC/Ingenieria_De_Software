#Ejemplo2.5


"""----------------------------------------------------------
Metodos
----------------------------------------------------------"""

def CalcularAreaTriangulo(baseT, alturaT):
    areaTriangulo = (baseT * alturaT) / 2
    return areaTriangulo

def CalcularAreaRectangulo(baseR, alturaR):
    areaRectangulo = (baseR * alturaR)
    return areaRectangulo

def SumarAreas(areaTriangulo, areaRectangulo):
    areaGeneral = areaTriangulo + areaRectangulo
    return areaGeneral


"""----------------------------------------------------------
DatosEntrada
----------------------------------------------------------"""

baseT = float(input("Ingrese la base del triángulo: "))
alturaT = float(input("Ingrese la altura del triángulo: "))

baseR = float(input("Ingrese la base del rectángulo: "))
alturaR = float(input("Ingrese la altura del rectángulo: "))


"""----------------------------------------------------------
DatosSalida
----------------------------------------------------------"""

areaTriangulo = CalcularAreaTriangulo(baseT,alturaT)

areaRectangulo = CalcularAreaRectangulo(baseR,alturaR)

areaGeneral = SumarAreas(areaTriangulo, areaRectangulo)

print("El área del triángulo es:", areaTriangulo)
print("El área del rectángulo es:", areaRectangulo)
print("El área general es:", areaGeneral)

#CDBC