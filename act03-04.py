#determinar numero mayor

print("Ingrese 3 numeros al azar")
num1 = input("Ingrese numero: ")
num2 = input("Ingrese numero: ")
num3 = input("Ingrese numero: ")

num1=int(num1)
num2=int(num2)
num3=int(num3)

may=0
men=0

if num1 > num2 and num1 > num3:
    may = num1
elif num2 > num1 and num2 > num3:
    may=num2
elif num3 > num1 and num3 > num2:
    may=num3

if num1 < num2 and num1 < num3:
    men= num1
if num2 < num1 and num2 < num3:
    men=num2
if num3 < num1 and num3 < num2:
    men= num3


print("numero Mayor: ", may)
print("numero Menor: ", men)
    

