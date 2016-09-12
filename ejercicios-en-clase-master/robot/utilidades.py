mapa_final = []
def cargar_mapa(mapa):	
	f = open(mapa, "r")	
	for line in f:
		mapa_final.append(list(line.strip()))
	return mapa_final


ordenes = []
def cargar_instrucciones(instrucciones):	
	h = open(instrucciones, "r")
	for regla in h:
		ordenes.append(regla.strip())
	return ordenes