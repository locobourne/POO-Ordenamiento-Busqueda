# Un estudio de abogados desea un sistema para procesar los datos de los juicios que tiene en su cartera. Por cada
# Juicio se conoce su código de expediente (un número entero), la descripción o carátula del juicio (una cadena), el
# tipo de juicio (un entero entre 1 y 15), el nombre del cliente defendido, y el monto de honorarios a cobrar por ese
# juicio. Se desea almacenar la información referida a los n juicios en un arreglo de objetos de tipo Juicio (definir el
# tipo Juicio y cargar n por teclado). Se pide desarrollar un programa en Python controlado por un menú de
# opciones, en el que se incluyan como mínimo dos módulos, para permita gestionar las siguientes tareas:

class Juicios:
    def __init__(self, expediente, descripcion, tipo, nombre, monto):
        self.expediente = expediente
        self.descripcion = descripcion
        self.tipo = tipo
        self.nombre = nombre
        self.monto = monto

    def __str__(self):
        return 'Expediente: ' + str(self.expediente) + ' | Descripcion: ' + str(self.descripcion) + ' | Tipo: ' + str(self.tipo) + \
            ' | Nombre: ' + str(self.nombre) + ' | Monto: ' + str(self.monto)
