# Una empresa metalúrgica que realiza piezas a medida necesita un programa que permita realizar estadísticas sobre sus proyectos.
# Por cada Proyecto se conoce: un código de identificación (una cadena), nombre de la empresa que realizó el encargo, cantidad
# de piezas a fabricar, tipo de pieza (un entero entre 100 y 120) y el costo por pieza. Se desea almacenar la información
# referida a los n proyectos en un arreglo de registros de tipo Proyecto (definir el tipo Proyecto y cargar n por teclado).
# Se pide desarrollar un programa en Python controlado por un menú de opciones y que posea como mínimo dos módulos,
# que permita gestionar las siguientes tareas:

import random
from empresa_metalurgica_class import *
random.seed(1010)

def menu_opciones():
    print('Opcion 1: Cargar datos')
    print('Opcion 2: Mostrar datos')
    print('Opcion 3: Importe total')
    print('Opcion 4: Buscar proyecto')
    print('Opcion 5: Salir')

def validar_n():
    n = int(input('Ingrese la cantidad de proyectos: '))
    while n <= 0:
        n = int(input('ERROR 404, ingrese la cantidad nuevamente'))
    return n

def cargar_vector_automat(n, vec):
    for i in range(n):
        #random nombres
        nom1 = 'Jose', 'Miguel', 'Maria', 'Maxi', 'Mariano', 'Gustavo', 'Samira'
        nom2 = 'Arreglos', 'Viajes', 'Reparaciones', 'Soluciones', 'Instalaciones', 'Piezas', 'Repuestos'
        # Genero los datos
        codigoid = i+1
        #nombremp = 'empresa' + str(codigoid)
        nombremp = random.choice(nom1) + ' ' + random.choice(nom2) + ' ' + str(codigoid)
        cantpiezas = random.randint(1, 20)
        piezatipo = random.randint(100, 120)
        piezacosto = round(random.uniform(1000, 25000), 2)
        # Creo el registro
        est = Estadistica(codigoid, nombremp, cantpiezas, piezatipo, piezacosto)
        # Agrego al vector
        vec.append(est)

def vector_completo(vec):
    for est in vec:
        print(est)


def ordenar_por_nombre(vec):
    n = len(vec)
    for i in range(0, n-1):
        for j in range(i+1 , n):
            if vec[i].nombremp > vec[j].nombremp:
                vec[i] , vec[j] = vec[j] , vec[i]

def mostrar_el_vector(vec):
    ordenar_por_nombre(vec)
    acum = 0
    for est in vec:
        acum += est.cantpiezas
    prom = acum // len(vec)

    for est in vec:
        if prom < est.cantpiezas:
            print(est)

def main():
    vec = []
    op = 0
    while op != 5:
        menu_opciones()
        op = int(input('Ingrese su opcion: '))
        if op == 1:
            # 1. Cargar el arreglo con los datos de los n proyectos. Valide o asegure trodos los datos cargados o generados sean correctos.
            # Puede hacer la carga en forma manual, o puede generar los datos en forma automática (con valores aleatorios). Pero al
            # menos una debe programar. Pero si hace carga automática, todos los campos deben ser cargados así (no combine ambas
            # técnicas en la carga de un registro).
            #TLDR: Cargar n proyectos al array y validar los datos. usar manual o auto
            n = validar_n()
            cargar_vector_automat(n, vec)
            vector_completo(vec)

        elif op == 2:
            # 2. Mostrar los datos de todos los proyectos cuya cantidad a fabricar sea mayor al promedio de piezas a fabricar de todo el
            # arreglo. El listado debe salir ordenado ordenados alfabéticamente por el nombre de las empresas solicitantes. Mostrar a
            # razón de un registro por línea. Al final del listado, muestre el promedio de piezas a fabricar que calculó para generar el
            # informe.
            #TLDR: Mostrar solo los proyectos que tengan mas piezas que el promedio de todos los proyectos. mostrar ordenados alfabeticamente
            #por nombre de empresa

            mostrar_el_vector(vec)

        elif op == 3:
            # 3. Determine el importe total a fabricar por cada tipo de pieza (20 acumuladores en un vector de acumulación). Pero solo
            # muestre los acumuladores desde el ac en adelante (siendo ac un número cargado por teclado). Por ejemplo, si ac vale
            # 100, muestre todos los acumuladores. Si ac vale 110, muestre todos desde el que corresponde al 110 en adelante, y así
            # por estilo.
            #TLDR:
            pass
        elif op == 4:
            # 4. Buscar un proyecto cuyo nombre de empresa solicitante coincida con emp y cuya cantidad de piezas a fabricar cp sea
            # menor a otro valor x (los valores emp, cp y x se cargan por teclado). Si existe, actualizar la cantidad de piezas de ese
            # registro sumándole un valor v cargado por teclado, y mostrar los datos. Si no existe indicar con un mensaje. Debe mostrar
            # los datos del primer
            #TLDR:
            pass
        elif op == 5:
            print('Bye Bye')
        else:
            print('Opcion incorrecta')







if __name__ == '__main__':
    main()