def is_palidrome(s):
    """
    we need to compare the two string to see once reverse the read the same way
    """

    # define the original string as a variable
    original_data = s 

    # define the new string as a reverse of the original string
    new_data = revrsed(s)

    if original_data == new_data:
        return True
    
    return False


def revrsed(data):
    """
    we define our reverse function as a list in python 
    """
    data = list(data)

    # Define the start and end index
    start_index = 0 
    end_index = len(data) - 1 

    # we iterate over the data
    while end_index > start_index:
        data[start_index], data[end_index] = data[end_index], data[start_index]
        start_index += 1 
        end_index -= 1 

    return ''.join(data)


if __name__ == '__main__':
    s = "1221"
    is_palidrome(s)
    print(is_palidrome(s))







