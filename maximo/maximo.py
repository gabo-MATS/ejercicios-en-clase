def maximo (l,n):
	if l[n]>l[n+1]:
		res=l[n]		
	return res>maximo(l,n) 
	
