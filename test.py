'''
estudiante*nombre, estudiante*_email, estudiante*_contrasenia, estudiante*_bio, estudiante*_hobbie, correo, contrasenia, bio, hobbie, seleccion_numerica, nombre_*  :string
inicio, automatico  :boolean
intentos, opcion, opcion_principal, opcion_ruleta, probabilidad_*    :integer

sin definir: estudiante*_fec, fec

# los * significan diferentes variables similares
'''

# Para ocultar los caracteres
import getpass
# Para limpiar la consola
import os
# Para usar delay
from time import sleep
# Para ruleta
import random
# Para calcular la edad
from datetime import datetime


# Usuarios y variables
estudiante1_nombre = "juan 1"
estudiante1_email = "estudiante1@ayed.com"
estudiante1_contrasenia = "111222"
estudiante1_fec = "1997-09-03"
estudiante1_bio = ""
estudiante1_hobbie = ""
estudiante2_nombre = "juan 2"
estudiante2_email = "estudiante2@ayed.com"
estudiante2_contrasenia = "333444"
estudiante2_fec = "2000-05-05"
estudiante2_bio = ""
estudiante2_hobbie = ""
estudiante3_nombre = "juan 3"
estudiante3_email = "estudiante3@ayed.com"
estudiante3_contrasenia = "555666"
estudiante3_fec = "2000-06-01"
estudiante3_bio = ""
estudiante3_hobbie = ""
# correo=""

inicio = False


def limpiar_pantalla():
    os.system('cls')

# Login


def login():
    # Var a usar
    global inicio
    global correo
    intentos = 3
    while intentos > 0:
        correo = input("Ingrese su correo electronico: ")
        contrasenia = getpass.getpass("Ingrese la contrasenia: ")
        if (correo == estudiante1_email and contrasenia == estudiante1_contrasenia) or (correo == estudiante2_email and contrasenia == estudiante2_contrasenia) or (correo == estudiante3_email and contrasenia == estudiante3_contrasenia):
            print("Inicio de sesion correcto.")
            intentos = 0
            inicio = True
            sleep(2)
            limpiar_pantalla()
        else:
            intentos -= 1
            print("Credenciales incorrectas.")
            print("Quedan ", intentos, " intentos")
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
    # Asigno los datos del estudiante a las variables auxiliares.
    if correo == estudiante1_email:
        fec = estudiante1_fec
        bio = estudiante1_bio
        hobbie = estudiante1_hobbie
    if correo == estudiante2_email:
        fec = estudiante2_fec
        bio = estudiante2_bio
        hobbie = estudiante2_hobbie
    if correo == estudiante3_email:
        fec = estudiante3_fec
        bio = estudiante3_bio
        hobbie = estudiante3_hobbie
    opcion = 0
    while opcion != "4":
        print("Sus datos actuales son: ")
        print("Su fecha de nacimiento es: ", fec)
        print("Su biografia es: ", bio)
        print("Su hobbie es: ", hobbie)
        print("Que dato desea cambiar?")
        print("1. Fecha de naciemiento")
        print("2. Biografia")
        print("3. Hobbie")
        print("4. Salir")
        seleccion_numerica = input("Ingrese su seleccion: ")
        while not seleccion_numerica.isnumeric():
            seleccion_numerica = input("Ingrese su seleccion (por su numero): ")
        opcion = int(seleccion_numerica)
        match opcion:
            case 1:
                fec = input("Ingrese la nueva fecha de nacimiento en formato YYYY-MM-DD : ")
            case 2:
                bio = input("Ingrese la nueva biografia: ")
            case 3:
                hobbie = input("Ingrese el nuevo hobbie: ")
    # Asigno el valor de las variables auxiliares al estudiante
    if correo == estudiante1_email:
        estudiante1_fec = fec
        estudiante1_bio = bio
        estudiante1_hobbie = hobbie
    if correo == estudiante2_email:
        estudiante2_fec = fec
        estudiante2_bio = bio
        estudiante2_hobbie = hobbie
    if correo == estudiante3_email:
        estudiante3_fec = fec
        estudiante3_bio = bio
        estudiante3_hobbie = hobbie


