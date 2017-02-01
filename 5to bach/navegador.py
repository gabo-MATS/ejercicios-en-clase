class Navegador(object):
	def __init__ (self,nombre,version):
		self.tabs=[]
		self.nombre=nombre
		self.version=version

	def agregar_tab(self, url,nombre):
		tab =Tab(url,nombre)	
		self.tabs.append(tab)
	def cerrar_tab (self,ctab,tabs):
		ctab-=1
		self.tabs.pop[ctab]		
	def cerrar_tabs(self,tabs):
		self.tabs=[] 
	def mostrar_tabs(self),tabs:
					
