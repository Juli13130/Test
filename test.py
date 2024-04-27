import getpass
sesion_iniciada = False
usuarios = {
    "estudiante1@ayed.com": "111222",
    "estudiante2@ayed.com": "333444",
    "estudiante3@ayed.com": "555666",
}

def menu_inicio():
    print(" ")  #espacio para que el "menu" sea mas obvio
    print("0-Registrarse")
    print("1-Iniciar sesion")
    print("3-Salir")
    seleccion_inicio = input("seleccionar: >")

    if seleccion_inicio == "0":
        print("registro")
    elif seleccion_inicio == "1":
        login()
    else:
        exit("Saliendo...")
def registro():
    print("aaa")  
def login():
    intentos= 3
    while intentos > 0 :
        correo= input ("Ingrese su correo electronico: ")
        if correo in usuarios:
            contraseña= getpass.getpass("Ingrese la contraseña: ")
            if contraseña== usuarios[correo]:
                print ("Inicio de sesion correcto.")
                sesion_iniciada = True
                return
            else:
                intentos -=1
                if intentos> 0:
                    print("Inicio de sesion incorrecto.","intente nuevamente")
                else:
                    print("Ha agotado todos los intentos disponibles. Fin del Inicio de Sesion.")
                    menu_inicio()
        else:
            intentos -=1
            if intentos > 0:
                print("Correo electronico incorrecto. Ingrese nuevamente su correo:")
            else:
                print("Ha intentado el maximo de intentos permitidos. Fin del Inicio de Sesion")
                menu_inicio()

while sesion_iniciada is False:
    menu_inicio()
def menu_principal():
    print(" ")
    print("0-Salir")
    print("1-Gestionar mi perfil")
    print("2-Gestionar candidatos")
    print("3-Matcheos")
    print("4-Reportes estadisticos")
menu_principal()