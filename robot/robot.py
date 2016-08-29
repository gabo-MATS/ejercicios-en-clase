class Robot(object):
	def __init__(self,x,y):
		self.direccion=90
		self.x=x
		self.y=y
		self.fichas=0
		self.mapa= None

	def colocar_en_mapa(self,mapa):
		pass	
	def move(self):
		if self.direccion==0 and self.x<80:
			self.x+=1	
		if self.direccion==90 and self.y<25:
			self.y+=1
		if self.direccion==180 and self.x>0:
			self.x-=1
		if self.direccion==270 and self.y>0:
			self.y-=1				
	def rotate(self):
		self.direccion-=90
		if self.direccion <0:
			self.direccion=270
		if self.direccion==0:
			robot=">"
			return robot
		if self.direccion==270:
			robot="v"
			return robot
			robot="<"
		if self.direccion==180:
			return robot
		if self.direccion==90:
			robot="^"
			return robot				
	def pick(self):
		self.fichas+=1


print (Robot.rotate(robot))
print (Robot.rotate)
print (Robot.rotate)
print (Robot.rotate)
print (Robot.rotate)
print (Robot.rotate)
print (Robot.rotate)
print (Robot.rotate)
print (Robot.rotate)
print (Robot.rotate)
print (Robot.rotate)
print (Robot.rotate)
print (Robot.rotate)
print (Robot.rotate)
print (Robot.rotate)
print (Robot.rotate)
# ^=90 <=180 >= 0  v=270