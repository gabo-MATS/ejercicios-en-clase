
from navegador import Navegador
from tab import Tab
print (" 1 abrir\n 2 salir del navegador ")

opc = int (input ("que opcion quiere ? "))
if opc==2 :
	opc=9
	
while opc!=9:
	if opc == 1:
		nombre = str(input("ingrese el nombre del navegador"))
		version = str(input("ingrese la version del navegador"))
		navegador=Navegador(nombre, version)

		print (" 1 abrir\n 2 agregar tab \n 3 cambiar tabs \n 4 cerrar tab\n 5 cerrar todos los tabs\n 6 guardar tab\n 7 mostrar tabs\n 8 descargar HTML de tab\n 9 salir del navegador ")
		opc = int (input ("que opcion quiere ? "))
	
	if opc == 2:	
		URL=input("ingrese el url nuevo ")
		nombre = input ("ingrese el nombre del Tab ")

		navegador.agregar_tab(URL,nombre)
		opc = int (input ("que opcion quiere ? "))

	if opc == 3:
		n= int (input("que tab quiere cambiar? "))
		URL = input("ingrese el url nuevo ")
		navegador.cambiar_tabs(n,URL)

		opc = int (input ("que opcion quiere ? "))

	if opc == 4:
		ctab=int (input("que tab quiere cerrar? "))
		navegador.cerrar_tab(ctab)

		opc = int (input ("que opcion quiere ? "))

	if opc == 5:
		navegador.cerrar_tabs()
		opc = int (input ("que opcion quiere ? "))

	if opc == 6:
		url= input("que tab quiere guardar")
		navegador.guadar_tab(url,url)

		opc = int (input ("que opcion quiere ? "))

	if opc == 7:
		print (navegador.mostrar_tabs())

		opc = int (input ("que opcion quiere ? "))

	if opc == 8:
		HTML= input("que tab quiere descargar")
		Tab.descargar_URL(HTML,HTML)

		opc = int (input ("que opcion quiere ? "))		