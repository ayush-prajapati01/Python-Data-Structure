'''

    @Author: Ayush Prajapati
    @Date: 25-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 25-07-2024 
    @Title : Python program to accept a user name and to display its reverse
    
'''


def reverse_name(first_name, last_name):
    """
    Description: 
        This function accepts a user's first and last name and returns them in reverse order with a space between them.
    Parameters:
        first_name: The user's first name.
        last_name: The user's last name.
    Return:
        str: The names in reverse order.
    """
    return f"{last_name} {first_name}"


def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    reversed_name = reverse_name(first_name, last_name)
    print(f"Reversed name: {reversed_name}")


if __name__ == "__main__":
    main()
