from robot import Robot
from mapa import Mapa
from moneda import Moneda
from utilidades import cargar_mapa,cargar_instrucciones
import time 



mi_mapa = cargar_mapa("mapas/mapa1.txt")
reglas = cargar_instrucciones("instrucciones/programa1.txt")

mapa=Mapa(4,8)


for y  in range(len(mi_mapa)):
	fila = mi_mapa[y]
	for x in range (len(fila)):
		casilla=mi_mapa[y][x]
		if casilla == "*":
			robot=Robot(x,y)
			mapa.asignar_robot(robot)
			robot.asignar_mapa(mapa)
		else:
			cantidad = int(casilla)
			for i in range (cantidad):
				moneda=Moneda(x,y)
				mapa.agregar_moneda(moneda)
mon=0
for i in reglas:
	if i=='PICK':
		robot.recoger()
		mon+=1
	if i=='MOVE':
		robot.move()
	if i=='ROTATE':
		robot.rotate() 
	print (mapa.dibujar())	
	print ("Monedas: " , mon)
	time.sleep(1)


		