def menu_principal():
    print("\n")
    print("1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadisticos")
    print("0. Salir")


def menu_print_gestion_perfil():
    print("1. Gestionar mi perfil")
    print(" a. Editar mis datos personales")
    print(" b. Eliminar mi perfil")
    print(" c. Volver")


def menu_opc_gestion_perfil():
    limpiar_pantalla()
    menu_print_gestion_perfil()
    opcion = input("Ingrese una opcion: ")
    while opcion != "c":
        if opcion == "a":
            menu_editar_datos_personales()
        # Para esta entrega los otros menúes no andan
        else:
            print("En construccion")
        limpiar_pantalla()
        menu_print_gestion_perfil()
        opcion = input("Ingrese una opcion: ")


def menu_print_gestion_candidatos():
    print("2. Gestionar candidatos")
    print(" a. Ver candidatos")
    print(" b. Reportar un candidato")
    print(" c. Volver")


def menu_opc_gestion_candidatos():
    limpiar_pantalla()
    menu_print_gestion_candidatos()
    opcion = input("Ingrese una opcion: ")
    while opcion != "c":
        if opcion == "a":
            menuvercandidatos()
        # Para esta entrega los otros menúes no andan
        else:
            print("En construccion")
        limpiar_pantalla()
        menu_print_gestion_candidatos()
        opcion = input("Ingrese una opcion: ")

def vercandidatos():

    global estudiante1_fec
    global estudiante1_bio
    global estudiante1_hobbie
    global estudiante2_fec
    global estudiante2_bio
    global estudiante2_hobbie
    global estudiante3_fec
    global estudiante3_bio
    global estudiante3_hobbie

    print("Candidatos: ")
    print("Nombre del candidato 1: ",estudiante1_nombre)
    print("Fecha de nacimiento del candidato 1: ",estudiante1_fec)
    print("Edad del candidato 1: ", calcularedad(estudiante1_fec))
    print("Biografia del estudiante 1: ",estudiante1_bio)
    print("Hobbie del estudiante 1 : ",estudiante1_hobbie)
    print("/n")
    print("Nombre del candidato 2: ",estudiante2_nombre)
    print("Fecha de nacimiento del candidato 2: ",estudiante2_fec)
    print("Edad del candidato 2: ", calcularedad(estudiante2_fec))
    print("Biografia del estudiante 2: ",estudiante2_bio)
    print("Hobbie del estudiante 2 : ",estudiante2_hobbie)
    print("/n")
    print("Nombre del candidato 3: ",estudiante3_nombre)
    print("Fecha de nacimiento del candidato 3: ",estudiante3_fec)
    print("Edad del candidato 3: ", calcularedad(estudiante3_fec))
    print("Biografia del estudiante 3: ",estudiante3_bio)
    print("Hobbie del estudiante 3 : ",estudiante3_hobbie)
    print("/n")

def calcularedad(fechadenacimiento):
    fechadenacimiento=datetime.strptime(fechadenacimiento,'%Y-%m-%d')
    hoy=datetime.now()
    edad=hoy.year-fechadenacimiento.year
    if (hoy.month,hoy.day) < (fechadenacimiento.month, fechadenacimiento.day):
        edad = edad-1
    return edad

def menuvercandidatos():
    limpiar_pantalla()
    vercandidatos()
    mgestudiante1=input("Ingrese el nombre del estudiante que le gusta: ")
    while mgestudiante1 != estudiante1_nombre or mgestudiante1 != estudiante2_nombre or mgestudiante1 != estudiante3_nombre:
        print("Ingreso el nombre de forma incorrecta.")
        vercandidatos()
        mgestudiante1=input("Ingrese el nombre del estudiante que le gusta: ")

def menu_print_matcheos():
    print("3. Matcheos")
    print(" a. Ver matcheos")
    print(" b. Eliminar un matcheo")
    print(" c. Volver")
    print(" x. Ruleta de afinidad")


