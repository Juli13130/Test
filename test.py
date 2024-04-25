import getpass
sesion_iniciada = False
usuarios = {
    "estudiante1@ayed.com": "111222",
    "estudiante2@ayed.com": "333444",
    "estudiante3@ayed.com": "555666",
}

def menu_inicio()
    print(" ")
    print("0-Registrarse")
    print("1-Iniciar sesion")
    seleccion_inicio = input("seleccionar: >")

    if seleccion_inicio == "0" or "r":
        print("registro")
    elif seleccion_inicio == "1" or "i":
        login()
    else: print("?")

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

menu_inicio()

    