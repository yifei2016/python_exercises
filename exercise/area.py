class Area:
	"""represents an area"""
	def compute_area_with_console_input(self):
		print("Enter a number for radius:")
		radius = input()
		area = radius * radius * 3.14159
		print("The area for the circle of radius " + str(radius) + " is " + str(area))
