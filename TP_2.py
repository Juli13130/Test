# Para ocultar los caracteres
import getpass
# Para limpiar la consola
import os
from re import A
# Para usar delay
from time import sleep
# Para ruleta
import random
# Para calcular la edad
from datetime import datetime

def inicializar_arrays(filas,columnas):
    columnas=columnas+1
    array = [ [0] * columnas for i in range(filas)]
    return array
    
#c = 4
#r = 3
#Array = [ [0] * c for i in range(r) ]



def limpiar_pantalla():
    os.system('cls')

def print_menu_inicio():
    print("0. Salir")
    print("1. Login")
    print("2. Registrarse")

def validar(var,min,max):
    var=int(var)
    while var<min or var >max:
        print("Opcion incorrecta.")
        var=input("Ingrese la opcion correctamente: ")
    return var
    
def print_tipos_usuarios():
    print("Los tipos de usuarios son: ")
    print("1. Estudiantes")
    print("2. Moderadores")

def check():
    
    contador_estudiantes=0
    contador_moderadores=0
    for i in range(8):
        if estudiantes[i][0] != 0:
            contador_estudiantes=contador_estudiantes+1
    for i in range(4):
        if moderadores[i][0] != 0:
            contador_moderadores=contador_moderadores+1
    if contador_estudiantes >= 4 and contador_moderadores >= 1:
        return True
    else:
        return False
    
# lista[columna][fila]
def login_estudiantes():
    global pos_estudiante
    intentos=0
    acceso="Denegado"
    while intentos < 3 :
        i=0
        email = input("Ingrese mail del estudiante: ")
        contrasenia = getpass.getpass("Ingrese la contrasenia: ")
        while estudiantes[i][0] != email and i<7:
            i=i+1
        estado = estudiantes[i][2]
        if email == estudiantes[i][0] and contrasenia == estudiantes[i][1]:
            intentos=4
            acceso="Estudiante"
            pos_estudiante=i
        else:
            intentos=intentos+1
            print("Quedan ",3-intentos," intentos")
    if acceso == "Estudiante" and estado != "ACTIVO":
        acceso="Denegado"
        print("Su cuenta se encuentra INACTIVA")
    return acceso
    

def login_moderadores():
    global pos_moderador
    intentos=0
    acceso="Denegado"
    while intentos < 3:
        i=0
        email = input("Ingrese mail del moderador: ")
        contrasenia = getpass.getpass("Ingrese la contrasenia: ")
        while moderadores[i][0] != email and i<3:
            i=i+1
        if email == moderadores[i][0] and contrasenia == moderadores[i][1]:
            intentos=4
            pos_moderador=i
            acceso="Moderador"
        else:
            intentos=intentos+1
            print("Quedan ",3-intentos," intentos")
    return acceso

def menu_principal_estudiantes():
    print("1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadisticos")
    print("0. Salir")

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
    
def menu_print_gestion_perfil():
    print("1. Gestionar mi perfil")
    print(" a. Editar mis datos personales")
    print(" b. Eliminar mi perfil")
    print(" c. Volver")
    
def menu_editar_datos_personales():
    global pos_estudiante
    # Asigno los datos del estudiante a las variables auxiliares.
    fec = estudiantes[pos_estudiante][4]
    bio = estudiantes[pos_estudiante][5]
    hobbie = estudiantes[pos_estudiante][6]
    opcion = 0
    while opcion != 4:
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
                fec = datetime.strptime(fec, '%Y-%m-%d').date()
                hoy = datetime.now()
                while (hoy.year < fec.year) or (hoy.year - fec.year) > 150:
                    print("El anio no puede ser posterior al actual o anterior a 150 anios")
                    fec = input("Ingrese la nueva fecha de nacimiento en formato YYYY-MM-DD : ")
                    fec = datetime.strptime(fec, '%Y-%m-%d').date()
                while (hoy.year == fec.year) and (hoy.month < fec.month):
                    print("El mes no puede ser posterior al actual")
                    fec = input("Ingrese la nueva fecha de nacimiento en formato YYYY-MM-DD : ")
                    fec = datetime.strptime(fec, '%Y-%m-%d').date()
                while (hoy.year == fec.year and hoy.month == fec.month and hoy.day < fec.day):
                    print("El dia no puede ser posterior al actual")
                    fec = input("Ingrese la nueva fecha de nacimiento en formato YYYY-MM-DD : ")
                    fec = datetime.strptime(fec, '%Y-%m-%d').date()
            case 2:
                bio = input("Ingrese la nueva biografia: ")
            case 3:
                hobbie = input("Ingrese el nuevo hobbie: ")
    # Asigno el valor de las variables auxiliares al estudiante
    estudiantes[pos_estudiante][4] = fec
    estudiantes[pos_estudiante][5] = bio
    estudiantes[pos_estudiante][6] = hobbie


