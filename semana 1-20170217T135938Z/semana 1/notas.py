from promedio import prome
ingresa="si"
prom=0
notas=0
nota=0
while ingresa == "si":
	
	nota=int(input("ingrese nota : "))
	if nota >100:
		print ("la nota esta fuera de rango")
		nota=int(input("ingrese nota : "))
	if nota <=100:
		prom+=nota
	notas+=1		
	ingresa=input("quiere ingresar otra nota: ")	
promedio=prome(notas,prom)	
print (promedio)		

