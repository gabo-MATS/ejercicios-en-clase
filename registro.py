# autor : gabriel martinez
print("1.crear estudiante \n 2.ingresar notas \n 3.reporte de notas \n 4. salir")
opc=int(input("ingrese que opcion quiere :  "))
estudiantes = {}
while opc != 4:
	if opc == 1:
		n=input("ingrese el estudiante: ")
		estudiantes[n]=[]
	if opc == 2:
		estu=input (" a que estudiante le quiere ingresar la nota:  ")
		nota=int(input("ingrese la nota: "))
		while nota <= 0 and nota >= 100:
			nota=int( input("ingrese la nota: ") )
		estudiantes[estu].append(nota)
	opc=int(input("ingrese que opcion quiere :  "))	
	print (estudiantes)
