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


