'''
    @Author: Ayush Prajapati
    @Date: 25-07-2024
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 25-07-2024
    @Title : Python program to access environment variables
'''

import os

def get_env_variable(variable_name):
    """
    Description: 
        This function retrieves the value of an environment variable.
    Parameters:
        variable_name: The name of the environment variable to retrieve.
    Return:
        str: The value of the environment variable, or a message if not found.
    """
    return os.getenv(variable_name, "Environment variable not found.")


def main():
    variable_name = input("Enter the environment variable name: ")
    value = get_env_variable(variable_name)
    print(f"Value of '{variable_name}': {value}")


if __name__ == "__main__":
    main()
