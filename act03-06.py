print("Seleccione el tipo de combustible a cargar")
print("(1)93 normal - (2)95 súper - (3)97 deluxe")
tipoCombustible = input(": ")
print("Cantidad de litro a cargar")
cantidaddLitros = input(": ")
total = float(cantidaddLitros)*720
print("************** Total a pagar ************  $:", total)
print("Con cuanto pagará")
dinero = int(input(": "))



if tipoCombustible == "1":
    tipoCombustible = "93 normal"
elif tipoCombustible == "2":
    tipoCombustible = "95 súper"
else:
    tipoCombustible = "97 deluxe"
2

print("======= Boleta de venta =======")

print("Combustible           : ",tipoCombustible)
print("Cantidad de Litros    : ",cantidaddLitros)
print("Total a pagar         :$", total)
print("Dinero ingresado      :$",dinero)
print("Vuelto                :$",dinero - total)
