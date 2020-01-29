"""
Author: Class
Description: This program calculates the year and number of days
past Jan. 1 given some number of days.
"""

DAYS_IN_YEAR = 365
START_YEAR = 2020

def main():
    days = int(input("Enter the number of days that have passed since Jan. 1 2020: "))

    years = days // DAYS_IN_YEAR
    current_year = years + START_YEAR

    days_since_jan_1 = days % DAYS_IN_YEAR

    print("The current year is", current_year)
    print("And it has been", days_since_jan_1, "days since January 1st.")


main()
