from tab import tab



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
		return self.tabs=[] 
	def mostrar_tabs(self,tabs):
		return self.tabs
	def guardar_tab(self):
		
	def cambiar_tabs(self,tabs):

	def creartxt():
		archi=open('url.txt','w')
		archi.close()

	def grabartxt():
		archi=open('url.txt','a')
		archi.write('Linea 1\n')
		archi.write('Linea 2\n')
		archi.write('Linea 3\n')
		archi.close()
	def leertxt():
		archi=open('url.txt','r')
		linea=archi.readline()
		while linea!="":
			print linea
			linea=archi.readline()
	 	archi.close()		
	 	
					
