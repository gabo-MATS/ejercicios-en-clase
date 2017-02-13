from tab import Tab
class Navegador(object):
	def __init__ (self,nombre,version):
		self.tabs=[]
		self.nombre=nombre
		self.version=version

	def agregar_tab(self, url,nombre):
		tab =Tab(url,nombre)	
		self.tabs.append(tab)
	def cerrar_tab (self,ctab):
		ctab-=1
		self.tabs.pop[ctab]		
	def cerrar_tabs(self):
		self.tabs=[] 
	def mostrar_tabs(self):
		return self.tabs
	def guardar_tab(self,url):
		Navegador.grabartxt(url)
	def cambiar_tabs(self,n,URL):
		n-=1
		self.tabs[n]=URL

	def creartxt():
		archi=open('url.txt','w')
		archi.close()

	def grabartxt(url):
		archi=open('url.txt','a')
		archi.write(url)
		archi.close()
	def leertxt():
		archi=open('url.txt','r')
		linea=archi.readline()
		while linea!="":
			return linea
			linea=archi.readline()
		archi.close()		
		
					
