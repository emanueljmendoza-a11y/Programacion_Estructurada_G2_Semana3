#Almacenar las funciones
edades = []
def almacenarEdades(edad):
    edades.append(edad)

def mostrarEdades():
    return edades

for i in range(10):
    while True:
        try:
            edad = int(input("Estudiante #{} ingrese su edad: ".format(i+1)))
            almacenarEdades(edad)
            break
        except ValueError:
            print("Se debe ingresar un numero entero")