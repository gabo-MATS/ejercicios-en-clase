from funtotito import marca
l= [["a","b","c"],
	["d","e","f"],
	["g","h","i"]
	]
print (l[0])
print (l[1])
print (l[2]) 
s=input ("ingrese pocision:")
if s=="a":
	m=l[0][0]
if s=="b":
	m=l[0][1]
if s=="c":
	m=l[0][2]
if s=="d":
	m=l[1][0]
if s=="e":
	m=l[1][1]
if s=="f":
	m=l[1][2]
if s=="g":
	m=l[2][0]
if s=="h":
	m=l[2][1]	
if s=="i":
	m=l[2][2]
print (m)
res=marca(l,m)
print (res)
print (l[0])
print (l[1])
print (l[2]) 