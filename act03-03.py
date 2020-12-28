#Para un cine capitalino, se requiere el cálculo del total a pagar por
#las entradas que se venden a un cliente.
#El costo general por entrada es de: $3500.- por persona, a excepción de
#los días lunes, martes o miércoles, donde se realiza un descuento del 15%.
#Realice un programa que imprima el total a pagar y que muestre
#la cantidad de entradas vendidas, el descuento aplicado y el total a pagar.
valorEntrada=3500
print("---------------------Bienvenido -------------------")
print("------------ Seleccione día de la funcion --------- \n")
print("(L)unes--(M)artes--(Mi)ercoles--(J)ueves--(V)iernes--(S)abado--(D)omingo")
dia = input(": ")
cantidad = int(input("Ingrese cantidad de entradas: "))


if dia.upper()=="L" or dia.upper()== "M" or dia.upper()=="MI":
    valorEntrada = 3500 - (3500*0.15)
    total = valorEntrada * cantidad
    desto = (cantidad * 3500)*0.15
else:
    total = valorEntrada * cantidad
    desto = 0


print(" --------------------------- \n ---------------------------")
print("Total a Pagar:      ", total)
print("Entradas Vendidas:  ", cantidad)
print("Descuento aplicado: ", desto)
    
    

