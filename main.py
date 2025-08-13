#importes
import os 
import random
import time

#dict
db = { 7086 : {'cuentas' : {}}
}

#Menus
def menu():
    os.system("cls")
    a = input('''
  SISTEMA DE GESTION BANCARIA
===============================

#1 Registro de cliente
#2 Solicitud Productos
#3 Deposito a cuentas
#4 Solicitud de creditos
#5 Retiros de cuentas
#6 Pagos a creditos
#7 Cerrar cuenta
#8 Salir

Seleccione una opcion: ''')
    
    return a

def menu_solicitud_productos():
    os.system("cls")
    a = input('''
  SOLICITUD DE PRODUCTOS
==========================

#1 Cuenta de ahorros
#2 Cuenta corriente
#3 CDT
#4 salir

Seleccione una opcion: ''')
    return a

def menu_depositos():
    os.system('cls')
    a = input('''
  DEPOSITOS A CUENTAS
=======================

#1 Cuenta de ahorros
#2 Cuenta corriente
#3 salir

Seleccione una opcion: ''')
    return a

def menu_creditos():
    os.system('cls')
    a = input('''
  SOLICITUD DE CREDITOS
=========================

#1 Credito de libre inversion
#2 Credito de vivienda
#3 Credito vehicular
#4 Salir

Seleccione una opcion: ''')
    return a

def menu_retiros():
    os.system('cls')
    a = input('''
  RETIROS
===========

#1 Cuenta de ahorros
#2 Cuenta corriente
#3 salir

Seleccione una opcion: ''')
    return a

def menu_pago_creditos():
    os.system('cls')
    a = input('''
  PAGO DE CREDITOS
=====================

#1 Credito de libre inversion
#2 Credito de vivienda
#3 Credito 
#4 Salir

Seleccione una opcion: ''')
    return a

def menu_cancelar():
    a = input('''
  CANCELAR CUENTA O PRODUCTOS
===============================

#1 Cuenta de ahorros
#2 Cuenta corriente
#3 CDT
#4 salir

Seleccione una opcion: ''')

#logica
#funciones logicas
def registro_user():
    os.system('cls')
    acc = True
    nombre = input('Ingrese el nombre completo: ').upper().strip()
    dni = input('Ingrese el numero de documento: ').upper().strip()
    email = input('Ingrese el correo electronico: ').upper().strip()
    movil = input('Ingrese el numero de telefono: ').strip()
    fijo = input('Ingrese el numero de telefono fijo: ').strip()
    pais = input('Ingrese el pais de residencia: ').upper().strip()
    dep = input('Ingrese el departamento de residencia: ').upper().strip()
    ciudad = input('Ingrese la ciudad o municipio de residencia: ').upper().strip()
    dirc = input('Ingrese la direccion de residencia: ').upper().strip()
    
    while acc:
        acc_num = random.randint(0, 10000)

        if acc_num  in db.keys():
            acc = True
        else:
            acc = False
    
    db[acc_num] = {
        'nombre': nombre,
        'dni': dni,
        'email': email,
        'contacto': {
            'movil': movil,
            'fijo': fijo
        },
        'ubicacion' : {
            'pais': pais,
            'departamento': dep,
            'ciudad': ciudad,
            'direccion': dirc
            },
        'cuentas' : {
        }
        
        
        }
    print(f'Usuario creado con exito, su numero de usuario es: {acc_num}')
    input('oprima enter para continuar')

#filtro de usuarios
def filtro_user(a, func):    
    if a in db.keys():
        print('Usuario encontrado')
        
    else:
        print('Usuario no existe, intente de nuevo')
        time.sleep(1)
        func()

#agregar cuentas
def add_acc_ahorro():
    filtro_user(numero_user, add_acc_ahorro)
    while True:
        num_acc = random.randint(100, 199)
        if num_acc in db[numero_user]['cuentas'].keys():
            continue
        else: 
            db[numero_user]['cuentas'] = {num_acc : 0}
            print(f'Cuenta de ahorros creada con exito, el numero de cuenta es: {num_acc}')
            input('Precione enter para continuar...')
            break
    
def add_acc_corriente():
    os.system('cls')
    filtro_user(numero_user, add_acc_corriente)
    
    while True:
        num_acc = random.randint(200, 299)
        if num_acc in db[numero_user]['cuentas'].keys():
            continue
        else: 
            db[numero_user]['cuentas'] = {num_acc : 0}
            print(f'Cuenta corriente creada con exito, el numero de cuenta es: {num_acc}')
            input('Precione enter para continuar...')
            break
def add_CDT():
    os.system('cls')
    filtro_user(numero_user, add_CDT)
    inv = int(input('Ingrese el valor de la inversion: '))
    
    v_g = inv * 0.12
    v_t = inv + v_g
    
    while True:
        num_acc = random.randint(300, 399)
        if num_acc in db[numero_user]['cuentas'].keys():
            continue
        else:
            db[numero_user]['cuentas'] = {num_acc : v_t}
            print(f'''Cuenta de CDT creado con exito, el numero de cuenta es: {num_acc}
Su saldo del CDT estimado a 1 año al 12% anual es: {v_t}''')
            input('Precione enter para continuar...')
            break

#inicio de programa
while True:
    try:
        match int(menu()):
            case 1:
                registro_user()
            case 2:
                global numero_user
                os.system('cls')
                numero_user = int(input('Ingrese el numero de usuario: '))
                while True:    
                    match int(menu_solicitud_productos()):
                        case 1:
                            add_acc_ahorro()
                        case 2:
                            add_acc_corriente()
                        case 3:
                            add_CDT()
                        case 4:
                            break
            case 3:
                os.system('cls')
                numero_user = int(input('Ingrese el numero de usuario: '))
                while True: 
                    match int(menu_depositos()):
                        case 1:
                            pass
                        case 2: 
                            pass
                        case 3:
                            break
            case 4:
                match int(menu_creditos()):
                    case 1:
                        pass
                    case 2: 
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
            case 5:
                match int(menu_retiros()):
                    case 1:
                        pass
                    case 2: 
                        pass
                    case 3:
                        pass
            case 6:
                match int(menu_pago_creditos()):
                    case 1:
                        pass
                    case 2: 
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
            case 7:
                match int(menu_cancelar()):
                    case 1:
                        pass
                    case 2: 
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
            case 8:
                break
    except ValueError:
        continue