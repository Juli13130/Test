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
estudiante1_bio = "Hola, soy Juan 1 :)"
estudiante1_hobbie = "Matar mosquitos"
estudiante2_nombre = "juan 2"
estudiante2_email = "estudiante2@ayed.com"
estudiante2_contrasenia = "333444"
estudiante2_fec = "2000-05-05"
estudiante2_bio = "Hola, soy Juan 2 :)"
estudiante2_hobbie = "Soy skater 8)"
estudiante3_nombre = "juan 3"
estudiante3_email = "estudiante3@ayed.com"
estudiante3_contrasenia = "555666"
estudiante3_fec = "2000-06-01"
estudiante3_bio = "Hola, soy Juan 3 :)"
estudiante3_hobbie = "Fulbito"
estudiante4_nombre = "juan 4"
estudiante4_email = "estudiante4@ayed.com"
estudiante4_contrasenia = "777888"
estudiante4_fec = "1980-06-01"
estudiante4_bio = "Hola, soy Juan 4 :)"
estudiante4_hobbie = "CS 1.6"
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
    global estudiante4_fec
    global estudiante4_bio
    global estudiante4_hobbie
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
    if correo == estudiante4_email:
        fec = estudiante4_fec
        bio = estudiante4_bio
        hobbie = estudiante4_hobbie
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
                fec=datetime.strptime(fec,'%Y-%m-%d').date()
                hoy=datetime.now()
                while (hoy.year < fec.year) or (hoy.year - fec.year) > 150  :
                    print("El año no puede ser posterior al actual o anterior a 150 años")
                    fec = input("Ingrese la nueva fecha de nacimiento en formato YYYY-MM-DD : ")
                    fec=datetime.strptime(fec,'%Y-%m-%d').date()
                while (hoy.year == fec.year) and (hoy.month < fec.month) :
                    print("El mes no puede ser posterior al actual")
                    fec = input("Ingrese la nueva fecha de nacimiento en formato YYYY-MM-DD : ")
                    fec=datetime.strptime(fec,'%Y-%m-%d').date()
                while (hoy.year == fec.year and hoy.month == fec.month and hoy.day < fec.day) :
                    print("El día no puede ser posterior al actual")
                    fec = input("Ingrese la nueva fecha de nacimiento en formato YYYY-MM-DD : ")
                    fec=datetime.strptime(fec,'%Y-%m-%d').date()
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
    if correo == estudiante4_email:
        estudiante4_fec = fec
        estudiante4_bio = bio
        estudiante4_hobbie = hobbie


def menu_principal():
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
        match opcion:
            case "a":
                menu_editar_datos_personales()
            case "b":
                print("En construccion...")
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
        match opcion:
            case "a":
                menuvercandidatos()
            case _:
                print("En construccion...")
                sleep(5)
        limpiar_pantalla()
        menu_print_gestion_candidatos()
        opcion = input("Ingrese una opcion: ")

