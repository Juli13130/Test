#Para ocultar los caracteres
import getpass
#Para limpiar la consola
import os
#Par usar delay
from time import sleep

#Usuarios y variables
estudiante1_email ="estudiante1@ayed.com"
estudiante1_contrasenia ="111222"
estudiante2_email ="estudiante2@ayed.com"
estudiante2_contrasenia ="333444"
estudiante3_email ="estudiante3@ayed.com"
estudiante3_contrasenia ="555666"

inicio=False

def limpiar_pantalla():

    #os.system("clear")
    os.system('cls')

#Login

def login():
    #Var a usar
    global inicio
    correo=""
    contrasenia=""
    intentos = 3
    while intentos > 0 :
        correo= input ("Ingrese su correo electronico: ")
        contrasenia = input("Ingrese la contrasenia: ")
        #contrasenia == getpass.getpass("Ingrese la contrasenia: ")
        if (correo == estudiante1_email and contrasenia == estudiante1_contrasenia) or (correo == estudiante2_email and contrasenia == estudiante2_contrasenia) or (correo == estudiante3_email and contrasenia == estudiante3_contrasenia):
            print ("Inicio de sesion correcto.")
            intentos = 0
            inicio = True
            sleep(3)
            limpiar_pantalla()
        else:
            intentos -=1
            print("Credenciales incorrectas.")
            print("Quedan ",intentos," intentos")
            sleep(3)
            limpiar_pantalla()

def menu_principal():
    print("\n")
    print("1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadisticos")
    print("0. Salir")

def menu_print_gestion_perfil():
    print("1. Gestionar mi perfil")
    print("a. Editar mis datos personales")
    print("b. Eliminar mi perfil")
    print("c. Volver")
    
def menu_opc_gestion_perfil():
    limpiar_pantalla()
    menu_print_gestion_perfil()
    opc = input("Ingrese una opcion: ")
    while opc != "c":
        if opc== "a":
            print("Menu editar mis datos personales")
        #Para esta entrega los otros menúes no andan
        else:
            print("En construccion")
        limpiar_pantalla()
        menu_print_gestion_perfil()
        opc = input("Ingrese una opcion: ")
    
def menu_print_gestion_candidatos():
    print("2. Gestionar candidatos")
    print("a. Ver candidatos")
    print("b. Reportar un candidato")
    print("c. Volver")

def menu_opc_gestion_candidatos():
    limpiar_pantalla()
    menu_print_gestion_candidatos()
    opc = input("Ingrese una opcion: ")
    while opc != "c":
        if opc== "a":
            print("Menu ver candidatos")
        #Para esta entrega los otros menúes no andan
        else:
            print("En construccion")
        limpiar_pantalla()
        menu_print_gestion_candidatos()
        opc = input("Ingrese una opcion: ")
    
def menu_print_matcheos():
    print("3. Matcheos")
    print("a. Ver matcheos")
    print("b. Eliminar un matcheo")
    print("c. Volver")
    
def menu_opc_matcheos():
    limpiar_pantalla()
    menu_print_matcheos()
    # opc = input("Ingrese una opcion: ")
    # while opc != "c":
    #     if opc== "a":
    #         print("Menu ver candidatos")
    #     #Para esta entrega los otros menúes no andan
    #     else:
    #         print("En construccion")
    #     limpiar_pantalla()
    #     menu_print_matcheos()
    #     opc = input("Ingrese una opcion: ")
    
###Programa###

    
login()
if inicio == True:
    opc_principal=1
    while opc_principal != 0:
        limpiar_pantalla()
        menu_principal()
        opc_principal = int(input("Ingrese opcion: "))
        if opc_principal == 1:
            menu_opc_gestion_perfil()
        elif opc_principal == 2:
            menu_opc_gestion_candidatos()
        elif opc_principal ==3:
            menu_opc_matcheos()
        elif opc_principal==4:
            print("En construccion")
        limpiar_pantalla()
    print("El sistema se cerrara.")
else:
    print("Ingreso incorrectamente las credenciales. El sistema se cerrara")
    

