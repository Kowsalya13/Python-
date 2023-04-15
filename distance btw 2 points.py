import math
print("Point1")
X1= int(input("Enter X1 co-ordinate: "))
Y1= int(input("Enter Y1 co-ordinate: "))    
print("Point2")
X2= int(input("Enter X2 co-ordinate: "))
Y2= int(input("Enter Y2 co-ordinate: "))
distance= math.sqrt(((X2-X1)**2)+((Y2-Y1)**2))
print("The distance between two points : ",str(distance))


