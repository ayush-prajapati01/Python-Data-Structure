'''

    @Author: Ayush Prajapati
    @Date: 30-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 30-07-2024 
    @Title: Python program to print a dictionary in table format.
    
'''


def print_table_from_dict(my_dict):
    """
    Description: 
        This function finds the unique value in the dictionary
    Parameters:
        my_dict: dictionary 
    Return:
        list: Contains unique values
    """
    # Print the names of the columns.
    print("{:^16} {:^16} {:^16}".format('NAME', 'AGE', 'LOCATION'))
    print(f"{'-' * 54}")
    # print each data item.
    for key, value in my_dict.items():
        name, age, location = value
        print("{:^16} {:^16} {:^16}".format(name, age, location))


def main():
    my_dict = {
        1: ["Ayush", 21, 'Sanpada'],
        2: ["Deven", 22, 'Panvel'],
        3: ["Prayag", 22, 'New Panvel'],
        4: ["Shiv", 22, 'Panvel'],
        5: ["Cheems", 2, 'Sanpada']
    }

    print(f"\nThe dictionary in table format is: \n{print_table_from_dict(my_dict)}")


if __name__ == "__main__":
    main()