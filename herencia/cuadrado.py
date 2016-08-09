from fig import FiguraGeometrica
#un cuadrado es una figura geometrica  
class cuadrado(FiguraGeometrica) :
	def __init__(self,lado):
		super().__init__(lado,lado) 
	def imprimir (self):
		return " "
		for i in range(self.altura):
			resultado += "* " * (self.base)+"\n" 
		return resultado