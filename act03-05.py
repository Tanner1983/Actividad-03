#tiene un valor base de $6.000 y variará según las siguientes condiciones:
#a.	Temporada alta: aumenta en 20%.
#b.	Escolares: el descuento es siempre el 80%.
#c.	Es frecuente: 10% adicional.
#Asuma que el cálculo del pago es para un sólo cliente e imprímalo en pantalla.

valorBase = 6000
valorAlta = 6000 + (valorBase * 0.2)
valorEstu = 6000 - (valorBase * 0.8)
valorFrec = 6000 - (valorBase * 0.1)

print("Bienvenido")
temporada = input("Temporada Alta S/N: ")
estudiant = input("Es estudiante S/N: ")
pasajerof = input("Pasajero frecuente? S/N: ")

if temporada.lower() == "n":
    pago = valorBase
else:
    pago = valorAlta

    
if estudiant.upper() == "S":
    pago = pago - (pago *0.8)
    

if pasajerof.upper() == "S":
    pago = pago - (pago * 0.1)
   
print("Valor a pagar: ", pago)
