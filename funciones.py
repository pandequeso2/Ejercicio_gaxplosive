#FUNCIONES PRINCIPALES:
import csv
pedidos=[]
comunas=('Puente alto','Pirque','La pintana')
def registrar_pedido():
    print('Registrar pedido. ')
    rut=int(input('Ingrese rut: '))
    nombre=input('Ingrese su nombre: ')
    direccion=input('Ingrese su direcion: ')
    comuna=int(input('Ingrese el numero de la comuna(1: Puente alto, 2: Pirque, 3: La pintana): '))
    print('\n PEDIDO.')
    #Primera forma: Pedir la cantidad de cilindros de 5kg yla cantidad de cilindoros
    #Segunda forma: Preguntar constantemente que cilindo quiere y la cantidad:
    cant_5k=int(input('Ingrese cantidad de cilindros de 5 kilos: '))
    cant_15K=int(input('Ingrese la cantidad de cilindros de 15 kiilos: '))
    total= cant_5k*12500 + cant_15K*25500
    #Como almacenan 1 pedido: Como dicionario!!
    pedido={'rut':rut,
            'nombre':nombre,
            'direccion':direccion,
            'comuna': comunas[comuna-1],
            'cantidad_5k':cant_5k,
            'cantidad_15k':cant_15K,
            'total':total}
    pedidos.append(pedido)
    print('Pedido agregado con exito!...')
def Listar_pedidos():
    if not pedidos:
        print('Esta en blanco, ve a la opcion 1 primero...')
    else:
        print('Lista de pedidos. ')
        for p in pedidos:
            print(f'Rut: {p['rut']}')
            print(f'Nombre: {p['nombre']}')
            print(f'Dirección: {p['direccion']}')
            print(f'Comuna: {p['comuna']}')
            print(f'Cantidad 5kg: {p['cantidad_5k']}')
            print(f'Cantidad 15kg: {p['cantidad_15k']}')
            print(f'Total: ${p['total']}')
            print()
def buscar_por_rut():
    if not pedidos:
        print('Lista en blanco, ve a la opcion 1 primero...')
    else:
        print('Buscar pedido por rut.')
        rut_buscar=int(input('Ingrese el rut a buscar: '))
        rut_existe=False
        for p in pedidos:
            if rut_buscar==p['rut']:
                rut_existe=True
                print(f'Rut: {p['rut']}')
                print(f'Nombre: {p['nombre']}')
                print(f'Dirección: {p['direccion']}')
                print(f'Comuna: {p['comuna']}')
                print(f'Cantidad 5kg: {p['cantidad_5k']}')
                print(f'Cantidad 15kg: {p['cantidad_15k']}')
                print(f'Total: ${p['total']}')
                print()
        if rut_existe==False:        
            print('Rut no existee!')
def Imprimir_hoja():
    if not pedidos:
        print('No existen pedidos.')
    else:
        print('Imprimir hoja en csv')
        comuna=int(input('Ingese su comuna:(1: Puente alto, 2: Pirque, 3: La pintana): '))
        nom_archivo=input('Ingrese el nombre de el archivo: ')+'.csv'
        try:
            with open(nom_archivo,'x',newline='') as file:
                escritor=csv.DictWriter(file,['rut','nombre','direccion','couna','cantidad_5k','cantidad_15k','total'])
                escritor.writeheader()
                for p in pedidos:
                    if p['comuna']==comunas[comuna-1]:
                        escritor.writerow(p)
            print('Archivo creado con exito...')            
        except:
            print('ERROR, el nombre de el archivo ya existe...')   
def salir():
    print('ADIOOOS...')
    exit()
