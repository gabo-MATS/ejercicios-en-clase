from funtotito import gano
print ("bienvenidos")
l= [["a","b","c"],
	["d","e","f"],
	["g","h","i"]
	]
m= [[0,0,0],
	[0,0,0],
	[0,0,0]
	]	
res= 0	
while res!=2 and res!=1 :	
	print (l[0])
	print (l[1])
	print (l[2]) 
	s=input("ingrese pocision jugador 1 : ")
	s_valor=ord(s)-ord("a")
	s_fila=s_valor%3
	s_columna=s_valor//3
	l[s_columna][s_fila]="X"
	m[s_columna][s_fila]=1
	res=gano(m)	
	if res != 1 :	
		print (l[0])
		print (l[1])
		print (l[2]) 
		s=str(input("ingrese pocision jugador 2 : "))
		s_valor=ord(s)-ord("a")
		s_fila=s_valor%3
		s_columna=s_valor//3
		l[s_columna][s_fila]="O"
		m[s_columna][s_fila]=-1
		res=gano(m)


if res ==1:
	print ("gano el jugador 1 !!!!!")	
if res ==2:
	print ("gano el jugador 2!!!!!")		
print (l[0])
print (l[1])
print (l[2]) 