from palabras import palabra
from gano import gano 
from muñeco import mu
print ("bienvenidos")
j="si"
gano=False
v=" "
p=palabra()
while j == "si" :
	w=palabra()
	sumaw=len(w)
	pal=list(p)
	while gano != "si" and gano != "no" :
		print ("_ "*sumaw)
		l=input ("ingrse una letra: ")
		gano=gano(l,pal)
		print (v)
		if gano == False:
			print (mu)


	j=input("desea seguir jugando: ")	

