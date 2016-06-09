# autor : gabriel martinez
print("1.crear estudiante \n 2.ingresar notas \n 3.reporte de notas \n 4. salir")
opc=int(input("ingrese que opcion quiere :  "))
estudiantes = {}
while opc != 4:
	if opc == 1:
		n=input("ingrese el estudiante: ")
		estudiantes[n]=[]
		print (estudiantes)
		print("1.crear estudiante \n 2.ingresar notas \n 3.reporte de notas \n 4. salir")
		opc=int(input("ingrese que opcion quiere :  "))	
	if opc == 2:
		estu=input (" a que estudiante le quiere ingresar la nota:  ")
		opc2 = "si"
		while opc2 == "si":
			nota=int(input("ingrese la nota: "))
			while nota <= 0 or nota >= 101:
				nota=int( input("ingrese la nota: ") )
			estudiantes[estu].append(nota)
			print (estudiantes)
			opc2=input("quiere ingresar otra nota al mismo estudiante  :  ")
		print("1.crear estudiante \n 2.ingresar notas \n 3.reporte de notas \n 4. salir")
		opc=int(input("ingrese que opcion quiere :  "))
	if opc == 3: 
		estu=input (" el reporte de que estudiante quiere ver:  ")	
		prom = sum(estudiantes[estu])/len(estudiantes[estu])
		print (estudiantes[estu] )
		print(prom)
		print("1.crear estudiante \n 2.ingresar notas \n 3.reporte de notas \n 4. salir")
		opc=int(input("ingrese que opcion quiere :  "))	
	
print ("gracias")