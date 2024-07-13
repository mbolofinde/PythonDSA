def reverse_array(nums):
    """
    we use a 2 pinter approach and define the start and end index 
    """

    # Define the Start index
    start_index = 0

    # Define the End Index
    end_index = len(nums) - 1 

    # Iterate over the list, Array
    while end_index > start_index:
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        start_index += 1
        end_index -= 1


if __name__ == '__main__':
    n = [ 12, 3, -1, 7, 2, 3, 10]
    reverse_array(n)
    print(n)