def vercandidatos():

    if correo == estudiante1_email:
        print("Candidatos: ")
        print("")
        print("Nombre del candidato: ",estudiante2_nombre)
        print("Fecha de nacimiento del candidato: ",estudiante2_fec)
        print("Edad del candidato: ", calcularedad(estudiante2_fec))
        print("Biografia del estudiante: ",estudiante2_bio)
        print("Hobbie del estudiante: ",estudiante2_hobbie)
        print("")
        print("Nombre del candidato: ",estudiante3_nombre)
        print("Fecha de nacimiento del candidato: ",estudiante3_fec)
        print("Edad del candidato: ", calcularedad(estudiante3_fec))
        print("Biografia del estudiante: ",estudiante3_bio)
        print("Hobbie del estudiante: ",estudiante3_hobbie)
        print("")
        print("Nombre del candidato: ",estudiante4_nombre)
        print("Fecha de nacimiento del candidato: ",estudiante4_fec)
        print("Edad del candidato: ", calcularedad(estudiante4_fec))
        print("Biografia del estudiante: ",estudiante4_bio)
        print("Hobbie del estudiante: ",estudiante4_hobbie)
        print("")

    elif correo == estudiante2_email:
        print("Candidatos: ")
        print("Nombre del candidato: ",estudiante1_nombre)
        print("Fecha de nacimiento del candidato: ",estudiante1_fec)
        print("Edad del candidato: ", calcularedad(estudiante1_fec))
        print("Biografia del estudiante: ",estudiante1_bio)
        print("Hobbie del estudiante: ",estudiante1_hobbie)
        print("")
        print("Nombre del candidato: ",estudiante3_nombre)
        print("Fecha de nacimiento del candidato: ",estudiante3_fec)
        print("Edad del candidato: ", calcularedad(estudiante3_fec))
        print("Biografia del estudiante: ",estudiante3_bio)
        print("Hobbie del estudiante: ",estudiante3_hobbie)
        print("")
        print("Nombre del candidato: ",estudiante4_nombre)
        print("Fecha de nacimiento del candidato: ",estudiante4_fec)
        print("Edad del candidato: ", calcularedad(estudiante4_fec))
        print("Biografia del estudiante: ",estudiante4_bio)
        print("Hobbie del estudiante: ",estudiante4_hobbie)
        print("")
    
    elif correo == estudiante3_email:
        print("Candidatos: ")
        print("Nombre del candidato: ",estudiante1_nombre)
        print("Fecha de nacimiento del candidato: ",estudiante1_fec)
        print("Edad del candidato: ", calcularedad(estudiante1_fec))
        print("Biografia del estudiante: ",estudiante1_bio)
        print("Hobbie del estudiante: ",estudiante1_hobbie)
        print("")
        print("Nombre del candidato: ",estudiante2_nombre)
        print("Fecha de nacimiento del candidato: ",estudiante2_fec)
        print("Edad del candidato: ", calcularedad(estudiante2_fec))
        print("Biografia del estudiante: ",estudiante2_bio)
        print("Hobbie del estudiante: ",estudiante2_hobbie)
        print("")
        print("Nombre del candidato: ",estudiante4_nombre)
        print("Fecha de nacimiento del candidato: ",estudiante4_fec)
        print("Edad del candidato: ", calcularedad(estudiante4_fec))
        print("Biografia del estudiante: ",estudiante4_bio)
        print("Hobbie del estudiante: ",estudiante4_hobbie)
        print("")

    else:
        print("Candidatos: ")
        print("Nombre del candidato: ",estudiante1_nombre)
        print("Fecha de nacimiento del candidato: ",estudiante1_fec)
        print("Edad del candidato: ", calcularedad(estudiante1_fec))
        print("Biografia del estudiante: ",estudiante1_bio)
        print("Hobbie del estudiante: ",estudiante1_hobbie)
        print("")
        print("Nombre del candidato: ",estudiante2_nombre)
        print("Fecha de nacimiento del candidato: ",estudiante2_fec)
        print("Edad del candidato: ", calcularedad(estudiante2_fec))
        print("Biografia del estudiante: ",estudiante2_bio)
        print("Hobbie del estudiante: ",estudiante2_hobbie)
        print("")
        print("Nombre del candidato: ",estudiante3_nombre)
        print("Fecha de nacimiento del candidato: ",estudiante3_fec)
        print("Edad del candidato: ", calcularedad(estudiante3_fec))
        print("Biografia del estudiante: ",estudiante3_bio)
        print("Hobbie del estudiante: ",estudiante3_hobbie)
        print("")

def calcularedad(fechadenacimiento):
    fechadenacimiento=datetime.strptime(fechadenacimiento,'%Y-%m-%d')
    hoy=datetime.now()
    edad=hoy.year-fechadenacimiento.year
    if (hoy.month,hoy.day) < (fechadenacimiento.month, fechadenacimiento.day):
        edad = edad-1
    return edad

def menuvercandidatos():
    if correo == estudiante1_email:
        yo_candidato=estudiante1_nombre
    elif correo == estudiante2_email:
        yo_candidato=estudiante2_nombre
    elif correo == estudiante3_email:
        yo_candidato=estudiante3_nombre
    else:
        yo_candidato=estudiante4_nombre
    limpiar_pantalla()
    vercandidatos()
    mgestudiante=input("Ingrese el nombre del estudiante que le gusta: ")
    while mgestudiante != estudiante1_nombre and mgestudiante != estudiante2_nombre and mgestudiante != estudiante3_nombre and mgestudiante != estudiante4_nombre or mgestudiante == yo_candidato:
        print("Ingreso el nombre de forma incorrecta o se elijio a usted mismo.")
        sleep(5)
        limpiar_pantalla()
        vercandidatos()
        mgestudiante=input("Ingrese el nombre del estudiante que le gusta: ")

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
            case "b":
                print("En construccion...")
            case "x":
                menu_ruleta()
            case _:
                print("Ingrese una opcion correctamente.")
                sleep(5)
        limpiar_pantalla()
        menu_print_matcheos()
        opcion = input("Ingrese una opcion: ")

