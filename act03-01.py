#El centro de alumnos quiere facilitar la tarea del cálculo de promedios
#y la situación de aprobación del curso, se solicita que a partir de un
#conjunto de 4 notas ingresada por el usuario (por teclado) su promedio
#corresponde a un aprobado (nota>=4) o reprobado (nota<4).
#Debe mostrar un mensaje por pantalla indicando tal situación.

class Estudiante:
    nombre=""
    nota1=0
    nota2=0
    nota3=0
    nota4=0
    promf=0



alumno = Estudiante()
alumno.nombre = input("Ingrese nombre Alumno: ")
alumno.nota1 = int(input("Primera Nota: "))
alumno.nota2 = int(input("Segunda Nota: "))
alumno.nota3 = int(input("Tercera Nota: "))
alumno.nota4 = int(input("Cuarta Nota: "))
alumno.promf = (alumno.nota1 + alumno.nota2 + alumno.nota3 + alumno.nota4)/4

if alumno.promf >=4:
    print("Promedio Final: ", alumno.promf, "Aprobado")    
else:
    print("Promedio Final: ", alumno.promf, "Reprobado")
    
