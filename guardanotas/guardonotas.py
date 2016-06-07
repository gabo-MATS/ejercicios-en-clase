opc = input("desea ingresar una nota? si o no:  ")
notas=[]
while opc == "si":
	n=int(input("ingrese la nota : "))
	notas.append(n)
	opc = input("desea ingresar una nota? si o no:  ")
misnotas= open("notasguardadas.txt","w")
for n in notas :
	misnotas.write(str(n))
	misnotas.write("\n")
misnotas.close()


