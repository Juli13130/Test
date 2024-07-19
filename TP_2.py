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
from turtle import pos
from zoneinfo import InvalidTZPathWarning

def inicializar_arrays(filas,columnas):
    array = [ [0] * columnas for i in range(filas)]
    i=0
    #Columna ID
    for i in range (filas):
        array[i][0]=i
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
        var=int(input("Ingrese la opcion correctamente: "))
    return var
    
def print_tipos_usuarios():
    print("Los tipos de usuarios son: ")
    print("1. Estudiantes")
    print("2. Moderadores")

def check():
    
    contador_estudiantes=0
    contador_moderadores=0
    for i in range(8):
        if estudiantes[i][1] != 0:
            contador_estudiantes=contador_estudiantes+1
    for i in range(4):
        if moderadores[i][1] != 0:
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
        while estudiantes[i][1] != email and i<7:
            i=i+1
        estado = estudiantes[i][3]
        if email == estudiantes[i][1] and contrasenia == estudiantes[i][2]:
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
        while moderadores[i][1] != email and i<3:
            i=i+1
        if email == moderadores[i][1] and contrasenia == moderadores[i][2]:
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

def menu_editar_datos_personales():
    global pos_estudiante
    # Asigno los datos del estudiante a las variables auxiliares.
    fec = estudiantes[pos_estudiante][5]
    bio = estudiantes[pos_estudiante][6]
    hobbie = estudiantes[pos_estudiante][7]
    opcion = 0
    while opcion != 4:
        print("Sus datos actuales son: ")
        print("Su fecha de nacimiento es: ", fec)
        print("Su biografia es: ", bio)
        print("Su hobbie es: ", hobbie)
        print("Que dato desea cambiar?")
        print("1. Fecha de nacimiento")
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
    estudiantes[pos_estudiante][5] = fec
    estudiantes[pos_estudiante][6] = bio
    estudiantes[pos_estudiante][7] = hobbie

def menu_print_gestion_perfil():
    print("1. Gestionar mi perfil")
    print(" a. Editar mis datos personales")
    print(" b. Eliminar mi perfil")
    print(" c. Volver")

def menu_eliminar_perfil(pos):
    
    limpiar_pantalla()
    print("Confirmar eliminacion de perfil")
    print("0. Si")
    print("1. No")
    opc=input("Ingrese una opcion: ")
    opc=validar(opc,0,1)
    match opc:
        case 0:
            estudiantes[pos][3]="INACTIVO"
        case 1:
            print("")
        case _:
            print("Ingrese una opcion correctamente")      

def menu_opc_gestion_perfil():
    global pos_estudiante
    limpiar_pantalla()
    menu_print_gestion_perfil()
    opcion = input("Ingrese una opcion: ")
    while opcion != "c":
        while estudiantes[pos_estudiante][3]=="ACTIVO":
            match opcion:
                case "a":
                    menu_editar_datos_personales()
                case "b":
                    menu_eliminar_perfil(pos_estudiante)
                case _:
                    print("Ingrese la opcion correctamente")
                    sleep(5)   
            limpiar_pantalla()
            if estudiantes[pos_estudiante][3]=="ACTIVO":
                menu_print_gestion_perfil()
                opcion = input("Ingrese una opcion: ")
            else:
                opcion="c"
        
def menu_print_gestion_candidatos():
    print("2. Gestionar candidatos")
    print(" a. Ver candidatos")
    print(" b. Reportar un candidato")
    print(" c. Volver")

