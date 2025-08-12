def menu():
    pass

def menu_depositos():
    pass

def menu_creditos():
    pass

def menu_pago_creditos():
    pass

def menu_retiros():
    pass

def menu_cancelar():
    pass


while True:
    try:
        match int(menu()):
            case 1:
                pass
            case 2:
                match int(menu_depositos()):
                    case 1:
                        pass
                    case 2: 
                        pass
                    case 3:
                        pass
            case 3:
                match int(menu_creditos()):
                    case 1:
                        pass
                    case 2: 
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
            case 4:
                match int(menu_retiros()):
                    case 1:
                        pass
                    case 2: 
                        pass
                    case 3:
                        pass
            case 5:
                match int(menu_pago_creditos()):
                    case 1:
                        pass
                    case 2: 
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
            case 6:
                match int(menu_cancelar()):
                    case 1:
                        pass
                    case 2: 
                        pass
                    case 3:
                        pass
            case 7:
                break
    except:
        pass