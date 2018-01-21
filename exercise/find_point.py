from point import Point 
from rectangle import Rectangle

def find_center(rect):
	point = Point()
	point.x = rect.corner.x + rect.length/2
	point.y = rect.corner.y + rect.width/2
	return point

box = Rectangle()
box.corner = Point()
box.corner.x = 10
box.corner.y = 20
box.length = 200
box.width = 100