def menu_ver_candidatos():
    
    global pos_estudiante
    yo_candidato = estudiantes[pos_estudiante][4]
    limpiar_pantalla()
    i=0
    print("Datos de candidatos: ")
    while i<7:
        if i != pos_estudiante and estudiantes[i][3]=="ACTIVO":
            print("--------------------------------------")
            print("Nombre: ",estudiantes[i][4])
            print("Fecha de nacimiento ",estudiantes[i][5])
            print("Edad: ",calcularedad(estudiantes[i][5]))
            print("Bio: ",estudiantes[i][6])
            print("Hobbie: ",estudiantes[i][7])
            print("ID del estudiante: ",i)
            print("--------------------------------------")
        i=i+1
    mgestudiante = input("Ingrese el nombre del estudiante que le gusta: ")
    i=0
    mgestudiante_pos=0
    while mgestudiante != estudiantes[mgestudiante_pos][4]:
        while i < 7:
            if estudiantes[i][4] == mgestudiante:
                mgestudiante_pos=i
                i=7
            else:
                i=i+1
        if i >= 7 and mgestudiante != estudiantes[mgestudiante_pos][4]:
            print("No se encontro al estudiante.")
            print("Verifique que lo escribio correctamente.")
            sleep(2)
            mgestudiante = input("Ingrese el nombre del estudiante que le gusta: ")
            i=0
            
            
    if estudiantes[mgestudiante_pos][4] == yo_candidato:
            print("No se puede elegir a usted mismo.")
            sleep(5)
            limpiar_pantalla()        
    else:
        print("Se dio like al estudiante: ",estudiantes[mgestudiante_pos][4])
        estudiantes_likes[pos_estudiante][mgestudiante_pos]=1
        sleep(5)
        limpiar_pantalla()
        
    #while mgestudiante != estudiante1_nombre and mgestudiante != estudiante2_nombre and mgestudiante != estudiante3_nombre and mgestudiante != estudiante4_nombre or mgestudiante == yo_candidato:
     #   print("Ingreso el nombre de forma incorrecta o se elijio a usted mismo.")
      #  sleep(5)
       # limpiar_pantalla()
        #vercandidatos()
        #mgestudiante = input("Ingrese el nombre del estudiante que le gusta: ")

def contador_reportes():
    contador_reportes=0
    for i in range(56):
        if reportes[i][3] != 0:
            contador_reportes=contador_reportes+1
    return contador_reportes

def menu_reportar_candidato():
    pos_reportado=0
    i=0
    reportante=estudiantes[pos_estudiante][4]
    print("Usuarios y ID: ")
    while i<7:
        if i != pos_estudiante and estudiantes[i][3]=="ACTIVO":
            print("--------------------------------------")
            print("Nombre: ",estudiantes[i][4])
            print("ID del estudiante: ",i)
            print("--------------------------------------")
        i=i+1
    print("Reportar por: ")
    print("0. ID")
    print("1. Usuario")
    opc=int(input("Ingrese opcion: "))
    opc=validar(opc,0,1)
    if opc == 0:
        reportado=int(input("Ingrese ID del usuario a reportar: "))
        reportado=validar(reportado,0,7)
        while reportado == pos_estudiante:
            print("No se puede reportar a usted mismo")
            reportado=int(input("Ingrese ID del usuario a reportar: "))
            reportado=validar(reportado,0,7)
        pos_reportado=reportado
    else:

        reportado=input("Ingrese nombre del usuario a reportar: ")
        i=0
        pos_reportado=0
        
        while reportado == estudiantes[pos_estudiante][4]:
            print("No se puede elegir a usted mismo.")
            reportado=input("Ingrese nombre del usuario a reportar: ")
        while reportado != estudiantes[pos_reportado][4]:
            while i<7:
                if estudiantes[i][4] == reportado:
                    pos_reportado=i
                    i=7
                else:
                    i=i+1
            if i >= 7 and reportado != estudiantes[pos_reportado][4]:
                print("No se encontro el nombre.")
                reportado=input("Ingrese nombre del usuario a reportar: ")
                i=0
    print("Armado de reporte: ")
    motivo=input("Ingrese motivo del reporte: ")
    estado=0
    id_reporte=contador_reportes()
    reportes[id_reporte][1]=estudiantes[pos_estudiante][0]
    reportes[id_reporte][2]=estudiantes[pos_reportado][0]
    reportes[id_reporte][3]=motivo
    reportes[id_reporte][4]=estado

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
                menu_ver_candidatos()
            case "b":
                menu_reportar_candidato()
            case _:
                print("Ingrese la opcion correctamente")
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
                print("En construccion...")
            case "b":
                print("En construccion...")
            #case "x":
                #menu_ruleta()
            case _:
                print("Ingrese una opcion correctamente.")
        sleep(5)
        limpiar_pantalla()
        menu_print_matcheos()
        opcion = input("Ingrese una opcion: ")

