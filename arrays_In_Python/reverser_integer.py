def reverse_integer(nums):
    remainder = 0 
    reversed_nums = 0 

    while nums > 0:
        remainder = nums % 10
        reversed_nums = reversed_nums*10 + remainder
        nums = nums//10 

    return reversed_nums


if __name__ == '__main__':
    n = 12345678900890
    print(reverse_integer(n))
