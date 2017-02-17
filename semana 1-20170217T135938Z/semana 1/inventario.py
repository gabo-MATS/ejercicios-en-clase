
inventario={}
opc=input("quiere ingresar producto ")
while opc== "si":
	productos=input("ingrese producto ")
	ingreso = True
	while ingreso ==True:
		try:	
			cantidad = int(input("ingrese la cantidad "))
			inventario[productos]=cantidad
			ingreso=False
		except :
			print ("INGRESE UNA CANTIDAD VALIDA CON NUMEROS")	
	opc=input("quiere ingresar producto ")

for productos in inventario:
	print (productos,inventario[productos])
