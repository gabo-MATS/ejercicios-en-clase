from collections import deque

def es_palindromo(l) :
	c=deque()
	p=[]
	for i in l:
		p.append(i)
		c.append(i)
	for i in range (len(l)):
		if c.popleft() != p.pop():
			return False

	return True	












