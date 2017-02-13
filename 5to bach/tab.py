import requests


class Tab (object):
    def __init__(self,URL,nombre):
        self.URL=URL
        self.nombre=nombre


    def descargar_URL(self,HTML):
        htm = requests.get(HTML)
        htm.headers
        Tab.grabartxt(htm)

        
    def creartxt():
        archi=open('html.txt','w')
        archi.close()

    def grabartxt(htm):
        archi=open('html.txt','a')
        archi.write(htm ,"\n")
        archi.close()
    def leertxt():
        archi=open('html.txt','r')
        linea=archi.readline()
        while linea!="":
            return linea
            linea=archi.readline()
        archi.close()       
        
    

        

