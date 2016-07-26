from palabras import palabra
from gano import ga 
from muñeco import mu
print ("bienvenidos")
j="si"
gano=False
v=0
while j == "si" :
	w=palabra()
	sumaw=len(w)
	pal=list(w)
	print (w)
	while gano != "si" and gano != "no" :
		print ("_ "*sumaw)
		l=input ("ingrse una letra: ")
		gano=ga(l,pal)
		if gano == False:
			v=v+1
			print (mu(v)) 
				


	j=input("desea seguir jugando: ")	

