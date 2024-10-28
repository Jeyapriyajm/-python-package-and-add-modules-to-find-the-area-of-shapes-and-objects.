
import Shape

def calculate_area(name): \
    # converting all character
    # into lower cases
    name = name.lower()
   
    # check for the conditions
    if name == "rectangle":
        l = int(input("Enter rectangle's length : "))
        b = int(input("Enter rectangle's breadth: "))
     
    # calculate area of rectangle
        rect_area =Shape.rectangle(l,b)
        print(f"The area of rectangle is : {rect_area}.")
   
    elif name == "square":
        s = int(input("Enter square's side length: "))
       
    # calculate area of square
        area =Shape.square(s)
        print(f"The area of square is : {area}.")
 
    elif name == "triangle":
        h = int(input("Enter triangle's height length : "))
        b = int(input("Enter triangle's breadth length: "))
       
    # calculate area of triangle
        area =Shape.triangle(b,h)
        print(f"The area of triangle is : {area}.")
 
    elif name == "circle":
        r = int(input("Enter circle's radius length : "))
         
    # calculate area of circle
        circ_area = Shape.circle(r)
        print(f"The area of circle is  : {circ_area}.")
         
   
    else:
        print("Sorry! This shape is not found!")
 

