from fig import FiguraGeometrica
#un cuadrado es una figura geometrica  
class Cuadrado(FiguraGeometrica) :
	def __init__(self,lado):
		super().__init__(lado,lado) 
	def imprimir (self):
		resultado=""
		for i in range(self.altura):
			resultado += "* " * (self.base)+"\n" 
		return resultado