'''
estudiante*_email, estudiante*_contrasenia, estudiante*_bio, estudiante*_hobbie, correo, contrasenia, bio, hobbie  :string
inicio  :boolean
intentos, opcion, opcion_principal    :integer

'''

#Para ocultar los caracteres
import getpass
#Para limpiar la consola
import os
#Par usar delay
from time import sleep

#Usuarios y variables
estudiante1_email ="estudiante1@ayed.com"
estudiante1_contrasenia ="111222"
estudiante1_fec=""
estudiante1_bio=""
estudiante1_hobbie=""
estudiante2_email ="estudiante2@ayed.com"
estudiante2_contrasenia ="333444"
estudiante2_fec=""
estudiante2_bio=""
estudiante2_hobbie=""
estudiante3_email ="estudiante3@ayed.com"
estudiante3_contrasenia ="555666"
estudiante3_fec=""
estudiante3_bio=""
estudiante3_hobbie=""
# correo=""

inicio=False

def limpiar_pantalla():

    #os.system("clear")
    os.system('cls')

#Login

def login():
    #Var a usar
    global inicio
    global correo
    intentos = 3
    while intentos > 0 :
        correo= input ("Ingrese su correo electronico: ")
        contrasenia = getpass.getpass("Ingrese la contrasenia: ")
        if (correo == estudiante1_email and contrasenia == estudiante1_contrasenia) or (correo == estudiante2_email and contrasenia == estudiante2_contrasenia) or (correo == estudiante3_email and contrasenia == estudiante3_contrasenia):
            print ("Inicio de sesion correcto.")
            intentos = 0
            inicio = True
            sleep(2)
            limpiar_pantalla()
        else:
            intentos -=1
            print("Credenciales incorrectas.")
            print("Quedan ",intentos," intentos")
            sleep(2)
            limpiar_pantalla()

def menu_editar_datos_personales():
    global correo
    global estudiante1_fec
    global estudiante1_bio
    global estudiante1_hobbie
    global estudiante2_fec
    global estudiante2_bio
    global estudiante2_hobbie
    global estudiante3_fec
    global estudiante3_bio
    global estudiante3_hobbie
    #Asigno los datos del estudiante a las variables auxiliares.
    if correo==estudiante1_email:
        fec=estudiante1_fec
        bio=estudiante1_bio
        hobbie=estudiante1_hobbie
    if correo==estudiante2_email:
        fec=estudiante2_fec
        bio=estudiante2_bio
        hobbie=estudiante2_hobbie
    if correo==estudiante3_email:
        fec=estudiante3_fec
        bio=estudiante3_bio
        hobbie=estudiante3_hobbie
    opcion=1
    while opcion!="4":
        print("Sus datos actuales son: ")
        print("Su fecha de nacimiento es: ",fec)
        print("Su biografia es: ",bio)
        print("Su hobbie es: ",hobbie)
        print("Que dato desea cambiar?")
        print("1. Fecha de naciemiento")
        print("2. Biografia")
        print("3. Hobbie")
        print("4. Salir")
        opcion= int(input("Ingrese el numero: "))
        match opcion:
            case 1:
                fec=input("Ingrese la nueva fecha de nacimiento en formato YYYY-MM-DD : ")
            case 2:
                bio=input("Ingrese la nueva biografia: ")
            case 3:
                hobbie=input("Ingrese el nuevo hobbie: ")
    #Asigno el valor de las variables auxiliares al estudiante
    if correo==estudiante1_email:
        estudiante1_fec=fec
        estudiante1_bio=bio
        estudiante1_hobbie=hobbie
    if correo==estudiante2_email:
        estudiante2_fec=fec
        estudiante2_bio=bio
        estudiante2_hobbie=hobbie
    if correo==estudiante3_email:
        estudiante3_fec=fec
        estudiante3_bio=bio
        estudiante3_hobbie=hobbie

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
    opcion = input("Ingrese una opcion: ")
    while opcion != "c":
        if opcion== "a":
            menu_editar_datos_personales()
        #Para esta entrega los otros menúes no andan
        else:
            print("En construccion")
        limpiar_pantalla()
        menu_print_gestion_perfil()
        opcion = input("Ingrese una opcion: ")
    
def menu_print_gestion_candidatos():
    print("2. Gestionar candidatos")
    print("a. Ver candidatos")
    print("b. Reportar un candidato")
    print("c. Volver")

def menu_opc_gestion_candidatos():
    limpiar_pantalla()
    menu_print_gestion_candidatos()
    opcion = input("Ingrese una opcion: ")
    while opcion != "c":
        if opcion== "a":
            print("Menu ver candidatos")
        #Para esta entrega los otros menúes no andan
        else:
            print("En construccion")
        limpiar_pantalla()
        menu_print_gestion_candidatos()
        opcion = input("Ingrese una opcion: ")
    
def menu_print_matcheos():
    print("3. Matcheos")
    print("a. Ver matcheos")
    print("b. Eliminar un matcheo")
    print("c. Volver")
    
def menu_opc_matcheos():
    limpiar_pantalla()
    menu_print_matcheos()
    # opcion = input("Ingrese una opcion: ")
    # while opcion != "c":
    #     if opcion== "a":
    #         print("Menu ver candidatos")
    #     #Para esta entrega los otros menúes no andan
    #     else:
    #         print("En construccion")
    #     limpiar_pantalla()
    #     menu_print_matcheos()
    #     opcion = input("Ingrese una opcion: ")
    
###Programa###

    
login()
if inicio:
    opc_principal=1
    while opc_principal != 0:
        limpiar_pantalla()
        menu_principal()
        opc_principal = int(input("Ingrese opcion: "))
        match opc_principal:
            case 1:
                menu_opc_gestion_perfil()
            case 2:
                menu_opc_gestion_candidatos()
            case 3:
                menu_opc_matcheos()
            case 4:
                print("En construccion")
        limpiar_pantalla()
    print("El sistema se cerrara.")
else:
    print("Ingreso incorrectamente las credenciales. El sistema se cerrara")
    