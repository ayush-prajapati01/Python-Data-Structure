'''

    @Author: Ayush Prajapati
    @Date: 25-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 25-07-2024 
    @Title : Python program to display Calendar of given month and year
    
'''


import calendar


def print_month_calendar(year, month):
    """
    Description:
        This function prints the calendar for a given month and year.
    Parameters:
        year: The year (as an integer)
        month: The month (as an integer, 1-12)
    Return:
        None
    """
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]
    
    print(f"{month_name} {year}".center(20))
    print("Mo Tu We Th Fr Sa Su")
    

    for week in cal:
        week_str = ""
        for day in week:
            if day == 0:
                week_str += "   "
            else:
                week_str += f"{day:2d} "
        print(week_str)
        

def main():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))
    
    if 1 <= month <= 12:
        print_month_calendar(year, month)
    else:
        print("Invalid month. Please enter a number between 1 and 12.")


if __name__ == "__main__":
    main()