def menu_print_gestion_candidatos():
    print("2. Gestionar candidatos")
    print(" a. Ver candidatos")
    print(" b. Reportar un candidato")
    print(" c. Volver")


'''
opcion : integer
'''


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


'''
seleccion_numerica : string
opcion_ruleta : integer
'''


def menu_ruleta():
    opcion_ruleta = 1
    while opcion_ruleta != 0:
        limpiar_pantalla()
        ruleta_instrucciones()
        seleccion_numerica = input("Ingrese su opcion: ")
        while not seleccion_numerica.isnumeric() or int(seleccion_numerica) > 1 or int(seleccion_numerica) < 0:
            print("Ingreso incorrectamente.")
            sleep(5)
            seleccion_numerica = input("Ingrese su opcion: ")
        opcion_ruleta = int(seleccion_numerica)
        match opcion_ruleta:
            case 1:
                ruleta()


'''
yo_candidato, nombre_* estudiante*_nombre : string
numran, probabilidad_* : integer
'''


def ruleta():
    global pos_estudiante
    limpiar_pantalla()
    numran = random.randint(0, 100)
    yo_candidato = estudiantes[pos_estudiante][4]
    i=0
    print("Los candidatos a elegir son los siguientes: ")
    while i<7:
        if i != pos_estudiante:
            print("Candidato: ",estudiantes[i][4], "posicion ",i)
        i=i+1
    
    a=input("Ingrese la posicion del candidato 1: ")
    a=validar(a,0,7)
    while estudiantes[pos_estudiante][4] == estudiantes[a][4]:
        print("No te podes elegir a vos mismo..")
        a=input("Ingrese la posicion del candidato 1: ")
        a=validar(a,0,7)
    
    b=input("Ingrese la posicion del candidato 2: ")
    b=validar(b,0,7)
    while estudiantes[pos_estudiante][4] == estudiantes[b][4] or estudiantes[b][4]==estudiantes[a][4]:
        print("No te podes elegir a vos mismo o elegir un candidato ya elegido..")
        b=input("Ingrese la posicion del candidato 2: ")
        b=validar(b,0,7)
    c=input("Ingrese la posicion del candidato 3: ")
    c=validar(c,0,7)
    while estudiantes[pos_estudiante][4] == estudiantes[b][4] or estudiantes[c][4]==estudiantes[a][4] or estudiantes[c][4]==estudiantes[b][4]:
        print("No te podes elegir a vos mismo o elegir un candidato ya elegido..")
        b=input("Ingrese la posicion del candidato 3: ")
        c=validar(c,0,7)
    
    nombre_A=estudiantes[a][4]
    nombre_B=estudiantes[b][4]
    nombre_C=estudiantes[c][4]


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
        print("Hiciste match con: ", nombre_A)
    elif numran >= probabilidad_A and numran < probabilidad_B + probabilidad_A:
        print("Hiciste match con: ", nombre_B)
    else:
        print("Hiciste match con: ", nombre_C)
    sleep(5)

def menu_opc_reportes():
    print("Soy el menu de reportes")

def menu_estudiantes():
    opc_principal = 5
    while opc_principal != 0:
        limpiar_pantalla()
        menu_principal_estudiantes()
        seleccion_numerica = input("Ingrese su seleccion: ")
        while not seleccion_numerica.isnumeric() or int(seleccion_numerica) > 4 or int(seleccion_numerica) < 0:
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
                menu_opc_reportes()
                sleep(5)
        limpiar_pantalla()
    
def menu_principal_moderadores():
    print("1. Gestionar usuarios")
    print("   a. Desactivar usuarios")
    print("   b. Volver")
    print("2. Gestionar reportes")
    print("   a. Ver reportes")
    print("   b. Volver")
    print("0. Salir")

def menu_moderadores():
    opc_principal = 5
    while opc_principal != 0:
        limpiar_pantalla()
        menu_principal_moderadores()
        seleccion_numerica = input("Ingrese su seleccion: ")
        while not seleccion_numerica.isnumeric() or int(seleccion_numerica) > 4 or int(seleccion_numerica) < 0:
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
                menu_opc_reportes()
                sleep(5)
        limpiar_pantalla()

