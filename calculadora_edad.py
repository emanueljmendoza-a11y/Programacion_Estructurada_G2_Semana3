#calcular la edad de una persona y decir si es mayor de edad o no 
from datetime import date 
from colorama import Fore, Style
try:
 año_nacimiento = int(input("dime el año de tu nacimiento: "))
 edad = date.today().year - año_nacimiento
 if edad >= 18:
    print("Eres mayor de edad")
 else:
    print(" eres menor de edad")
except ValueError:
    print(Fore.Red + "Por favor, ingresa un año válido." + Style.RESET_ALL)