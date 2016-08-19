def cargar_mapa(mapa):
	mapa_final = []
	f = open(mapa, "r")
	
	for line in f:
		mapa_final.append(list(line.strip()))

	return mapa_final

mi_mapa = cargar_mapa("mapas/mapa1.txt")
print (mapa_final)
