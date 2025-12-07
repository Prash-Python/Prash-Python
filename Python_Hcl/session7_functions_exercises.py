"""
Create modularised functions to calculate the area of geometrical figures.
"""
def area_of_square(side):
    return side * side

def area_of_triangle(base, height):
    return base * height * 0.5

def area_of_rectangle(length, breadth):
    return length * breadth

def area_of_circle(radius):
    return (22 * radius * radius)/7
    

def main():
    print("1. Area of square \n 2. Area of triangle \n 3. Area of rectangle \n 4. Area of circle \n ")
    choice = int(input("Enter the choice: "))
    if choice == 1:
        side = int(input("Enter side for square: "))
        print("Area of square: ", area_of_square(side))
    elif choice == 2:
        base = int(input("Enter base for triangle: "))
        height = int(input("Enter height for triangle: "))
        print("Area of triangle: ", area_of_triangle(base, height))
    elif choice == 3:
        length = int(input("Enter length for rectangle: "))
        breadth = int(input("Enter breadth for rectangle: "))
        print("Area of Rectangle: ", area_of_rectangle(length, breadth))
    else:
        radius = int(input("Enter radius for circle: "))
        print("Area of circle: ", area_of_circle(radius))
main()
