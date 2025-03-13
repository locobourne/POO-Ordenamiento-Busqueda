class Estadistica:
    def __init__(self, codigoid, nombremp, cantpiezas, piezatipo, piezacosto):
        self.codigoid = codigoid
        self.nombremp = nombremp
        self.cantpiezas = cantpiezas
        self.piezatipo = piezatipo
        self.piezacosto = piezacosto

    def __str__(self):
        return 'Codigo: ' + str(self.codigoid) +' || Nombre: ' + str(self.nombremp)  + ' || Cantidad: ' + str(self.cantpiezas) + \
            ' || Tipo: ' + str(self.piezatipo) + ' || Costo: $' + str(self.piezacosto)
        #return res