def menu_opc_reportes():
    
    global pos_estudiante
    
    col=0
    contador_match=0
    contador_likes_dados=0
    contador_likes_recibidos=0
    
    while col <= 7:
        if col != pos_estudiante:
            if estudiantes_likes[col][pos_estudiante] == 1:
                if estudiantes_likes[col][pos_estudiante] == estudiantes_likes[pos_estudiante][col]:
                    contador_match = contador_match+1
                else:
                    #contador_likes_dados=contador_likes_dados+1
                    contador_likes_recibidos=contador_likes_recibidos+1
            else:
                if estudiantes_likes[col][pos_estudiante] != estudiantes_likes[pos_estudiante][col]:
                    #contador_likes_recibidos=contador_likes_recibidos+1
                    contador_likes_dados=contador_likes_dados+1
        col=col+1
    
    #Parece que contador_likes_dados
    #Y contador_likes_recibidos estan al reves
    #No estoy entendiendo como funcionan los arreglos?    

    print("Matcheados sobre el % posible: ", ((contador_match/7)*100), "%")
    print("Likes dados y no recibidos: ", contador_likes_dados)
    print("Likes recibidos y no respondidos: ",contador_likes_recibidos)
    sleep(5)
    limpiar_pantalla()   

def menu_estudiantes():
    opc_principal = 5
    while opc_principal != 0 and estudiantes[pos_estudiante][3]=="ACTIVO":
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
        limpiar_pantalla()
        sleep(5)
    
def menu_principal_moderadores():
    print("1. Gestionar usuarios")
    print("   a. Desactivar usuarios")
    print("   b. Volver")
    print("2. Gestionar reportes")
    print("   a. Ver reportes")
    print("   b. Volver")
    print("3. Reportes estadisticos")
    print("4. Bonus track 1")
    print("5. Bonus track 2")
    print("0. Salir")

def menu_print_gestion_usuarios():
    print("a. Desactivar usuario")
    print("b. Volver")

def menu_gestion_usuarios():
    pos_eliminado=0
    print("Eliminar por: ")
    print("0. ID")
    print("1. Usuario")
    opc=int(input("Ingrese opcion: "))
    opc=validar(opc,0,1)
    if opc == 0:
        id_eliminado=int(input("Ingrese ID del usuario a eliminar: "))
        id_eliminado=validar(id_eliminado,0,7)
        while estudiantes[id_eliminado][1] == 0:
            print("No se encuentra usuario.")
            id_eliminado=int(input("Ingrese ID del usuario a eliminar: "))
            id_eliminado=validar(id_eliminado,0,7)
        pos_eliminado=id_eliminado
    else:
        nombre_eliminado=input("Ingrese nombre del usuario a eliminar: ")
        i=0
        pos_eliminado=0
        while nombre_eliminado != estudiantes[pos_eliminado][4]:
            while i<7:
                if estudiantes[i][4] == nombre_eliminado:
                    pos_eliminado=i
                    i=7
                else:
                    i=i+1
            if i >= 7 and nombre_eliminado != estudiantes[pos_eliminado][4]:
                print("No se encontro el nombre.")
                nombre_eliminado=input("Ingrese nombre del usuario a eliminar: ")
                i=0
    menu_eliminar_perfil(pos_eliminado)
  
