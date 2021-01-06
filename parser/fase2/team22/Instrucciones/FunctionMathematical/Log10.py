import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos import Instruccion3D as c3d
from Optimizador.C3D import Valor as ClassValor
from Optimizador.C3D import OP_ARITMETICO as ClassOP_ARITMETICO
from Optimizador.C3D import Identificador as ClassIdentificador

class Log10(Instruccion):
    def __init__(self, valor, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        arbol.consola.append('Función en proceso...')

    def generar3D(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        code = []
        t0 = c3d.getLastTemporal()
        t1 = c3d.getTemporal()
        code.append(c3d.operacion(t1, ClassIdentificador(t0), ClassValor("\"LOG10(" + str(self.valor.generar3D(tabla, arbol)) + ")\"", "STRING"), ClassOP_ARITMETICO.SUMA))

        return code
'''
instruccion = Log10(10,None, 1,2)

instruccion.ejecutar(None,None)
'''