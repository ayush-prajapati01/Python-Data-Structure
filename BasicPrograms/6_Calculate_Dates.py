'''

    @Author: Ayush Prajapati
    @Date: 25-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 25-07-2024 
    @Title : Python program to calculate number of days between two dates.
    
'''


from datetime import date


def days_between_dates(date1, date2):
    """
    Description:
        This function calculates the number of days between two dates.
    Parameters:
        date1: A tuple representing the first date (year, month, day)
        date2: A tuple representing the second date (year, month, day)
    Return:
        int: The number of days between the two dates
    """
    d1 = date(date1[0], date1[1], date1[2])
    d2 = date(date2[0], date2[1], date2[2])
    delta = d2 - d1
    return abs(delta.days)


def main():
    print("Enter the first date")
    year1 = int(input("Year: "))
    month1 = int(input("Month(1-12): "))
    day1 = int(input("Day(1-31): "))

    print("\nEnter the second date:")
    year2 = int(input("Year: "))
    month2 = int(input("Month(1-12): "))
    day2 = int(input("Day(1-31): "))

    date1 = (year1, month1, day1)
    date2 = (year2, month2, day2)

    difference = days_between_dates(date1, date2)
    print(f"\nNumber of days between the two dates: {difference} days")


if __name__ == "__main__":
    main()