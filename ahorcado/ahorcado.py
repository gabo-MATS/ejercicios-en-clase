from palabras import palabra
from gano import gano 

print ("bienvenidos")
j="si"
gano=False
v=" "
while j == "si" :
	w=palabra()
	sumaw=len(w)
	pal=list(palabra)
	while gano != "si" and gano != "no" :
		print ("_ "*sumaw)
		l=input ("ingrse una letra: ")
		gano=gano(res)
		print (v)

	j=input("desea seguir jugando: ")	

