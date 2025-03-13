

# a. Cargar el arreglo pedido con los datos de los n juicios. Valide o asegure que los datos cargados sean correctos.
# Puede hacer la carga en forma manual, o puede generar los datos en forma automática (con valores
# aleatorios). Pero al menos una debe programar. Pero si hace carga automática, todos los campos deben ser
# cargados así (no combine ambas técnicas en la carga de un objeto).

# b. Mostrar datos de todos los juicios cuyo monto de honorarios sea mayor a mon (que se carga por teclado), en
# un listado ordenado de menor a mayor según la descripción o carátula, a razón de un juicio por línea. Al final
# del listado, indique cuántos objetos se mostraron.

# c. Determinar y mostrar la cantidad de juicios que hay por cada posible tipo (15 contadores en un vector de
# conteo). Mostrar sólo aquellos contadores que sean mayores a una cantidad c ingresada por teclado.

# d. Determinar si existe un juicio cuyo código de expediente sea igual a cod. Si existe alguno, modificar el monto
# de honorarios de ese objeto tomando el nuevo valor por teclado, y mostrar los datos de ese juicio incluyendo
# esa modificación. Si no existe, informar con un mensaje. Debe mostrar los datos del primero que encuentre, y
# detener la búsqueda en el primero que encuentre (sin importar si hay más de un objeto que cumpla el criterio
# pedido)

import random
from estudio_juridico_class import *
random.seed(1010)


def menu():
    print('Opcion 1: ')
    print('Opcion 2: ')
    print('Opcion 3: ')
    print('Opcion 4: ')
    print('Opcion 5: Salir ')



def ordenar_vec(vec):
    n = len(vec)
    for i in range(0, n+1):
        for j in range(i+1, n):
            if vec[i].descripcion > vec[j].descripcion:
                vec[i], vec[j] = vec[j], vec[i]




def validar_n():
    n = int(input('Ingrese el valor de n: '))
    while n <= 0:
        n = int(input('ERROR!!!! Ingrese el valor de n: '))
    return n


def cargar_vector(n, vec):
    # Un estudio de abogados desea un sistema para procesar los datos de los juicios que tiene en su cartera. Por cada
    # Juicio se conoce su código de expediente (un número entero), la descripción o carátula del juicio (una cadena), el
    # tipo de juicio (un entero entre 1 y 15), el nombre del cliente defendido, y el monto de honorarios a cobrar por ese
    # juicio. Se desea almacenar la información referida a los n juicios en un arreglo de objetos de tipo Juicio (definir el
    # tipo Juicio y cargar n por teclado). Se pide desarrollar un programa en Python controlado por un menú de
    # opciones, en el que se incluyan como mínimo dos módulos, para permita gestionar las siguientes tareas:

    for i in range(n):
        expediente = random.randint(1, 5000)
        descripcion = 'descripcion ' + str(i+1)
        tipo = random.randint(1,15)
        cliente = 'cliente ' +  str(i+1)
        monto = round(random.uniform(1000, 6000), 2)

        p = Juicios(expediente, descripcion, tipo, cliente, monto)
        vec.append(p)


def mostrar_todo(vec):
    for i in vec:
        print(i)

def punto_2(vec):
    # b. Mostrar datos de todos los juicios cuyo monto de honorarios sea mayor a mon (que se carga por teclado), en
    # un listado ordenado de menor a mayor según la descripción o carátula, a razón de un juicio por línea. Al final
    # del listado, indique cuántos objetos se mostraron.
    mon = int(input('Ingrese el valor de mon: '))
    while mon <= 0:
        mon = int(input('ERROR!!!! Ingrese el valor de mon: '))
    contador_p2 = 0
    for i in vec:
        if i.monto > mon:
            contador_p2 += 1
            print(i)
    if contador_p2 > 0:
        print('Se encontraron ', str(contador_p2), 'objetos')
    else:
        print('No se encontraron objetos')


def punto_3(vec):
    # c. Determinar y mostrar la cantidad de juicios que hay por cada posible tipo (15 contadores en un vector de
    # conteo). Mostrar sólo aquellos contadores que sean mayores a una cantidad c ingresada por teclado.
    vec_p3 = [0] * 15

    c = int(input('Ingrese el valor de c: '))
    while c < 0:
        c = int(input('ERROR!!!! Ingrese el valor de c: '))

    indice = 0
    for i in vec:
        indice = i.tipo
        vec_p3[indice-1] += 1

    for tipo in range(len(vec_p3)):

        if vec_p3[tipo] > c:
            print('Para el tipo: ' + str(tipo+1) + ' Hay ' + str(vec_p3[tipo]) +' juicios')



def punto_4(vec):
    # d. Determinar si existe un juicio cuyo código de expediente sea igual a cod. Si existe alguno, modificar el monto
    # de honorarios de ese objeto tomando el nuevo valor por teclado, y mostrar los datos de ese juicio incluyendo
    # esa modificación. Si no existe, informar con un mensaje. Debe mostrar los datos del primero que encuentre, y
    # detener la búsqueda en el primero que encuentre (sin importar si hay más de un objeto que cumpla el criterio
    # pedido)
    cod = int(input('Ingrese el valor de cod: '))
    while cod <= 0:
        cod = int(input('ERROR!!!! Ingrese el valor de cod: '))
    hola = None
    for i in vec:
        if i.expediente == cod:
            nuevo_m = int(input('Ingrese el valor del nuevo monto: '))
            while nuevo_m <= 0:
                nuevo_m = int(input('ERROR!!!! Ingrese el valor de nuevo monto: '))

            i.monto = nuevo_m
            hola = i
            return hola
            break







def main():
    vec = []
    op = 0
    while op != 5:
        esta_ordenado = False
        menu()
        op = int(input('Ingrese la opcion: '))
        if op == 1:
            # a. Cargar el arreglo pedido con los datos de los n juicios. Valide o asegure que los datos cargados sean correctos.
            # Puede hacer la carga en forma manual, o puede generar los datos en forma automática (con valores
            # aleatorios). Pero al menos una debe programar. Pero si hace carga automática, todos los campos deben ser
            # cargados así (no combine ambas técnicas en la carga de un objeto).
            n = validar_n()
            cargar_vector(n, vec)
            mostrar_todo(vec)



        elif op == 2:
            # b. Mostrar datos de todos los juicios cuyo monto de honorarios sea mayor a mon (que se carga por teclado), en
            # un listado ordenado de menor a mayor según la descripción o carátula, a razón de un juicio por línea. Al final
            # del listado, indique cuántos objetos se mostraron.
            if vec != []:

                if ordenar_vec(vec):
                    esta_ordenado = True

                punto_2(vec)
            else:
                print('Primero debes cargar el vector')

        elif op == 3:
            # c. Determinar y mostrar la cantidad de juicios que hay por cada posible tipo (15 contadores en un vector de
            # conteo). Mostrar sólo aquellos contadores que sean mayores a una cantidad c ingresada por teclado.
            if vec != []:

                punto_3(vec)


            else:
                print('Primero debes cargar el vector')

        elif op == 4:
            if vec != []:

                hola = punto_4(vec)

                if hola != None:
                    print(hola)
                else:
                    print('No se encontro dicho expediente.')


            else:
                print('Primero debes cargar el vector')

        elif op == 5:
            print('Byeeeeeeeeeee')

        else:
            print('Ingrese una opcion valida')






if __name__ == '__main__':
    main()