'''

    @Author: Ayush Prajapati
    @Date: 25-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 25-07-2024 
    @Title : Python program to display first and last colors from the given list.
    
'''


def first_and_last_colors(color_list):
    """
    Description: 
        This function returns the first and last colors from the given list.
    Parameters:
        color_list: A list containing color names.
    Return:
        tuple: A tuple containing the first and last colors.
    """
    if not color_list:
        return None, None
    return color_list[0], color_list[-1]


def main():
    color_list = ["Red", "Green", "White", "Black"]
    first_color, last_color = first_and_last_colors(color_list)
    print(f"First color: {first_color}")
    print(f"Last color: {last_color}")


if __name__ == "__main__":
    main()
