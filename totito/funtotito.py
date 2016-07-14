def gano (m):
	sumas=[]
	for j in range (3):
		sumas.append(m[0][j]+m[1][j]+m[2][j])
	for fila in m:
			sumas.append(sum(fila))
			
	d1=0
	d2=0
	for i in range (3):
		d1+=m[i][i]
		d1+=m[i][2-i]
	sumas.append(d1)
	sumas.append(d2)	
	if 	3 in sumas:
		return 1
	elif -3 in sumas:
		return 2
	else : 
		return False		




