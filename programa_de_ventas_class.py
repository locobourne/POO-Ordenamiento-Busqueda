# Una empresa necesita un programa para procesar todas las ventas que se realizan. De cada Venta se conocen los siguientes datos: número
# de ticket, nombre del cliente, importe total, un código del vendedor (la empresa posee vendedores identificados con un número entero
# entre 1 y 13, ambos incluidos), y un código de producto (identificados con un número entero entre 0 y 7, ambos incluidos). Se desea
# almacenar la información de n ventas en un arreglo de registros de tipo Venta (definir el tipo Venta y cargar n por teclado).
# Se pide desarrollar un programa en Python controlado por un menú de opciones y que posea como mínimo dos módulos, que permita
# gestionar las siguientes tareas:



class empresa:
    def __init__(self, ticket,cliente, importe, codigov, codigop):
        self.ticket = ticket
        self.cliente = cliente
        self.importe = importe
        self.codigov = codigov
        self.codigop = codigop

    def __str__(self):
        return 'Ticket: ' + str(self.ticket) + ' | Cliente: ' + str(self.cliente) + ' | Importe: ' + str(self.importe) + \
            ' | Codigo Vendedor: ' + str(self.codigov) + ' |  Codigo Producto: ' + str(self.codigop)