def registrar():
    print("Menu de registro")
    print("0. Salir")
    print("1. Registro de usuarios")
    print("2. Registro de moderadores")
    opc=input("Ingrese opcion: ")
    opc=validar(opc,0,2)
    while opc != 0:
        i=0
        contador_estudiantes=0
        contador_moderadores=0
        for i in range(8):
            if estudiantes[i][0] != 0:
                contador_estudiantes=contador_estudiantes+1
        for i in range(4):
            if moderadores[i][0] != 0:
                contador_moderadores=contador_moderadores+1
        if opc==1:
            aux=0
            print("Hay ",contador_estudiantes," estudiantes registrados")
            print("Quedan ",8-contador_estudiantes," lugares disponibles")
            while aux == 0 and contador_estudiantes < 8:
                email=input("Ingrese email del usuario: ")
                contrasenia=input("Ingrese contrasenia del usuario: ")
                print("Estado del usuario: ")
                print("1. Activo")
                print("2. Inactivo")
                estado=input("Ingrese estado del usuario: ")
                estado=validar(estado,1,2)
                if estado==1:
                    estado="ACTIVO"
                else:
                    estado="INACTIVO"
                estudiantes[contador_estudiantes][0]=email
                estudiantes[contador_estudiantes][1]=contrasenia
                estudiantes[contador_estudiantes][2]=estado
                contador_estudiantes=contador_estudiantes+1
                aux=input("Ingrese 0 para seguir: ")
                aux=int(aux)
        elif opc==2:
            aux=0
            print("Hay ",contador_moderadores," moderadores registrados")
            print("Quedan ", 4-contador_moderadores," lugares disponibles")
            while aux == 0 and contador_moderadores < 4:
                email=input("Ingrese email del moderador: ")
                contrasenia=input("Ingrese contrasenia del moderador: ")
            
                moderadores[contador_moderadores][0]=email
                moderadores[contador_moderadores][1]=contrasenia
                contador_moderadores=contador_moderadores+1
            
                aux=input("Ingrese 0 para seguir: ")
        limpiar_pantalla()
        print("Menu de registro")
        print("0. Salir")
        print("1. Registro de usuarios")
        print("2. Registro de moderadores")
        opc=input("Ingrese opcion: ")
        opc=validar(opc,0,2)
    limpiar_pantalla()
            
def menu_print_matcheos():
    print("3. Matcheos")
    print(" a. Ver matcheos")
    print(" b. Eliminar un matcheo")
    print(" c. Volver")
    print(" x. Ruleta de afinidad")
  
def calcularedad(fechadenacimiento):
    if fechadenacimiento != 0:
        fechadenacimiento = datetime.strptime(fechadenacimiento, '%Y-%m-%d')
        hoy = datetime.now()
        edad = hoy.year-fechadenacimiento.year
        if (hoy.month, hoy.day) < (fechadenacimiento.month, fechadenacimiento.day):
            edad = edad-1
    else:
        edad=0    
    return edad

def menuvercandidatos():
    
    global pos_estudiante
    yo_candidato = estudiantes[pos_estudiante][4]
    limpiar_pantalla()
    i=0
    print("Datos de candidatos: ")
    while i<7:
        if i != pos_estudiante:
            print("--------------------------------------")
            print("Nombre: ",estudiantes[i][3])
            print("Fecha de nacimiento ",estudiantes[i][4])
            print("Edad: ",calcularedad(estudiantes[i][4]))
            print("Bio: ",estudiantes[i][5])
            print("Hobbie: ",estudiantes[i][6])
            print("Posicion del estudiante: ",i)
            print("--------------------------------------")
        i=i+1
    mgestudiante = input("Ingrese la posicion del estudiante que le gusta: ")
    mgestudiante = validar(mgestudiante,0,7)
    
    #while mgestudiante != estudiante1_nombre and mgestudiante != estudiante2_nombre and mgestudiante != estudiante3_nombre and mgestudiante != estudiante4_nombre or mgestudiante == yo_candidato:
     #   print("Ingreso el nombre de forma incorrecta o se elijio a usted mismo.")
      #  sleep(5)
       # limpiar_pantalla()
        #vercandidatos()
        #mgestudiante = input("Ingrese el nombre del estudiante que le gusta: ")

def login():
    if check() == True:
        
        print_tipos_usuarios()
        tipo_usuario=input("Ingrese tipo de usuario para login: ")
        tipo_usuario=validar(tipo_usuario,1,2)
        
        if tipo_usuario == 1:
            estado_login=login_estudiantes()
        else:
            estado_login=login_moderadores()    

        if estado_login == "Estudiante":
            menu_estudiantes()
        elif estado_login == "Moderador":
            menu_moderadores()
        else:
            print("Acceso denegado")
    else:
        print("No se puede iniciar porque no hay 1 moderador y 4 estudiantes registrados.")
        sleep(5)
        limpiar_pantalla()

      


#   0. Salir
#   1. Login
#   2. Registrarse

estudiantes=inicializar_arrays(8,6)
moderadores=inicializar_arrays(4,2)

print_menu_inicio()
opc=input("Ingrese opcion: ")
opc=validar(opc,0,2)

while opc != 0:
    
    if opc == 1:
        login()
        
    else:
        registrar()
    
    print_menu_inicio()
    opc=input("Ingrese opcion: ")
    opc=validar(opc,0,2) 