def menu_opc_gestion_usuarios():
    limpiar_pantalla()
    menu_print_gestion_usuarios()
    opcion = input("Ingrese una opcion: ")
    while opcion != "b":
        match opcion:
            case "a":
                menu_gestion_usuarios()
            case _:
                print("Ingrese la opcion correctamente")
                sleep(5)
        limpiar_pantalla()
        menu_print_gestion_usuarios()
        opcion = input("Ingrese una opcion: ")


def menu_print_gestion_reportes():
    print("a. Ver reportes")
    print("b. Volver")
    
def menu_gestion_reportes():
    i=0
    while i < 56:
        if reportes[i][3] !=0:
            id_reportante=reportes[i][1]
            id_reportado=reportes[i][2]
            motivo=reportes[i][3]
            estado=reportes[i][4]
            if estudiantes[id_reportante][3]=="ACTIVO" and estudiantes[id_reportado][3]=="ACTIVO" and estado == 0:
                print("Reporte numero: ",i)
                print("ID del reportante: ",id_reportante)
                print("ID del reportado: ",id_reportado)
                print("Motivo del reporte: ",motivo)
                print("Que desea hacer?: ")
                print("0. Ignorar reporte")
                print("1. Bloquear a reportado")
                opc=input("Ingrese opcion: ")
                opc=validar(opc,0,1)
                if opc == 0:
                    reportes[i][4]=2
                else:
                    estudiantes[id_reportado][3]="INACTIVO"
                    reportes[i][4]=1
        i=i+1

def menu_opc_gestion_reportes():
    limpiar_pantalla()
    menu_print_gestion_reportes()
    opcion = input("Ingrese una opcion: ")
    while opcion != "b":
        match opcion:
            case "a":
                menu_gestion_reportes()
            case _:
                print("Ingrese la opcion correctamente")
                sleep(5)
        limpiar_pantalla()
        menu_print_gestion_reportes()
        opcion = input("Ingrese una opcion: ")

def bonus_track_1():
    edades=[21,18,20,19,23,24]
    print("Dadas las edades: ",edades)
    i=0
    j=0
    aux=0
    max=edades[0]
    while i<5:
        j=i+1
        while j < 5:
            if edades[i] > edades[j]:
                aux=edades[j]
                edades[j]=edades[i]
                edades[i]=aux
            j=j+1
        i=i+1
    i=0
    contador_huecos=0
    while i<5:
        edad_1=int(edades[i])
        edad_2=(int(edades[i+1]))
        if (edad_2-edad_1) != 1:
            contador_huecos=contador_huecos+1
            print("Hay un hueco entre ", edad_1 ," y ", edad_2)
            print("El numero que falta es: ", edad_1+1)
        i=i+1
    print("Hay ",contador_huecos," huecos en total.")
    sleep(5)
            
def bonus_track_2():
    cantidad_estudiantes=contador_estudiante()
    print("Hay ",cantidad_estudiantes," estudiantes cargados")
    print("Por lo tanto hay ", (cantidad_estudiantes*(cantidad_estudiantes-1))," matcheos posibles")
    sleep(5)

def menu_moderadores():
    opc_principal = 5
    while opc_principal != 0:
        limpiar_pantalla()
        menu_principal_moderadores()
        seleccion_numerica = input("Ingrese su seleccion: ")
        while not seleccion_numerica.isnumeric() or int(seleccion_numerica) > 5 or int(seleccion_numerica) < 0:
            print("Ingreso incorrectamente.")
            seleccion_numerica = input("Ingrese su seleccion: ")
        opc_principal = int(seleccion_numerica)
        match opc_principal:
            case 1:
                menu_opc_gestion_usuarios()
            case 2:
                menu_opc_gestion_reportes()
            case 3:
                print("En construccion..")
            case 4:
                bonus_track_1()
            case 5:
                bonus_track_2()
        limpiar_pantalla()

