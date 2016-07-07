from funtotito import gano
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
	s=str(input("ingrese pocision: "))
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
	if l[0][0]and l[0][1]and l[0][2]=="X":
		print ("jugador 1 gano") 	
		w=True
	if l[1][0]and l[1][1]and l[1][2]=="X":
		print ("jugador 1 gano") 	
		w=True	
	if l[2][0]and l[2][1]and l[2][2]=="X":
		print ("jugador 1 gano") 	
		w=True
	if l[0][0]and l[1][0]and l[2][0]=="X":
		print ("jugador 1 gano") 	
		w=True		
	if l[0][1]and l[1][1]and l[2][1]=="X":
		print ("jugador 1 gano") 	
		w=True
	if l[0][2]and l[1][2]and l[2][2]=="X":
		print ("jugador 1 gano") 	
		w=True	
	if l[0][0]and l[1][1]and l[2][2]=="X":
		print ("jugador 1 gano") 	
		w=True
	if l[0][2]and l[1][1]and l[2][0]=="X":
		print ("jugador 1 gano") 	
		w=True		
print (l[0])
print (l[1])
print (l[2]) 