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

def inicializar_arrays(filas,columnas):
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
    i=0
    email = input("Ingrese mail del estudiante: ")
    contrasenia = getpass.getpass("Ingrese la contrasenia: ")
    while estudiantes[i][0] != email and i<7:
        i=i+1
    estado = estudiantes[i][2]
    print(estudiantes[i][0])
    if email == estudiantes[i][0] and contrasenia == estudiantes[i][1] and estado == "ACTIVO":
        return "Estudiante"
    else:
        return "Denegado"

def login_moderadores():
    i=0
    email = input("Ingrese mail del moderador: ")
    contrasenia = getpass.getpass("Ingrese la contrasenia: ")
    while moderadores[i][0] != email and i<3:
        i=i+1
    if email == moderadores[i][0] and contrasenia == moderadores[i][1]:
        return "Moderador"
    else:
        return "Denegado"

def menu_estudiantes():
    print("Soy estudiante")
    
def menu_moderadores():
    print("Soy moderador")

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

      


#   0. Salir
#   1. Login
#   2. Registrarse

estudiantes=inicializar_arrays(8,3)
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



