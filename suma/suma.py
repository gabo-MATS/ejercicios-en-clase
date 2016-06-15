def suma (l):
	if len(l) == 1:
		return l[0]

	sublista = l[1:]
	submaximo = suma(sublista)


	return l[0]+submaximo	 
	