def contador_estudiante():
    contador_estudiantes=0
    for i in range(8):  
        if estudiantes[i][1] != 0:  
             contador_estudiantes=contador_estudiantes+1
    return contador_estudiantes
    
def contador_moderador():
    contador_moderadores=0
    for i in range(4):
        if moderadores[i][1] != 0:
            contador_moderadores=contador_moderadores+1
    return contador_moderadores

def registrar():
    print("Menu de registro")
    print("0. Salir")
    print("1. Registro de usuarios")
    print("2. Registro de moderadores")
    opc=input("Ingrese opcion: ")
    opc=validar(opc,0,2)
    while opc != 0:
        i=0
        contador_estudiantes=contador_estudiante()
        contador_moderadores=contador_moderador()
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
                nombre=input("Ingrese nombre del usuario: ")
                
                estudiantes[contador_estudiantes][1]=email
                estudiantes[contador_estudiantes][2]=contrasenia
                estudiantes[contador_estudiantes][3]=estado
                estudiantes[contador_estudiantes][4]=nombre
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
            
                moderadores[contador_moderadores][1]=email
                moderadores[contador_moderadores][2]=contrasenia
                contador_moderadores=contador_moderadores+1
            
                aux=input("Ingrese 0 para seguir: ")
                aux=int(aux)
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
    #print(" x. Ruleta de afinidad")
  
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

def inicializar_likes(array):
    i=0
    for i in range (8):
        j=0
        for j in range (8):
            array[i][j]=numran = random.randint(0,1)
    return array

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

def testing():
    print("Usuarios de testing activados")
    sleep(5)
    limpiar_pantalla()
    
    estudiantes[0][1]="estudiante1"
    estudiantes[0][2]="estudiante1"
    estudiantes[0][3]="ACTIVO"
    estudiantes[0][4]="Nombre1"
    estudiantes[0][5]="1997-09-03"
    estudiantes[0][6]="Soy el primer estudiante"
    estudiantes[0][7]="Programar"

    estudiantes[1][1]="estudiante2"
    estudiantes[1][2]="estudiante2"
    estudiantes[1][3]="ACTIVO"
    estudiantes[1][4]="Nombre2"
    estudiantes[1][5]="1996-09-03"
    estudiantes[1][6]="Soy el segundo estudiante"
    estudiantes[1][7]="Jugar al counter"

    estudiantes[2][1]="estudiante3"
    estudiantes[2][2]="estudiante3"
    estudiantes[2][3]="ACTIVO"
    estudiantes[2][4]="Nombre3"
    estudiantes[2][5]="1995-09-03"
    estudiantes[2][6]="Soy el tercer estudiante"
    estudiantes[2][7]="Jugar futbol"

    estudiantes[3][1]="estudiante4"
    estudiantes[3][2]="estudiante4"
    estudiantes[3][3]="ACTIVO"
    estudiantes[3][4]="Nombre4"
    estudiantes[3][5]="1994-09-03"
    estudiantes[3][6]="Soy el cuarto estudiante"
    estudiantes[3][7]="Salir a bailar"

    moderadores[0][1]="mod1"
    moderadores[0][2]="mod1"

#   0. Salir
#   1. Login
#   2. Registrarse

estudiantes=inicializar_arrays(8,8)
moderadores=inicializar_arrays(4,3)
reportes=inicializar_arrays(56,5)
estudiantes_likes=inicializar_arrays(8,8)
estudiantes_likes=inicializar_likes(estudiantes_likes)

testing()



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


#Modulos anteriores sin usar
    
# def ruleta_instrucciones():
#     print("La Ruleta de afinidad es una forma de seleccionar tu matcheo")
#     print("usando tu afinidad con tres personas!")
#     print("Puedes elegir ser matcheado automaticamente o solo mostrar el nombre")
#     print("(necesitaras el nombre exacto para hacerlo automaticamente asi que seria buena idea ir a [Gestion de candidatos])")
#     print(" 1. Ruleta")
#     print(" 0. Salir")


