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

"""
Question 1: Generate pairs from two nested loops such that their sum is even.
"""
def calculate_even_sum():
    my_list = [(x,y) for x in [1,2,3] for y in [3,4,5] if (x + y)%2==0]
    print(my_list)
calculate_even_sum()

"""
Question 2: Find the count of repeating words in a text.
"""
text = "apple banana apple orange banana apple"
my_dict = {w: text.split().count(w) for w in set(text.split())}
print(my_dict)