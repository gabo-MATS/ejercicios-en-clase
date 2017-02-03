import request
def creartxt():
    archi=open('html.txt','w')
    archi.close()

def grabartxt():
    archi=open('html.txt','a')
    archi.write('Linea 1\n')
    archi.write('Linea 2\n')
    archi.write('Linea 3\n')
    archi.close()

def leertxt():
    archi=open('html.txt','r')
    linea=archi.readline()
    while linea!="":
        print linea
        linea=archi.readline()
     archi.close()	


class Tab (object)
	def __init__(self,URL,nombre):
		self.URL=URL
		self.nombre=nombre


	def descargar_URL(self,URL):
		r = request.get(URL)
		r.status_code
		r.body
		
		
	

		

