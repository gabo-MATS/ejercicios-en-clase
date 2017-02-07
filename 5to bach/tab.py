import request


class Tab (object)
	def __init__(self,URL,nombre):
		self.URL=URL
		self.nombre=nombre


	def descargar_URL(self,URL):
		r = request.get(URL)
		r.status_code
		r.body

		
    def creartxt():
        archi=open('url.txt','w')
        archi.close()

    def grabartxt():
        archi=open('url.txt','a')
        archi.write(URL)
        archi.close()
    def leertxt():
        archi=open('url.txt','r')
        linea=archi.readline()
        while linea!="":
            print linea
            linea=archi.readline()
        archi.close()           
		
	

		

