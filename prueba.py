print ("bienvenidos")
l= [["a","b","c"],
	["d","e","f"],
	["g","h","i"]
	]
m =[[0,0,0],
	[0,0,0],
	[0,0,0]
	]	
w = 0	
while w!=True:	
	print (l[0])
	print (l[1])
	print (l[2]) 
	s=input("ingrese pocision jugador 1 : ")
	s_valor=ord(s)-ord("a")
	s_fila=s_valor%3
	s_columna=s_valor//3
	l[s_columna][s_fila]="X"
	m[s_columna][s_fila]=1
	sum(m)
	
	if w != True:	
		print (l[0])
		print (l[1])
		print (l[2]) 
		s=str(input("ingrese pocision jugador 2 : "))
		s_valor=ord(s)-ord("a")
		s_fila=s_valor%3
		s_columna=s_valor//3
		l[s_columna][s_fila]="O"
		m[s_columna][s_fila]=2
		if l[0][0]=="O" and l[0][1]=="O" and l[0][2]=="O":
			print ("jugador 2 gano") 	
			w=True
		if l[1][0]=="O" and l[1][1]=="O" and l[1][2]=="O":
			print ("jugador 2 gano") 	
			w=True	
		if l[2][0]=="O" and l[2][1]=="O" and l[2][2]=="O":
			print ("jugador 2 gano") 	
			w=True
		if l[0][0]=="O" and l[1][0]=="O" and l[2][0]=="O":
			print ("jugador 2 gano") 	
			w=True		
		if l[0][1]=="O" and l[1][1]=="O" and l[2][1]=="O":
			print ("jugador 2 gano") 	
			w=True
		if l[0][2]=="O" and l[1][2]=="O" and l[2][2]=="O":
			print ("jugador 2 gano") 	
			w=True	
		if l[0][0]=="O" and l[1][1]=="O" and l[2][2]=="O":
			print ("jugador 2 gano") 	
			w=True
		if l[0][2]=="O" and l[1][1]=="O" and l[2][0]=="O":
			print ("jugador 2 gano") 	
			w=True				
print (l[0])
print (l[1])
print (l[2]) 