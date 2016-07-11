print ("bienvenidos")
l= [["a","b","c"],
	["d","e","f"],
	["g","h","i"]
	]
w = 0	
while w!=True:	
	print (l[0])
	print (l[1])
	print (l[2]) 
	s=str(input("ingrese pocision jugador 1 : "))
	if s=="a":
		l[0][0]="X"
	if s=="b":
		l[0][1]="X"
	if s=="c":
		l[0][2]="X"
	if s=="d":
		l[1][0]="X"
	if s=="e":
		l[1][1]="X"
	if s=="f":
		l[1][2]="X"
	if s=="g":
		l[2][0]="X"
	if s=="h":
		l[2][1]="X"	
	if s=="i":
		l[2][2]="X"
	if l[0][0]=="X" and l[0][1]=="X" and l[0][2]=="X":
		print ("jugador 1 gano") 	
		w=True
	if l[1][0]=="X" and l[1][1]=="X" and l[1][2]=="X":
		print ("jugador 1 gano") 	
		w=True	
	if l[2][0]=="X" and l[2][1]=="X" and l[2][2]=="X":
		print ("jugador 1 gano") 	
		w=True
	if l[0][0]=="X" and l[1][0]=="X" and l[2][0]=="X":
		print ("jugador 1 gano") 	
		w=True		
	if l[0][1]=="X" and l[1][1]=="X" and l[2][1]=="X":
		print ("jugador 1 gano") 	
		w=True
	if l[0][2]=="X" and l[1][2]=="X" and l[2][2]=="X":
		print ("jugador 1 gano") 	
		w=True	
	if l[0][0]=="X" and l[1][1]=="X" and l[2][2]=="X":
		print ("jugador 1 gano") 	
		w=True
	if l[0][2]=="X" and l[1][1]=="X" and l[2][0]=="X":
		print ("jugador 1 gano") 	
		w=True	
	if w != True:	
		print (l[0])
		print (l[1])
		print (l[2]) 
		s=str(input("ingrese pocision jugador 2 : "))
		if s=="a":
			l[0][0]="O"
		if s=="b":
			l[0][1]="O"
		if s=="c":
			l[0][2]="O"
		if s=="d":
			l[1][0]="O"
		if s=="e":
			l[1][1]="O"
		if s=="f":
			l[1][2]="O"
		if s=="g":
			l[2][0]="O"
		if s=="h":
			l[2][1]="O"	
		if s=="i":
			l[2][2]="O"
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