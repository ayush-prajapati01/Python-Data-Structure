'''
    @Author: Ayush Prajapati
    @Date: 25-07-2024
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 25-07-2024
    @Title : Python program to list all files in a directory
'''

import os

def list_files(directory):
    """
    Description: 
        This function lists all files in a given directory.
    Parameters:
        directory: The path of the directory to list files from.
    Return:
        list: A list of filenames in the directory.
    """
    try:
        return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    except FileNotFoundError:
        print("Directory not found.")
        return []

def main():
    directory = input("Enter the directory path: ")
    files = list_files(directory)
    print(f"Files in '{directory}': {files}")

if __name__ == "__main__":
    main()