def ruleta_instrucciones():
    print("La Ruleta de afinidad es una forma de seleccionar tu matcheo")
    print("usando tu afinidad con tres personas!")
    print("Puedes elegir ser matcheado automaticamente o solo mostrar el nombre")
    print("(necesitaras el nombre exacto para hacerlo automaticamente asi que seria buena idea ir a [Gestion de candidatos])")
    print(" 1. Ruleta")
    print(" 0. Salir")

def menu_ruleta():
    opcion_ruleta = 1
    while opcion_ruleta != 0:
        limpiar_pantalla()
        ruleta_instrucciones()
        seleccion_numerica = input("Ingrese su opcion: ")
        while not seleccion_numerica.isnumeric() or int(seleccion_numerica)>1 or int(seleccion_numerica)<0 :
            print("Ingreso incorrectamente.")
            sleep(5)
            seleccion_numerica = input("Ingrese su opcion: ")
        opcion_ruleta = int(seleccion_numerica)
        match opcion_ruleta:
            case 1:
                ruleta()

        


def ruleta():
    numran = random.randint(0, 100)
    if correo == estudiante1_email:
        yo_candidato=estudiante1_nombre
    elif correo == estudiante2_email:
        yo_candidato=estudiante2_nombre
    elif correo == estudiante3_email:
        yo_candidato=estudiante3_nombre
    else:
        yo_candidato=estudiante4_nombre
    nombre_A = input("Nombre #1: ")
    while nombre_A != estudiante1_nombre and nombre_A != estudiante2_nombre and nombre_A != estudiante3_nombre and nombre_A != estudiante4_nombre or nombre_A == yo_candidato:
        print("Ingrese correctamente el nombre o no puede ser usted mismo")
        nombre_A = input("Nombre #1: ")
    nombre_B = input("Nombre #2: ")
    while nombre_B != estudiante1_nombre and nombre_B != estudiante2_nombre and nombre_B != estudiante3_nombre and nombre_B != estudiante4_nombre or nombre_B == yo_candidato or nombre_B == nombre_A:
        print("Ingrese correctamente el nombre o no puede ser usted mismo")
        nombre_B = input("Nombre #2: ")
    nombre_C = input("Nombre #3: ")
    while nombre_C != estudiante1_nombre and nombre_C != estudiante2_nombre and nombre_C != estudiante3_nombre and nombre_C != estudiante4_nombre or nombre_C == yo_candidato or nombre_C == nombre_B or nombre_C == nombre_A:
        print("Ingrese correctamente el nombre o no puede ser usted mismo")
        nombre_C = input("Nombre #3: ")
    print("Ahora asignamos nuestra afinidad con ellos")
    print("Solo tienes 100 puntos de afinidad para distribuir")
    probabilidad_A = int(input("Afinidad con " + nombre_A + ": "))
    probabilidad_B = int(input("Afinidad con " + nombre_B + ": "))
    probabilidad_C = int(input("Afinidad con " + nombre_C + ": "))
    while probabilidad_A + probabilidad_B + probabilidad_C != 100:
        print("La afinidad no puede ser mayor a 100")
        print(probabilidad_A + probabilidad_B + probabilidad_C, "?")
        probabilidad_A = int(input("Afinidad con " + nombre_A + ": "))
        probabilidad_B = int(input("Afinidad con " + nombre_B + ": "))
        probabilidad_C = int(input("Afinidad con " + nombre_C + ": "))
    
    print(f"Se tiro un dado de {numran} , {probabilidad_C} es el sobrante")
    sleep(2)
    limpiar_pantalla()
    if numran < probabilidad_A:
        print("Hiciste match con: ",nombre_A)
    elif numran >= probabilidad_A and numran < probabilidad_B + probabilidad_A:
        print("Hiciste match con: ",nombre_B)
    else:
        print("Hiciste match con: ",nombre_C)

# ##Programa## #
login()
if inicio:
    opc_principal = 5
    while opc_principal != 0:
        limpiar_pantalla()
        menu_principal()
        seleccion_numerica = input("Ingrese su seleccion: ")
        while not seleccion_numerica.isnumeric() or int(seleccion_numerica)>4 or int(seleccion_numerica)<0 :
            print("Ingreso incorrectamente.")
            seleccion_numerica = input("Ingrese su seleccion: ")
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
