import random
from estudio2class import *
random.seed(1010)

def menu_opciones():
    print('Opcion 1.')
    print('Opcion 2.')
    print('Opcion 3.')
    print('Opcion 4.')
    print('Opcion 5.')
    print('Opcion 6.')

def validar_n():
    n = int(input('Ingrese el valor de n: '))
    while n <= 0:
        n = int(input('ERROR !!!! Ingrese el valor de n: '))
    return n

def cargar_vector(vec, n):
    # 1- Cargar el arreglo pedido con los datos de las n actividades. Valide que el día sea mayor o igual a 1 y
    # menor o igual a 31, que el importe a cobrar sea mayor a cero, y que la cantidad de personas sea 0 o
    # mayor que 0. Puede hacer la carga en forma manual, o puede generar los datos en forma automática
    # (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe
    # programar.
    for i in range(n):
        dia = random.randint(1, 31)
        descripcion = 'ejercicios ' + str(i+1)
        importe = round(random.uniform(1, 5000))
        cantidad = random.randint(0,100)
        nombre = 'guia ' + str(i+1)

        c = club(dia,descripcion,importe,cantidad,nombre)
        vec.append(c)

def mostrar_vec(vec):
    for i in vec:
        print(i)

def ordenar_vec(vec):
    n = len(vec)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if vec[i].dia > vec[j].dia:
                vec[i] , vec[j] = vec[j] , vec[i]



def punto_2(vec):
    # 2- Mostrar todos los datos de las actividades, a razón de un registro por línea, que tengan día de partida
    # entre ini y fin, siendo ini y fin valores enteros que se cargan por teclado. El listado debe salir
    # ordenado por día de partida. Al final del listado, mostrar una línea adicional con la cantidad total de
    # personas que participarán las actividades mostradas en el listado
    mostrar_vec(vec)
    ini = int(input('Ingrese el valor de ini: '))
    while ini <= 0:
        ini = int(input('ERROR !!!! Ingrese el valor de ini: '))

    fin = int(input('Ingrese el valor de fin: '))
    while fin <= 0:
        fin = int(input('ERROR !!!! Ingrese el valor de fin: '))


    cont_personas = 0
    for i in vec:
        if i.dia >= ini and i.dia <= fin:
            cont_personas += i.cantidad
            print(i)
    print('Participaran:', cont_personas)


def punto_3(vec):
    # 3- Determinar y mostrar el importe total recaudado por cada posible día del mes. En total, 31
    # acumuladores. Mostrar todos los valores cuyo resultado sea mayor a 0.
    vec_p3 = [0] * 31
    for i in vec:
        indice = i.dia
        vec_p3[indice-1] += i.importe

    for i in range(len(vec_p3)):
        if vec_p3[i] >= 1:
            print('El dia ' + str(i+1) + ' se recaudo ' + str(vec_p3[i]))


def punto_4(vec):
    # 4- Determinar y mostrar el DIA y la DESCRIPCION de la actividad que tenga más personas registradas. Si
    # además esa actividad supera una cantidad x (x se carga por teclado) informar con otro mensaje que
    # hará falta un guía extra. En el caso de que exista más de una actividad con la misma cantidad de
    # másxima personas mostrar todas, y para cada una informar (si corresponde) el mensaje para el guía
    # extra.
    vec_p4 = []
    n = len(vec)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if vec[i].cantidad < vec[j].cantidad:
                vec[i] , vec[j] = vec[j] , vec[i]

    x = int(input('Ingrese el valor de x: '))
    while x <= 0:
        x = int(input('ERROR !!!! Ingrese el valor de x: '))
    mayor_valor = vec[0]
    for i in vec:
        if mayor_valor.cantidad == i.cantidad:
            vec_p4.append(i)

    for i in vec_p4:
        if i.cantidad > x:
            print('Dia: ' + str(i.dia) + ' | Descripcion: ' + str(i.descripcion) + ' Le hace falta un guia extra')
        else:
            print('Dia: ' + str(i.dia) + ' | Descripcion: ' + str(i.descripcion))

def punto_5(vec):
    # 5- Determinar si existe una actividad para el día d y con descripción t, siendo d y t valores que se carga
    # por teclado. Si existe, mostrar todos sus datos. Si no existe, indicar con un mensaje. Si existe más de
    # una actividad para el día y descripción cargados mostrar solo la primera
    d = int(input('Ingrese el valor de d: '))
    t = input('Ingrese el valor de t: ')
    while d <= 0:
        d = int(input('ERROR !!!! Ingrese el valor de d: '))
    encontro = None
    for i in vec:
        if i.dia == d and i.descripcion == t:
            encontro = i
            break
    return encontro








def main():
    vec = []
    op = 0
    esta_ordenado = None
    while op != 6:
        menu_opciones()
        op = int(input('Seleccione el menu: '))
        if op == 1:
            # 1- Cargar el arreglo pedido con los datos de las n actividades. Valide que el día sea mayor o igual a 1 y
            # menor o igual a 31, que el importe a cobrar sea mayor a cero, y que la cantidad de personas sea 0 o
            # mayor que 0. Puede hacer la carga en forma manual, o puede generar los datos en forma automática
            # (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe
            # programar.
            n = validar_n()
            cargar_vector(vec, n)
            mostrar_vec(vec)

        elif op == 2:

            if vec != []:
            # 2- Mostrar todos los datos de las actividades, a razón de un registro por línea, que tengan día de partida
            # entre ini y fin, siendo ini y fin valores enteros que se cargan por teclado. El listado debe salir
            # ordenado por día de partida. Al final del listado, mostrar una línea adicional con la cantidad total de
            # personas que participarán las actividades mostradas en el listado.
                if ordenar_vec(vec):
                    esta_ordenado = True
                punto_2(vec)

            else:
                print('Tiene que cargar el vector primero')
            pass


        elif op == 3:

            # 3- Determinar y mostrar el importe total recaudado por cada posible día del mes. En total, 31
            # acumuladores. Mostrar todos los valores cuyo resultado sea mayor a 0.

            if vec != []:
                punto_3(vec)

            else:
                print('Tiene que cargar el vector primero')



        elif op == 4:
            # 4- Determinar y mostrar el DIA y la DESCRIPCION de la actividad que tenga más personas registradas. Si
            # además esa actividad supera una cantidad x (x se carga por teclado) informar con otro mensaje que
            # hará falta un guía extra. En el caso de que exista más de una actividad con la misma cantidad de
            # másxima personas mostrar todas, y para cada una informar (si corresponde) el mensaje para el guía
            # extra.

            if vec != []:
                punto_4(vec)

            else:
                print('Tiene que cargar el vector primero')



        elif op == 5:
            # 5- Determinar si existe una actividad para el día d y con descripción t, siendo d y t valores que se carga
            # por teclado. Si existe, mostrar todos sus datos. Si no existe, indicar con un mensaje. Si existe más de
            # una actividad para el día y descripción cargados mostrar solo la primera

            if vec != []:
                encontro = punto_5(vec)
                if encontro != None:
                    print(encontro)
                else:
                    print('No se encontraron ventas con esos valores')

            else:
                print('Tiene que cargar el vector primero')
            pass


        elif op == 6:
            print("Fin del programa")
        else:
            print("Ingrese una opcion correcta entre 1 y 6")








if __name__ == '__main__':
    main()