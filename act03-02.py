#Determinar el pago a realizar en una fotocopiadora, donde el precio
#por cada fotocopia es de $20. Al imprimir más de 30 fotocopias se
#realiza un descuento al total del pago de un 10%.
#Notas: 
#Asuma que el cálculo del pago es para un solo cliente. 
#Valide que la cantidad de fotocopias sea mayor a 0.

print("Cada fotocopia vale $20")
print("Ingrese cantidad de hojas para fotocopiar")
cant = input(": ")
cant = int(cant)

if cant > 0:
    subtotal = cant*20
    if cant >=30:
        print("Total a pagar: ", round(int(subtotal)-(int(subtotal)*0.1)))
    else:
        print("Total a pagar: ", subtotal)
else:
    print("Cantidad invalida")
    
