def binary_search(nums, val):
    low = 0
    high = len(nums) - 1 

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == val:
            return f"The target value is: {val} at location in the list {mid}"
        elif nums[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return 'not found'


if __name__ == '__main__':
    n = [1,2,3,4,5,6,7]
    value = 3
    rst = binary_search(n, value)
    print(rst)
