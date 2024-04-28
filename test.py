import getpass
import sys  # parte de limpiar_consola(), se puede eliminar
loop = True  # esto no puede cambiar ya que es preferible salir mediante exit
sesion_iniciada = False
usuarios = {
    "estudiante1@ayed.com": "111222",
    "estudiante2@ayed.com": "333444",
    "estudiante3@ayed.com": "555666",
}


def menu_inicio():
    print(" ")  # espacio para que el "menu" sea mas obvio
    print("0-Registrarse")
    print("1-Iniciar sesion")
    print("2-Salir")
    seleccion_inicio = input("seleccionar: >")

    if seleccion_inicio == "0":
        registro()
    elif seleccion_inicio == "1":
        login()
    else:  # no estoy seguro si es preferible a un if ^ == 2
        exit("Saliendo...")


def registro():
    global sesion_iniciada
    print("codigo va aca")  # placeholder+truco para llegar al otro menu rapido
    sesion_iniciada = True


def login():
    intentos = 3
    while intentos > 0:
        correo = input("Ingrese su correo electronico: ")
        if correo in usuarios:
            contraseña = getpass.getpass("Ingrese la contraseña: ")
            if contraseña == usuarios[correo]:
                print("Inicio de sesion correcto.")
                global sesion_iniciada
                sesion_iniciada = True
            else:
                intentos -= 1
                if intentos > 0:
                    print("Inicio de sesion incorrecto.", "intente nuevamente")
                else:
                    print("Ha agotado todos los intentos disponibles. Fin del Inicio de Sesion.")  # el enunciado dice "si ingresa 3 incorrectas se cerrara el programa", aca puede haber un exit tranquilamente pero prefiero no volver a correr el .ṕy
        else:
            intentos -= 1
            if intentos > 0:
                print("Correo electronico incorrecto. Ingrese nuevamente su correo:")
            else:
                print("Ha intentado el maximo de intentos permitidos. Fin del Inicio de Sesion")  # lo mismo ^^^


def limpiar_consola(n=1):  # mas que nada para limpiar la consola de menus previos, se puede eliminar sin problemas
    for _ in range(n):
        sys.stdout.write("\x1b[1A")  # cursor up one line
        sys.stdout.write("\x1b[2K")  # delete the last line


def editor_datos():
    print("yay")  # placeholder


def menu_principal():
    global sesion_iniciada
    print(" ")
    print("0-Salir")
    print("1-Gestionar mi perfil")
    print("2-Gestionar candidatos")
    print("3-Matcheos")
    print("4-Reportes estadisticos")
    seleccion_pri = input("Selecionar: >")
    if seleccion_pri == "1":
        limpiar_consola(6)  # (6) lineas limpiadas
        print("--Gestionar mi perfil--")
        print("a-Editar mis datos personales")
        if input("sel: ").casefold() == "a":
            editor_datos()
        else:
            return
        # print("b-")
        # print("c-Salir")
    elif seleccion_pri == "2":
        limpiar_consola(6)
        print("--Gestionar candidatos--")
        print("a-Ver candidatos")
        # print("b-")
        # print("c-Salir")
    elif seleccion_pri == "3":
        limpiar_consola(6)
        print("--Matcheos--")
        print("a-Editar mis datos personales")
        print("b-")
        print("c-Salir")
    elif seleccion_pri == "4":
        print("en construccion")
    elif seleccion_pri == "0":
        limpiar_consola(6)
        print("0-Volver")
        print("1-Salir de la cuenta")
        print("~-Salir")
        salir = input("Estas seguro? ")
        if salir == "0":
            return
        elif salir == "1":
            sesion_iniciada = False
        else:
            exit
    else:
        print("?")  # me gustaria tener mensajes aleatorios aca, ya que no podemos tirarte de una sesion iniciada y no hay mucho que poner


while loop is True:  # mantiene al usuario en un menu u otro
    if sesion_iniciada is False:
        menu_inicio()
    if sesion_iniciada is True:
        menu_principal()
