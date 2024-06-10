def reverse_data(data):
    # set data to list for python implmentation
    data = list(data)

    # Using two pointer references for start and end index
    start_index = 0
    end_index = len(data) - 1

    # Iterate over the list, swap data as we increment and de-crement the reference pointers

    while start_index < end_index:
        data[start_index], data[end_index] = data[end_index], data[start_index]
        start_index = start_index + 1
        end_index = end_index - 1 

    return ''.join(data)


if __name__ == "__main__":
    s = "new day"
    new_s = reverse_data(s)
    print(new_s)


