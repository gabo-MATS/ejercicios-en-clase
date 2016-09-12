from robot import Robot
from mapa import Mapa
from moneda import Moneda
from utilidades import cargar_mapa,cargar_instrucciones
import time 

mapa_final = []
def cargar_mapa(mapa):	
	f = open(mapa, "r")	
	for line in f:
		mapa_final.append(list(line.strip()))
	return mapa_final
mi_mapa = cargar_mapa("mapas/mapa1.txt")

ordenes = []
def cargar_instrucciones(instrucciones):	
	h = open(instrucciones, "r")
	for regla in h:
		ordenes.append(list(regla.split()))
	return ordenes
reglas = cargar_instrucciones("instrucciones/programa1.txt")

for y  in range(len(mi_mapa)):
	fila = mi_mapa[y]
	for x in range (len(fila)):
		casilla=mi_mapa[y][x]
		if casilla == "*":
			robot(x,y)
		if casilla == "0":
			pass
		if casilla > "0":
			Moneda(x,y)

	
for i in reglas:
	if i=='PICK':
		robot.recoger
	if i=='MOVE':
		robot.move
	if i=='ROTATE':
		robot.rotate 
	print (Mapa(dibujar))	
	time.sleep(0.1)


		


