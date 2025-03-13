# Un club de trecking que acostumbra a organizar actividades al aire libre necesita un programa que permita
# organizar las actividades del mes. De cada actividad se registra: el día de partida (un número entero entre 1 y
# 31), la descripción (una cadena de caracteres), el importe que se cobra para cubrir gastos, la cantidad de
# personas registradas y el nombre del guía. Se desea almacenar la información referida a los n servicios en un
# arreglo de registros de tipo Actividad (definir el tipo Actividad y cargar n por teclado).
# Se pide desarrollar un programa en Python controlado por un menú de opciones y que posea como mínimo dos
# módulos, que permita gestionar las siguientes tareas:

class club:
    def __init__(self,dia,descripcion,importe,cantidad,nombre):
        self.dia = dia
        self.descripcion = descripcion
        self.importe = importe
        self.cantidad = cantidad
        self.nombre = nombre

    def __str__(self):
        return 'Dia: ' + str(self.dia) + ' | Descripcion: ' + str(self.descripcion) + ' | Importe: ' + str(self.importe) + \
            ' | Cantidad de Personas: ' + str(self.cantidad) + ' | Nombre: ' + str(self.nombre)

