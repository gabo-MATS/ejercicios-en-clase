
import sys,random
cantidad=int(sys.argv[1])
longitud=int(sys.argv[2])
i=0
j=0
letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]
passwords={}
password=[]
while i <= cantidad :
	while j<= longitud :
		random.shuffle(letras)
		l=letras[1]
		password.append(l)
		password.join()
	passwords=pasword

print(passwords)		

