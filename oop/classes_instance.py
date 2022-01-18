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


