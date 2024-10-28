#The main function

import Object_main as ob
import Shape_main as sp
import Combine_shape as cs
import Combine_object as co
import os


os.system("COLOR 9")
print("\t\t..........................."
      "Calculate Area..........................")
print("\n\t01.Calculate Shapes \n"
      "\t02.Calculate Objects\n"
      "\t03.Calculate Combine Shapes and Objects\n")

# Get input from user want to find type of the shape

a = input("\nEnter the menue number :")
a = a.lower()
os.system('cls')
while(a == '1' or a == '2' or a=='3'  and a != 0):
    if a == "1":
        os.system("COLOR A")
        print("\n\t\t..........................."
              "Calculate Area of Shape..........................")
        print("\nShape Names : Rctangle,Square,Triangle,Circle\n")
        shape_name = input("\nEnter the name of the shape : ")
       
        # function calling
        sp.calculate_area(shape_name)
        print("----------------------------------------------------------------------")
        print("\t\t..........................."
          "Calculate Area..........................")
        print("\n\t01.Calculate Shapes \n"
          "\t02.Calculate Objects\n"
          "\t03.Calculate Combine Shapes and Objects\n")
        a = input("\nEnter the menue number :")
        os.system('cls')

    elif a == "2":
        os.system("COLOR B")
        
        print("\n\t\t..........................."
              "Calculate Area of Object..........................")
        print("\nObject Names : Cube,cuboid,cone,sphere,hemisphere,pyramid,cylinder\n")
        shape_name = input("\nEnter the name of shape : ")
       
        # function calling
        ob.calculate_area_3d(shape_name)
        print("---------------------------------------------------------------------\n")
        print("\n\t01.Calculate Shapes\n "
          "\t02.Calculate Objects\n"
          "\t03.Calculate Combine Shapes and Objects\n")
        a = input("\nEnter the menue number :")
        a = a.lower()
        os.system('cls')

    elif a =="3":
        os.system("COLOR E")
        print("\n\tDo you want to combine 2D shape or 3D Object")
        i = input("Enter 2D or 3D :")
        i = i.lower()
        os.system('cls')
        if i == "2d":
            print("\n\t\t..........................."
                  "Calculate Area of Combine Shape..........................")
            print("\nShape Names : Rctangle,Square,Triangle,Circle,Half circle\n")
            cs.combine_shape()
            print("---------------------------------------------------------------------\n")
            
            print("\n\t01.Calculate Shapes\n "
                  "\t02.Calculate Objects\n"
                      "\t03.Calculate Combine Shapes and Objects\n")
            a = input("\nEnter the menue number :")
            os.system('cls')
        elif i == "3d":
            print("\n\t\t..........................."
                  "Calculate Area of Combine Object..........................")
            print("\nObject Names : Cube,cuboid,cone,sphere,hemisphere,pyramid,cylinder\n")
            co.combine_object()
            print("---------------------------------------------------------------------\n")

            print("\n\t01.Calculate Shapes\n"
                "\t02.Calculate Objects\n"
                  "\t03.Calculate Combine Shapes and Objects\n")
            a = input("\nEnter the menue number :")
            os.system('cls')
            

    else:
        os.system("COLOR E")
        #If the condition is false display an error message and get the input again 
        print("Sorry your decision is not found!")
        print("\n\t01.Calculate Shapes\n"
                "\t02.Calculate Objects\n"
                  "\t03.Calculate Combine Shapes and Objects\n")
        a = input("\nEnter the menue number :")
        
        os.system('cls')
