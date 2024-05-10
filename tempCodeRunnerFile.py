 opc_principal=1
    while opc_principal != 0:
        limpiar_pantalla()
        menu_principal()
        opc_principal = input("Ingrese opcion: ")
        match int(opc_principal):
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