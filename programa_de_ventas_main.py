import random
from clasecaso1 import *
random.seed(1010)

def menu_opciones():
    print('Opcion 1: Cargar datos')
    print('Opcion 2: Mostrar datos ordenados')
    print('Opcion 3: Cantidad de ventas')
    print('Opcion 4: Menor importe')
    print('Opcion 5: Buscar ticket')
    print('Opcion 6: Salir')

def validar_n():
    n = int(input('Ingrese el valor de n: '))
    while n <= 0:
        n = int(input('ERROR !!!!! Ingrese el valor de n'))
    return n

def cargar_datos(n, vec):
    for i in range(n):
        ticket = i+1
        cliente = 'cliente '+ str(ticket)
        importe = round(random.uniform(100, 6000),2)
        codigov = random.randint(1,13)
        codigop = random.randint(0,7)

        emp = empresa(ticket, cliente, importe, codigov, codigop)
        vec.append(emp)

def ordenar_vector(vec):
    n = len(vec)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if vec[i].importe < vec[j].importe:
                vec[i] , vec[j] = vec[j] , vec[i]

def vector_completo(vec):
    for est in vec:
        print(est)

def punto_2(vec):
    vec_p2 = []

    x = int(input('Ingrese el valor de x: '))
    while x <= 0:
        x = int(input('ERROR !!!!! Ingrese el valor de x: '))

    e = int(input('Ingrese el valor de e: '))
    while e <= 0:
        e = int(input('ERROR !!!!! Ingrese el valor de e: '))

    for est in vec:
        if est.importe >= x and est.importe <= e:
            vec_p2.append(est)

    #ordenar_vector(vec_p2)

    if vec_p2 == []:
        print('No se encontraron valores!!!')
    else:
        for i in vec_p2:
            print('Cliente: ' + str(i.cliente) +' | Importe: ' + str(i.importe) + ' |  Codigo Producto: ' + str(i.codigop))


def punto_3(vec):
    # 3- Determinar cuántas ventas de cada código de producto se realizaron (8 contadores). Indicar si la empresa vendió más productos
    # con código de producto par o con código de producto impar e informar por pantalla estos valores.
    vec_cont = [0] * 8
    for ventas in vec:
        indice = ventas.codigop
        vec_cont[indice] += 1
    cont_par = 0
    cont_impar = 0
    for i in range(len(vec_cont)):
        print(i, vec_cont[i])
        if (i % 2) == 0:
            cont_par += vec_cont[i]
        else:
            cont_impar += vec_cont[i]
    if cont_par == cont_impar:
        print('Se encontro la misma cantidad de importes PARES: ', cont_par, ' y ' , cont_impar, ' IMPARES')

    elif cont_par > cont_impar:
        print('La empresa vendio MAS productos con codigo PAR: ', cont_par, ' y ' , cont_impar, ' IMPARES')
    else:
        print('La empresa vendio MAS productos con codigo IMPAR: ', cont_impar, ' y ', cont_par, ' PARES')


def punto_4(vec, vec_ordenado):
    # 4- Determinar y mostrar el número de ticket, el nombre del cliente y el código de producto de la venta que tenga el menor importe
    # de venta realizada. Mostrar estos datos en una sola línea.
    menor_valor = 0

    if vec_ordenado is True:
        menor_valor = vec[-1]
    else:
        menor_valor = vec[1]
        for i in range(1, len(vec)):
            if vec[i].importe < menor_valor.importe:
                menor_valor = vec[i]

    print('Ticket: ' + str(menor_valor.ticket) + ' | Cliente: ' + str(menor_valor.cliente) + ' |  Codigo Producto: ' + str(menor_valor.codigop))


def punto_5(vec):
    # 5- Determinar si existe alguna venta cuyo número de ticket sea igual a t, pero que también tengo un código de vendedor entre 1 y 5.
    # Si existe, mostrar todos los datos de ese registro. Si no existe, informar con un mensaje.
    t = int(input('Ingrese el valor de t: '))
    while t <= 0:
        t = int(input('ERROR !!!!! Ingrese el valor de t: '))

    encontro = None
    for i in vec:
        if i.ticket == t and (i.codigov >= 1 and i.codigov <= 5):
            encontro = i
            break

    return encontro






def main():

    op = 0
    vec = []
    vec_ordenado = False
    while op != 6:
        menu_opciones()
        op = int(input('Ingrese la opcion: '))
        if op == 1:
            # 1- Cargar el arreglo con los datos de las n ventas. Validar que el importe sea mayor a 0 y que el código de vendedor y el del producto
            # estén en el rango indicado. Puede hacer la carga en forma manual, o puede generar los datos en forma automática (con valores
            # aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.

            n = validar_n()
            cargar_datos(n , vec)
            vector_completo(vec) #COMENTAR!!!

        elif op == 2:
            # 2- Mostrar el nombre del cliente, el importe y el código del producto de todas las ventas con un importe total entre x e y (con x e y
            # ingresados por teclado). Este listado debe mostrar una línea por cada venta y debe estar presentado en orden de mayor a menor
            # según el importe de la venta.
            if ordenar_vector(vec):
                vec_ordenado = True
            punto_2(vec)

        elif op == 3:
            # 3- Determinar cuántas ventas de cada código de producto se realizaron (8 contadores). Indicar si la empresa vendió más productos
            # con código de producto par o con código de producto impar e informar por pantalla estos valores.
            punto_3(vec)


        elif op == 4:
            # 4- Determinar y mostrar el número de ticket, el nombre del cliente y el código de producto de la venta que tenga el menor importe
            # de venta realizada. Mostrar estos datos en una sola línea.
            punto_4(vec, vec_ordenado)
        elif op == 5:
            # 5- Determinar si existe alguna venta cuyo número de ticket sea igual a t, pero que también tengo un código de vendedor entre 1 y 5.
            # Si existe, mostrar todos los datos de ese registro. Si no existe, informar con un mensaje.
            encontro = punto_5(vec)
            if encontro != None:
                print(encontro)
            else:
                print('No se encontraron ventas con esos valores')

        elif op == 6:
            print('Error')
        else:
            print('Opcion incorrecta')







if __name__ == '__main__':
    main()
