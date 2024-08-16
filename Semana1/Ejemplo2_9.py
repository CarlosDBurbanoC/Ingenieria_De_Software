#Ejemplo2.7


"""----------------------------------------------------------
Metodos
----------------------------------------------------------"""
def sueldoSemanal(sueldoS):
    sueldoS = horasT * pagoH
    return sueldoS

def sueldoSemanalSMLV(sueldoSMLV):#extra :3
    sueldoSMLV = horasT * 5531
    return sueldoSMLV


"""----------------------------------------------------------
DatosEntrada
----------------------------------------------------------"""
    
horasT = float(input("Ingrese horas trabajadas: "))
pagoH = float(input("Ingrese pago por hora: "))


"""----------------------------------------------------------
DatosSalida
----------------------------------------------------------"""

sueldoC= sueldoSemanal(horasT)
sueldoCSMLV= sueldoSemanalSMLV(horasT)
print ("El sueldo semanal a cobrar  es :", round(sueldoC, 2))
print ("El sueldo SMLV semanal a cobrar  es :", round(sueldoCSMLV, 2))

#CDBC