'''
    @Author: Ayush Prajapati
    @Date: 25-07-2024
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 25-07-2024
    @Title : Python program to find out the number of CPUs in use
'''

import os


def count_cpus():
    """
    Description: 
        This function returns the number of CPUs in use on the system.
    Return:
        int: The number of CPUs.
    """
    return os.cpu_count()

def main():
    num_cpus = count_cpus()
    print(f"Number of CPUs in use: {num_cpus}")

if __name__ == "__main__":
    main()
