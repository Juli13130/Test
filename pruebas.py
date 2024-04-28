import sys
def delete_multiple_lines(n=1):
    """Delete the last line in the STDOUT."""
    for _ in range(n):
        sys.stdout.write("\x1b[1A")  # cursor up one line
        sys.stdout.write("\x1b[2K")  # delete the last line





def menu_principal():
    print(" ")
    print("0-Salir")
    print("1-Gestionar mi perfil")
    print("2-Gestionar candidatos")
    print("3-Matcheos")
    print("4-Reportes estadisticos")
    seleccion_pri = input("Selecionar: >")
    if seleccion_pri == "1":
        delete_multiple_lines(6)
        print("--1-Gestionar mi perfil--")
        print("a-Editar mis datos personales")
    elif seleccion_pri == "2":
        print("s")
    elif seleccion_pri == "3":
        print("t")
    elif seleccion_pri == "4":
        print("e")
    elif seleccion_pri == "0":
        print("ss")
    else:
        print("?")
menu_principal()
