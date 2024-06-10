def ispalidrome(data):
    original_data = data
    new_data = data_reversed(original_data)

    if new_data == original_data:
        return True
    else:
        return False
    

def data_reversed(data):
    data = list(data)

    first_index = 0 
    last_index = len(data) - 1 

    while first_index < last_index:
        data[first_index], data[last_index] = data[last_index], data[first_index]
        first_index += 1
        last_index -= 1 
    
    return ''.join(data)


if __name__ == '__main__':
    s = 'light'
    print(ispalidrome(s))

