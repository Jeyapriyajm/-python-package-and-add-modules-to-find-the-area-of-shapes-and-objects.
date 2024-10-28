pi = 22/7
def cube(a):
    area = 6 * (a**2)
    return area

def rectangular_prism(l,w,h):
    area = 2 * (w*l + h*l + h*w)
    return area

def cylinder(r,h):
    area = 2 * pi * r*(r+h)
    return area
def cone(r,l):
    area = pi * r *(r + l)
    return area

def sphere(r):
    area = 4 * pi * (r**2)
    return area

def hemisphere(r):
    area = 3 * pi * (r**2)
    return area

def pyramid(a,h):
    area = (a**2)+(2 * a * h)
    return area

def cylinder(c,h):
    area = 2* pi *(c**2)+ (2*pi*c*h)
    return area
    















