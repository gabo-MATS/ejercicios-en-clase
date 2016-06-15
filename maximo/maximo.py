def maximo (l):
	if len(l) == 1:
		return l[0]
	
	sublista = l[1:]
	submaximo = maximo(sublista)

	if l[0] > submaximo:		
		return l[0]
	return submaximo	 
	