'''
seleccion_numerica : string
opcion_ruleta : integer
'''


# def menu_ruleta():
#     opcion_ruleta = 1
#     while opcion_ruleta != 0:
#         limpiar_pantalla()
#         ruleta_instrucciones()
#         seleccion_numerica = input("Ingrese su opcion: ")
#         while not seleccion_numerica.isnumeric() or int(seleccion_numerica) > 1 or int(seleccion_numerica) < 0:
#             print("Ingreso incorrectamente.")
#             sleep(5)
#             seleccion_numerica = input("Ingrese su opcion: ")
#         opcion_ruleta = int(seleccion_numerica)
#         match opcion_ruleta:
#             case 1:
#                 ruleta()


'''
yo_candidato, nombre_* estudiante*_nombre : string
numran, probabilidad_* : integer
'''


# def ruleta():
#     global pos_estudiante
#     limpiar_pantalla()
#     numran = random.randint(0, 100)
#     yo_candidato = estudiantes[pos_estudiante][4]
#     i=0
#     print("Los candidatos a elegir son los siguientes: ")
#     while i<7:
#         if i != pos_estudiante:
#             print("Candidato: ",estudiantes[i][4], "posicion ",i)
#         i=i+1
    
#     a=input("Ingrese la posicion del candidato 1: ")
#     a=validar(a,0,7)
#     while estudiantes[pos_estudiante][4] == estudiantes[a][4]:
#         print("No te podes elegir a vos mismo..")
#         a=input("Ingrese la posicion del candidato 1: ")
#         a=validar(a,0,7)
    
#     b=input("Ingrese la posicion del candidato 2: ")
#     b=validar(b,0,7)
#     while estudiantes[pos_estudiante][4] == estudiantes[b][4] or estudiantes[b][4]==estudiantes[a][4]:
#         print("No te podes elegir a vos mismo o elegir un candidato ya elegido..")
#         b=input("Ingrese la posicion del candidato 2: ")
#         b=validar(b,0,7)
#     c=input("Ingrese la posicion del candidato 3: ")
#     c=validar(c,0,7)
#     while estudiantes[pos_estudiante][4] == estudiantes[b][4] or estudiantes[c][4]==estudiantes[a][4] or estudiantes[c][4]==estudiantes[b][4]:
#         print("No te podes elegir a vos mismo o elegir un candidato ya elegido..")
#         b=input("Ingrese la posicion del candidato 3: ")
#         c=validar(c,0,7)
    
#     nombre_A=estudiantes[a][4]
#     nombre_B=estudiantes[b][4]
#     nombre_C=estudiantes[c][4]


#     print("Ahora asignamos nuestra afinidad con ellos")
#     print("Solo tienes 100 puntos de afinidad para distribuir")
#     probabilidad_A = int(input("Afinidad con " + nombre_A + ": "))
#     probabilidad_B = int(input("Afinidad con " + nombre_B + ": "))
#     probabilidad_C = int(input("Afinidad con " + nombre_C + ": "))
#     while probabilidad_A + probabilidad_B + probabilidad_C != 100:
#         print("La afinidad no puede ser mayor a 100")
#         print(probabilidad_A + probabilidad_B + probabilidad_C, "?")
#         probabilidad_A = int(input("Afinidad con " + nombre_A + ": "))
#         probabilidad_B = int(input("Afinidad con " + nombre_B + ": "))
#         probabilidad_C = int(input("Afinidad con " + nombre_C + ": "))

#     print(f"Se tiro un dado de {numran} , {probabilidad_C} es el sobrante")
#     sleep(2)
#     limpiar_pantalla()
#     if numran < probabilidad_A:
#         print("Hiciste match con: ", nombre_A)
#     elif numran >= probabilidad_A and numran < probabilidad_B + probabilidad_A:
#         print("Hiciste match con: ", nombre_B)
#     else:
#         print("Hiciste match con: ", nombre_C)
#     sleep(5)    