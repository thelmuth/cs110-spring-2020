import math

def main():

    # for cat in range(11):
    #     a = area_of_circle(cat)
    #     print("The area is", a)


    longer_college = longer_string("Hamilton College", "Colgate University")
    print(longer_college)

    longer_animal = longer_string("elephant", "dog")
    print(longer_animal)

def area_of_circle(radius):
    """Calculates the area of a circle."""
    area = math.pi * (radius ** 2)
    return area


def longer_string(string1, string2):
    """Returns the longer of string1 and string2"""
    if len(string1) > len(string2):
        return string1
    else:
        return string2









main()
