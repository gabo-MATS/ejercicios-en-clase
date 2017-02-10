
from navegador import Navegador 
from tab import Tab
print ("1 abrir\n 2 crear tab\n 3 agregar tab\n 4 cerrar tab\n 5 cerrar todos los tabs\n 6 guardar tab\n 7 mostrar tabs\n 8 cambiar tabs\n 9 descargar HTML de tab\n 10 salir del navegador ")

opc = int (input ("que opcion quiere ? "))
	
while opc!=10:
	if opc == 1:
		nombre = str(input("ingrese el nombre del navegador"))
		version = str(input("ingrese la version del navegador"))
		navegador=Navegador(nombre, version)

		opc = int (input ("que opcion quiere ? "))
	
	if opc == 2:	
		URL=input("ingrese el url nuevo ")
		nombre = input ("ingrese el nombre del Tab ")

		navegador.agregar_tab(URL,nombre)
		opc = int (input ("que opcion quiere ? "))

	if opc == 3:

		opc = int (input ("que opcion quiere ? "))

	if opc == 4:

		opc = int (input ("que opcion quiere ? "))

	if opc == 5:
		navegador.cerrar_tabs()
		opc = int (input ("que opcion quiere ? "))

	if opc == 6:

		opc = int (input ("que opcion quiere ? "))

	if opc == 7:
		print (navegador.mostrar_tabs())

		opc = int (input ("que opcion quiere ? "))

	if opc == 8:

		opc = int (input ("que opcion quiere ? "))

	if opc == 9:
		URL= input("que tab quiere guardar")

		opc = int (input ("que opcion quiere ? "))		