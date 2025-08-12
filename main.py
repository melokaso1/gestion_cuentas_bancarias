#importes
import os 
import random

#dict
db = {
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
    nombre = input('Ingrese el nombre completo: ')
    dni = input('Ingrese el numero de documento: ')
    email = input('Ingrese el correo electronico: ')
    movil = input('Ingrese el numero de telefono: ')
    fijo = input('Ingrese el numero de telefono fijo: ')
    pais = input('Ingrese el pais de residencia: ')
    dep = input('Ingrese el departamento de residencia: ')
    ciudad = input('Ingrese la ciudad o municipio de residencia: ')
    dirc = input('Ingrese la direccion de residencia: ')
    
    while acc:
        acc_num = random.randint(0,10000)

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
            }
        }
    print(f'Usuario creado con exito, su numero de usuario es: {acc_num}')
    input('oprima enter para continuar')

#inicio de programa
while True:
    try:
        match int(menu()):
            case 1:
                registro_user()
            case 2:
                match int(menu_solicitud_productos()):
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
            case 3:
                match int(menu_depositos()):
                    case 1:
                        pass
                    case 2: 
                        pass
                    case 3:
                        pass
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
    except:
        continue