from palabras import palabra
from gano import ga 
from muñeco import mu
print ("bienvenidos")
j="si"
v=0
while j == "si" :
	w=palabra()
	pal=list(w)
	guiones = []
	gano=False
	v=0
	lu=[]
	for l in w:
			guiones.append(" _")
	while gano != "si" and gano != "no" :
		print ("".join(guiones))	
		l=input ("ingrse una letra: ")
		for i in range (len(w)):
			if pal[i]==l:
				guiones[i]=l
		gano=ga(l,pal)
		if gano == False:
			lu.append(l)
			print ("".join(lu))
			v=v+1
			print (mu(v))
			if v == 7:
				gano = "no"
		if " _"	not in guiones:
			gano ="si"	 		

	if gano == "no":
		print ("perdio") 
	if gano == "si":
		print ("gano!!!!!") 				
	print ("la palabra era : ", w)	
	j=input("desea seguir jugando: ")	
print ("gracias por jugar")
