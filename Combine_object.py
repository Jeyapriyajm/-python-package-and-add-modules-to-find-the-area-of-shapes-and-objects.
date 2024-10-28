import Shape as s
import object as o
pi = 22/7
total_area = 0
def combine_object():
    name = input("Enter the 1 st object :")
    name2 = input("Enter the 2 nd object :")
    name = name.lower()
    name2 = name2.lower()

    #combine cone and cube
        
    if ((name == "cone" and name2 =="cube" )or (name=="cube" and name2 =="cone")):
        a = int(input("\nEnter lenght of the edge : "))
        cube_one= s.square(a)
        cube_areas = o.cube(a)- s.square(a)

        r = int(input("Enter the radius of the circular base: "))
        l = int(input("Enter slant height of the cone       : "))

        circle = s.circle(r)
        cone_areas =  o.cone(r,l) - s.circle(r) 

        if circle > cube_one:
            total_area = (circle - cube_one)+ cube_areas + cone_areas
            
        else:
            total_area = (cube_one - circle)+ cube_areas + cone_areas

        print(f"The total area of combine object is {total_area}")

    #combine cuboid and cone
        
    elif((name == "cuboid" and name2 =="cone" )or (name=="cone" and name2 =="cuboid")):
        a = int(input("Enter the length of the cuboid :"))
        b = int(input("Enter the height of the cuboid :"))
        c = int(input("Enter the width of the cuboid  :"))

        one_side =s.rectangle(a,b)
        cuboid_area =o.rectangular_prism(a,b,c)- s.rectangle(a,b)

        r = int(input("Enter the radius of the circular base: "))
        l = int(input("Enter slant height of the cone       : "))

        circle = s.circle(r)
        cone_areas =o.cone(r,l)- s.circle(r)

        if circle > one_side :
            total_area = (circle - one_side)+ cone_areas + cuboid_area
        else:
            total_area = (one_side - circle)+cone_areas + cuboid_area

        print(f"The total area of combine object is {total_area}")

    #combine cuboid and cube

    elif((name == "cuboid" and name2 =="cube" )or (name=="cube" and name2 =="cuboid")):
        a = int(input("\nEnter lenght of the edge : "))
        cube_one= s.square(a)
        cube_areas = o.cube(a) - s.square(a)

        a = int(input("Enter the length of the cuboid :"))
        b = int(input("Enter the height of the cuboid :"))
        c = int(input("Enter the width of the cuboid  :"))

        one_side =s.rectangle(a,b)
        cuboid_area =o.rectangular_prism(a,b,c)- s.rectangle(a,b)
        if one_side > cube_one:
            total_area = (one_side - cube_one)+ cube_areas + cuboid_area
        else:
            total_area = (cube_one - one_side)+ cube_areas + cuboid_area

        print(f"The total area of combine object is {total_area}")

    #combine cuboid and cone
        
    elif((name == "cuboid" and name2 =="cone" )or (name=="cone" and name2 =="cuboid")):
        r = int(input("Enter the radius of the circular base: "))
        l = int(input("Enter slant height of the cone       : "))

        circle = s.circle(r)
        cone_areas =o.cone(r,l)- s.circle(r)

        a = int(input("Enter the length of the cuboid :"))
        b = int(input("Enter the height of the cuboid :"))
        c = int(input("Enter the width of the cuboid  :"))

        one_side =s.rectangle(a,b)
        cuboid_area =o.rectangular_prism(a,b,c)- s.rectangle(a,b)
        
        if one_side > circle:
            total_area = (one_side - circle)+ cone_areas + cuboid_area
        else:
            total_area = (circle - one_side)+ cone_areas + cuboid_area

        print(f"The total area of combine object is {total_area}")

    #combine cone and pyramid
        
    elif((name == "pyramid" and name2 =="cone" )or (name=="cone" and name2 =="pyramid")):
        r = int(input("Enter the radius of the circular base: "))
        l = int(input("Enter slant height of the cone       : "))

        circle = s.circle(r)
        cone_areas =o.cone(r,l)- s.circle(r)

        a = int(input("Enter the length of the base square :"))
        b = int(input("Enter the height of the pyramid triangle :"))

        base = s.square(a)
        other_side = o.pyramid(a,b)- s.square(a)
        
        if base > circle:
            total_area = (base - circle)+ cone_areas + other_side
        else:
            total_area = (circle - base)+ cone_areas + other_side

        print(f"The total area of combine object is {total_area}")

    #combine cone and sphere
        
    elif((name == "sphere" and name2 =="cone" )or (name=="cone" and name2 =="sphere")):
        c = int(input("Enter the redius of the sphere"))
        sphere_area = o.sphere(c)
        r = int(input("Enter the radius of the circular base: "))
        l = int(input("Enter slant height of the cone       : "))
        cone_area = o.cone(r,l)
        total_area = sphere_area + cone_area
        print(f"The total area of combine object is {total_area}")

    #combine hemisphere and cone

    elif((name == "hemisphere" and name2 =="cone" )or (name=="cone" and name2 =="hemisphere")):
        r = int(input("Enter the radius of the circular base: "))
        l = int(input("Enter slant height of the cone       : "))

        circle = s.circle(r)
        cone_areas =o.cone(r,l)- s.circle(r)

        c = int(input("Enter the radius of the hemisphere : "))

        circle1 = s.circle(c)
        other_area = o.hemisphere(c) - s.circle(c)
        
        if circle1 > circle:
            total_area = (circle1 - circle)+ cone_areas + other_area
        else:
            total_area = (circle - circle1)+ cone_areas + other_area

        print(f"The total area of combine object is {total_area}")

    #combine cone and cylinder
        

    elif((name == "cone" and name2 =="cylinder" )or (name=="cylinder" and name2 =="cone")):
        r = int(input("Enter the radius of the circular base of cone: "))
        l = int(input("Enter slant height of the cone       : "))

        circle = s.circle(r)
        cone_areas =o.cone(r,l)- s.circle(r)

        c = int(input("Enter the radius of cylinder's the circular base : "))
        h = int(input("Enter height of the cylinder         : "))

        circle1 = s.circle(c)
        other_side= o.cylinder(c,h) - s.circle(c)

        if circle1 > circle:
            total_area = (circle1 - circle)+ cone_areas + other_side
        else:
            total_area = (circle - circle1)+ cone_areas + other_side

        print(f"The total area of combine object is {total_area}")

    #combine cube and pyramid

    elif ((name == "pyramid" and name2 =="cube" )or (name=="cube" and name2 =="pyramid")):
        a = int(input("\nEnter lenght of the edge : "))
        cube_one= s.square(a)
        cube_areas = o.cube(a)- s.square(a)

        a = int(input("Enter the length of the base square :"))
        b= int(input("Enter the height of the pyramid triangle :"))

        base = s.square(a)
        other_side = o.pyramid(a,b)- s.square(a)
        
        if base > cube_one:
            total_area = (base - cube_one)+ cube_areas + other_side
        else:
            total_area = (cube_one - base)+ cube_areas + other_side

        print(f"The total area of combine object is {total_area}")

    #combine cube and sphere
    elif((name == "sphere" and name2 =="cube" )or (name=="cube" and name2 =="sphere")):
        a = int(input("Enter the lenght of the edge :"))
        cube_area =o.cube(a)

        c = int(input("Enter the radius of the sphere"))
        sphere_area = o.sphere(c)
        total_area = cube_area + sphere_area

        print(f"The total area of combine object is {total_area}")

    #combine cube and hemisphere


    elif((name == "hemisphere" and name2 =="cube" )or (name=="cube" and name2 =="hemisphere")):
        a = int(input("\nEnter lenght of the edge : "))
        cube_one= s.square(a)
        cube_areas = o.cube(a)- s.square(a)

        c = int(input("Enter the radius of the hemisphere : "))

        circle1 = s.circle(c)
        other_area = o.hemisphere(c) - s.circle(c)
        
        if circle1 > cube_one:
            total_area = (circle1 - cube_one)+ cube_areas + other_area
        else:
            total_area = (cube_one - circle1)+ cube_areas + other_area

        print(f"The total area of combine object is {total_area}")

    #combine cube and cylinder

    elif((name == "cube" and name2 =="cylinder" )or (name=="cylinder" and name2 =="cube")):
        a = int(input("\nEnter lenght of the edge : "))
        cube_one= s.square(a)
        cube_areas = o.cube(a)- s.square(a)

        c = int(input("Enter the radius of cylinder's the circular base : "))
        h = int(input("Enter height of the cylinder         : "))

        circle1 = s.circle(c)
        other_side= o.cylinder(c,h) - s.circle(c)

        if circle1 > cube_one:
            total_area = (circle1 - cube_one)+ cube_areas + other_side
        else:
            total_area = (cube_one - circle1)+ cube_areas + other_side

        print(f"The total area of combine object is {total_area}")

    #combine cuboid and pyramid

    elif ((name == "pyramid" and name2 =="cuboid" )or (name=="cuboid" and name2 =="pyramid")):
        a = int(input("Enter the length of the cuboid :"))
        b = int(input("Enter the height of the cuboid :"))
        c = int(input("Enter the width of the cuboid  :"))

        one_side =s.rectangle(a,b)
        cuboid_area =o.rectangular_prism(a,b,c)- s.rectangle(a,b)

        a = int(input("Enter the length of the base square :"))
        b = int(input("Enter the height of the pyramid triangle :"))

        base = s.square(a)
        other_side = o.pyramid(a,b)- s.square(a)
        
        if base > one_side:
            total_area = (base - one_side)+ cuboid_area + other_side
        else:
            total_area = (one_side - base)+ cuboid_area + other_side

        print(f"The total area of combine object is {total_area}")

    #combine cuboid and sphere

    elif ((name == "sphere" and name2 =="cuboid" )or (name=="cuboid" and name2 =="sphere")):
        a = int(input("Enter the length of the cuboid :"))
        b = int(input("Enter the height of the cuboid :"))
        c = int(input("Enter the width of the cuboid  :"))
        cuboid_area =o.rectangular_prism(a,b,c)
        r = int(input("Enter the radius of the sphere"))
        sphere_area = o.sphere(r)
        total_area = cuboid_area + sphere_area

        print(f"The total area of combine object is {total_area}")

    #combine cuboid and hemisphere

    elif((name == "hemisphere" and name2 =="cuboid" )or (name=="cuboid" and name2 =="hemisphere")):
        a = int(input("Enter the length of the cuboid :"))
        b = int(input("Enter the height of the cuboid :"))
        c = int(input("Enter the width of the cuboid  :"))

        one_side =s.rectangle(a,b)
        cuboid_area =o.rectangular_prism(a,b,c)- s.rectangle(a,b)

        r = int(input("Enter the radius of the hemisphere : "))

        circle1 = s.circle(r)
        other_area = o.hemisphere(r) - s.circle(r)
        
        if circle1 > one_side:
            total_area = (circle1 - one_side)+ cuboid_area + other_area
        else:
            total_area = (one_side - circle1)+ cuboid_area + other_area

        print(f"The total area of combine object is {total_area}")

    #combine cuboid and cylinder

    elif((name == "cuboid" and name2 =="cylinder" )or (name=="cylinder" and name2 =="cuboid")):
        a = int(input("Enter the length of the cuboid :"))
        b = int(input("Enter the height of the cuboid :"))
        c = int(input("Enter the width of the cuboid  :"))

        one_side =s.rectangle(a,b)
        cuboid_area =o.rectangular_prism(a,b,c)- s.rectangle(a,b)

        c = int(input("Enter the radius of cylinder's the circular base : "))
        h = int(input("Enter height of the cylinder         : "))

        circle1 = s.circle(c)
        other_side= o.cylinder(c,h) - s.circle(c)

        if circle1 > one_side:
            total_area = (circle1 - one_side)+ cuboid_area + other_side
        else:
            total_area = (one_side - circle1)+ cuboid_area + other_side

        print(f"The total area of combine object is {total_area}")

    #combine pyramid and sphere

    elif ((name == "sphere" and name2 =="pyramid" )or (name=="pyramid" and name2 =="sphere")):
        a = int(input("Enter the length of the base square :"))
        b = int(input("Enter the height of the pyramid triangle :"))
        pyramid_area =o.pyramid(a,b)
        r = int(input("Enter the radius of the sphere"))
        sphere_area = o.sphere(r)
        total_area = pyramid_area + sphere_area

        print(f"The total area of combine object is {total_area}")    

    #combine pyramid and cylinder
        
    elif((name == "pyramid" and name2 =="cylinder" )or (name=="cylinder" and name2 =="pyramid")):
        a = int(input("Enter the length of the base square :"))
        b = int(input("Enter the height of the pyramid triangle :"))

        base = s.square(a)
        other_side = o.pyramid(a,b)- s.square(a)
        
        c = int(input("Enter the radius of cylinder's the circular base : "))
        h = int(input("Enter height of the cylinder         : "))

        circle1 = s.circle(c)
        other_area= o.cylinder(c,h) - s.circle(c)

        if circle1 > base:
            total_area = (circle1 - base)+ other_side + other_area
        else:
            total_area = (base - circle1)+ other_side + other_area

        print(f"The total area of combine object is {total_area}")
        
    #combine hemisphere and cylinder

    elif((name == "hemisphere" and name2 =="cylinder" )or (name=="cylinder" and name2 =="hemisphere")):
        r = int(input("Enter the radius of the hemisphere : "))

        circle1 = s.circle(r)
        other_area = o.hemisphere(r) - s.circle(r)
        
        c = int(input("Enter the radius of cylinder's the circular base : "))
        h = int(input("Enter height of the cylinder         : "))

        circle = s.circle(c)
        other_side= o.cylinder(c,h) - s.circle(c)

        if circle1 > circle:
            total_area = (circle1 - circle)+ other_side + other_area
        else:
            total_area = (circle - circle1)+ other_side + other_area

        print(f"The total area of combine object is {total_area}")

    else:
        print("Sorry! This shape is not available")
        

        
        
        
        
        
        




