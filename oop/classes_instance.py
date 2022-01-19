# my first class
class MyFirstClass:
    pass
    
    #calling the function....
    
a = MyFirstClass()
 print(a)
 '''
 returns// <__main__.MyFirstClass object at 0xb7b7faec> //on my terminal

this shows a was instantiated from the class. 
 '''
 
 #adding attributes using dit notaion directly
 
class Point:
    pass
    
    
p1 = Point()
p2 = Point()
p1.x = 5
p1.y = 4
p2.x = 3
p2.y = 6
print(p1.x, p1.y)
print(p2.x, p2.y)

'''
returns //
5 4
3 6   //

an empty class is created with no behavior or data and later assigned 2 instances.
The syntax use here was <object>.<attribute> = <value>.
'''

#completing the point example

import math
class Point:
"Represents a point in two-dimensional geometric coordinates"
    def __init__(self, x=0, y=0):
		"""Initialize the position of a new point. The x and y
		coordinates can be specified. If they are not, the
		point defaults to the origin."""
		self.move(x, y)

	def move(self, x, y):
		"Move the point to a new location in 2D space."
		self.x = x
		self.y = y

	def reset(self):
		"Reset the point back to the geometric origin: 0, 0"
		self.move(0, 0)

	def calculate_distance(self, other_point):
		"""Calculate the distance from this point to a second
		point passed as a parameter.
		This function uses the Pythagorean Theorem to calculate
		the distance between the two points. The distance is
		returned as a float."""
		return math.sqrt(
		(self.x - other_point.x) ** 2
		+ (self.y - other_point.y) ** 2
		)


#Up comming exercise.
