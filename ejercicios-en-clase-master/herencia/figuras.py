from cuadrado import Cuadrado 
from triangulo import Triangulo 
figura =None
print ("1.crear figura\n2.salir")
opc2=int(input("que opcion quiere: "))
if opc2==2:
	opc2=4
while opc2!=4:
	if opc2==1:
		figura =None
		figura=int(input("que figura quiere 1.triangulo o 2.cuadrado"))
		if figura==1:
			altura=int(input("ingrese la altura: "))
			base=int(input("ingrese la base: "))
			figura_escogida=Triangulo(base,altura)
		if figura==2:
			lado=int(input("ingrese el lado: "))
			figura_escogida=Cuadrado(lado)	
	if opc2==2:
		print ("area: ", figura_escogida.calcular_area())
	if opc2==3:
		print (figura_escogida.imprimir())	
	print ("1.crear figura\n2.mostrar area\n3.imprimir\n4.salir")
	opc2=int(input("que opcion quiere: "))	
print("gracias")			


