import object as o
def calculate_area_3d(name): 
    pi = 3.14
    # converting all characters
    # into lower case
    name = name.lower()

    # check for the conditions
    
    if name == "cube" :
        a = int(input("Enter lenght of the edge : "))

        # calculate the area 

        cube_area = o.cube(a)
        print(f"The area of cube is : {cube_area}.")



    elif name == "cylinder":
        r = int(input("Enter the radius of the circular base: "))
        h = int(input("Enter height of the cylinder         : "))
        

        #calculate the area 

        cylinder_area = o.cylinder(r,h)
        print(f"The area of cylinder is : {cylinder_area}.")
        
    elif name == "cone":
        r = int(input("Enter the radius of the circular base: "))
        l = int(input("Enter slant height of the cone       : "))
        
        #calculate the area 

        cone_area = o.cone(r,l)
        print(f"The area of cone is : {cone_area}.")

    elif name == "sphere":
        r = int(input("Enter the radius of the sphere : "))

        #calculate the area

        sphere_area = o.sphere(r)
        print(f"The area of sphere is  :  {sphere_area}.")

    elif name == "hemisphere" :
        r = int(input("Enter the radius of the hemisphere : "))

        #calculate the area

        hemisphere_area = o.hemisphere(r)
        print(f"The area of hemisphere is : {hemisphere_area}.")
    elif name== "cuboid" :
        a = int(input("Enter the length of the cuboid :"))
        b = int(input("Enter the height of the cuboid :"))
        c = int(input("Enter the width of the cuboid  :"))

        #calculate the area

        cuboid_area = o.rectangular_prism(a,b,c)
        print(f"The are of cuboid is : {cuboid_area}.")

    elif name== "pyramid" :
        a = int(input("Enter the length of the base square :"))
        b = int(input("Enter the height of the pyramid triangle :"))
        

        #calculate the area

        pyramid_area =o.pyramid(a,b) 
        print(f"The area of pyramid is : {pyramid_area}.")
    else:
        print("Sorry! This shape is not available")
        
