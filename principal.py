from funciones import *
import msvcrt,os,time

while True:
    os.system('cls')
    print('Gaxplosive.')
    print('1. Registrar pedido')
    print('2. Listar los pedidos. ')
    print('3. Buscar pedido por rut')
    print('4. Imprimir hoja de pedido. ')
    print('5. Salir.')
    opc=input('Ingrese una opción: ')
    os.system('cls')
    if opc=='1':
        registrar_pedido()
    elif opc=='2':
        Listar_pedidos()
    elif opc=='3':
        buscar_por_rut()
    elif opc=='4':
        Imprimir_hoja()
    elif opc=='5':
        salir()
    else:
        print('ERROR, debe ser de 1 a 5...')
    print('Ingrese una tecla para continuar...')
    msvcrt.getch()    