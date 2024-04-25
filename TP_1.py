import getpass
# Base de datos de usuarios (correo y contraseña)
usuarios = {
    "estudiante1@ayed.com": "111222",
    "estudiante2@ayed.com": "333444",
    "estudiante3@ayed.com": "555666",
}


def login():
    intentos= 3
    while intentos > 0 :
        correo= input ("Ingrese su correo electronico: ")
        if correo in usuarios:
            contraseña= getpass.getpass("Ingrese la contraseña: ")
            if contraseña== usuarios[correo]:
                print ("Inicio de sesion correcto.")
                return
            else:
                intentos -=1
                if intentos> 0:
                    print("Inicio de sesion incorrecto.","intente nuevamente")
                else:
                    print("Ha agotado todos los intentos disponibles. Fin del Inicio de Sesion.")
                    return
        else:
            intentos -=1
            if intentos > 0:
                print("Correo electronico incorrecto. Ingrese nuevamente su correo:")
            else:
                print("Ha intentado el maximo de intentos permitidos. Fin del Inicio de Sesion")
                return
            
login()

