'''
    @Author: Ayush Prajapati
    @Date: 25-07-2024
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 25-07-2024
    @Title : Python program to call an external command
'''

import subprocess


def call_external_command(command):
    """
    Description: 
        This function calls an external command using the subprocess module.
    Parameters:
        command: The command to be executed as a string.
    Return:
        str: The output of the command or an error message.
    """
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return f"An error occurred: {e}"


def main():
    command = input("Enter the command to execute: ")
    output = call_external_command(command)
    print(f"Command output:\n{output}")

if __name__ == "__main__":
    main()
