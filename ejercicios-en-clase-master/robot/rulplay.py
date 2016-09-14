from robot import Robot
from mapa import Mapa
from moneda import Moneda
from utilidades import cargar_mapa,cargar_instrucciones
import time 



mi_mapa = cargar_mapa("mapas/mapa1.txt")
reglas = cargar_instrucciones("instrucciones/programa1.txt")

for y  in range(len(mi_mapa)):
	fila = mi_mapa[y]
	for x in range (len(fila)):
		casilla=mi_mapa[y][x]
		if casilla == "*":
			Robot.dibujar(x,y)
			Mapa.asignar_robot(x,y)
			Robot.asignar_mapa(x,y)
		else:
			Moneda(x,y)

	
for i in reglas:
	if i=='PICK':
		Robot.recoger()
	if i=='MOVE':
		Robot.move()
	if i=='ROTATE':
		Robot.rotate() 
	print (mi_mapa(dibujar))	
	time.sleep(0.1)


		


