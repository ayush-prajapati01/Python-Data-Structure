'''

    @Author: Ayush Prajapati
    @Date: 25-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 25-07-2024 
    @Title : Python program to check whether a file exists.
    
'''

import os
    

def check_file_exists(file_path):
    """
    Description:
        This function checks whether a file exists at the given path.
    Parameters:
        file_path: The path to the file to be checked.
    Return:
        bool: True if the file exists, False otherwise.
    """

    return os.path.exists(file_path)



file_path = "8_Histogram.py"
if check_file_exists(file_path):
    print(f"The file {file_path} exist")