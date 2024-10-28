import Shape as s
pi = 22/7
total_area = 0
def combine_shape():
    def rectangle(name):
        # converting all characters
        # into lower cases
        name = name.lower()

        l = int(input("Enter rectangle's length : "))
        b = int(input("Enter rectangle's breadth: "))

        # calculate area of rectangle
        rect_area = s.rectangle(l,b)
        print(f"The area of rectangle is : {rect_area}.")

        #  add or substitute the area
        global total_area
        i = int(input("If you want to add enter 1 or not enter 0 :"))
        if i == 1 :
            total_area = total_area + rect_area
        elif i == 0:
            total_area = total_area - rect_area
            
    def square(name):

        # converting all characters
        # into lower cases
        name = name.lower()
            
        a = int(input("Enter square's side length: "))
               
        # calculate area of square
        sqt_area = s.square(a)
        print(f"The area of square is : {sqt_area}.")

        #  add or substitute the area
        global total_area
        i = int(input("\nIf you want to add enter 1 or not enter 0 :"))
        if i == 1 :
            total_area = total_area + sqt_area
        elif i == 0:
            total_area = total_area - sqt_area
        

    def triangle(name):
            
        # converting all characters
        # into lower cases
        name = name.lower()

        h = int(input("Enter triangle's height length : "))
        b = int(input("Enter triangle's breadth length: "))
               
        # calculate area of triangle
        tri_area = s.triangle(b,h)
        print(f"The area of triangle is : {tri_area}.")

        #  add or substitute the area
        global total_area
        i = int(input("\nIf you want to add enter 1 or not enter 0 :"))
        if i == 1 :
            total_area = total_area + tri_area
        elif i == 0:
            total_area = total_area - tri_area
       

    def circle(name):

        # converting all characters
        # into lower cases
        name = name.lower()

        r = int(input("Enter circle's radius length : "))
                 
        # calculate area of circle
        circ_area = s.circle(r)
        print(f"The area of circle is : {circ_area}.")

        #  add or substitute the area
        global total_area
        i = int(input("\nIf you want to add enter 1 or not enter 0 :"))
        if i == 1 :
            total_area = total_area + circ_area
        elif i == 0:
            total_area = total_area - circ_area
    def half_circle(name):

        # converting all characters
        # into lower cases
        name = name.lower()

        r = int(input("Enter circle's radius length : "))
                 
        # calculate area of circle
        circ_area = s.half_circle(r)
        print(f"The area of circle is : {circ_area}.")

        #  add or substitute the area
        global total_area
        i = int(input("\nIf you want to add enter 1 or not enter 0 :"))
        if i == 1 :
            total_area = total_area + circ_area
        elif i == 0:
            total_area = total_area - circ_area
        

    y = int(input("\nHow many shapes in our combine shape :"))
    for i in range(0,y):
        shape_name = input("\nEnter the name of shape : ")
        if shape_name =="rectangle":
            rectangle(shape_name)

        elif shape_name =="square":
            square(shape_name)
                    
        elif shape_name =="triangle":
            triangle(shape_name)

        elif shape_name =="circle":
            circle(shape_name)
        elif shape_name =="half circle":
            half_circle(shape_name)
                   
        else:
            print("Please enter the correct shape name")

    print(f"The total area of the Combine shape is : {total_area}")

    
    
                

        
        
            
          



        

        
        
            

    

    

    
