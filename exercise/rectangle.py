from point import Point
class Rectangle:
	"""repsents a Rectangle"""
	
	def find_center(self):
		p = Point()
		p.x = self.corner.x + self.width/2
		p.y = self.corner.y + self.height/2
		return p
