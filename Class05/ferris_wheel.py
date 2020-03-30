import math

FEET_PER_MILE = 5280

def main():
    height = float(input("Enter the height of the Ferris wheel in feet: "))
    distance = float(input("Enter the distance the ferris wheel has traveled in miles: "))

    # Converting distance to feet and height to circumference
    distance_in_ft = distance * FEET_PER_MILE
    circumference = height * math.pi

    # This calculates the rotations of the Ferris wheel and the
    # distance past the last rotation
    rotations = int(distance_in_ft // circumference)
    feet_past_last_rotation = round(distance_in_ft % circumference)

    print("The ferris wheen rotated", rotations, "times.") # This prints rotations
    print("The outside traveled", feet_past_last_rotation, "feet past the last rotation.")




main()
