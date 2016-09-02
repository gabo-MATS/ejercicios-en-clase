class Robot(object):
	def __init__(self,x,y):
		self.direccion="^"
		self.x=x
		self.y=y
		self.fichas=0
		self.mapa= None

	def colocar_en_mapa(self,mapa):
		pass	
	def move(self):
		if self.direccion==">" and self.x<ancho:
			self.x+=1	
		if self.direccion=="v" and self.y<alto:
			self.y+=1
		if self.direccion=="<" and self.x>0:
			self.x-=1
		if self.direccion=="^" and self.y>0:
			self.y-=1				
	def rotate(self):
		if self.direccion=="^":
			self.direccion=">"
		if self.direccion==">":
			self.direccion="v"
		if self.direccion=="v":
			self.direccion="<"
		if self.direccion=="<"
			self.direccion="^"		
		return self.direccion				
	def pick(self,x,y):
		if self.x==x and self.y==y:
			self.fichas+=1

# ^=90 <=180 >= 0  v=270