def menu_opc_matcheos():
    limpiar_pantalla()
    menu_print_matcheos()
    opcion = input("Ingrese una opcion: ")
    while opcion != "c":
        match opcion:
            case "a":
                print("Menu ver candidatos")
            case "x":
                menu_ruleta()
        limpiar_pantalla()
        menu_print_matcheos()
        opcion = input("Ingrese una opcion: ")


def menu_ruleta():
    limpiar_pantalla()
    ruleta_instrucciones()
    seleccion_numerica = input("Ingrese una opcion: ")
    while not seleccion_numerica.isnumeric():
        seleccion_numerica = input("Ingrese una opcion (por su num): ")
    opcion_ruleta = int(seleccion_numerica)
    while seleccion_numerica != 0:
        match opcion_ruleta:
            case 1:
                global automatico
                automatico = True
                ruleta()
            case 2:
                ruleta()


def ruleta():
    numran = random.randint(0, 100)
    if automatico is False:
        nombre_A = input("Persona #1: ")
        nombre_B = input("Persona #2: ")
        nombre_C = input("Persona #3: ")
    else:
        nombre_A = input("Nombre #1: ")
        while nombre_A is not estudiante1_nombre or estudiante2_nombre or estudiante3_nombre:
            nombre_A = input("Nombre #1: ")
        nombre_B = input("Nombre #1: ")
        while nombre_B is not estudiante1_nombre or estudiante2_nombre or estudiante3_nombre:
            nombre_B = input("Nombre #1: ")
        nombre_C = input("Nombre #1: ")
        while nombre_C is not estudiante1_nombre or estudiante2_nombre or estudiante3_nombre:
            nombre_C = input("Nombre #1: ")
    print("Ahora asignamos nuestra afinidad con ellos")
    print("solo tienes 100 puntos de afinidad para distribuir")
    probabilidad_A = int(input("Afinidad con ", nombre_A, ": "))
    probabilidad_B = int(input("Afinidad con ", nombre_B, ": "))
    probabilidad_C = int(input("Afinidad con ", nombre_C, ": "))
    while probabilidad_A + probabilidad_B + probabilidad_C != 100:
        print(probabilidad_A + probabilidad_B + probabilidad_C, "?")
        probabilidad_A = int(input("Afinidad con ", nombre_A, ": "))
        probabilidad_B = int(input("Afinidad con ", nombre_B, ": "))
        probabilidad_C = int(input("Afinidad con ", nombre_C, ": "))
    print("Se tiro un dado de ", numran, " ", probabilidad_C, " es el sobrante")
    sleep(0.5)
    limpiar_pantalla()
    if numran < probabilidad_A:
        print(nombre_A)
        if automatico:
            print("Matcheo añadido")
            # ############################## necesito registro de matcheos o algo
    elif numran >= probabilidad_A and numran < probabilidad_B + probabilidad_A:
        print(nombre_B)
        if automatico:
            print("Matcheo añadido")
    else:
        print(nombre_C)
        if automatico:
            print("Matcheo añadido")


def ruleta_instrucciones():
    print("La Ruleta de afinidad es una forma de seleccionar tu matcheo")
    print("usando tu afinidad con tres personas!")
    print("Puedes elegir ser matcheado automaticamente o solo mostrar el nombre")
    print("(necesitaras el nombre exacto para hacerlo automaticamente asi que seria buena idea ir a [Gestion de candidatos])")
    print(" 0-Salir")
    print(" 1-automatico")
    print(" 2-Manual")


# ##Programa## #
login()
if inicio:
    opc_principal = 5
    while opc_principal != 0:
        limpiar_pantalla()
        menu_principal()
        seleccion_numerica = input("Ingrese su seleccion: ")
        while not seleccion_numerica.isnumeric():
            seleccion_numerica = input("Ingrese su seleccion (por su numero): ")
        opc_principal = int(seleccion_numerica)
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
