def is_palidrone(s):
    """
    a palindrome is when you reverse a given string handled as a list in python 
    and it will still spell and mean the same word
    e.g. radar , madam... 
    to solve this we need to have 2 pointer referencing the start_index and end_index
    respectively in a list. 

    """
    # let us define any date passed as a list
    s = list(s)

    # Defne the start index & the end index 
    start_index = 0 
    end_index = len(s) - 1 

    # we now iterate though the list 
    while start_index < end_index:
        # we now do a swap to reverse the list
        s[start_index], s[end_index] = s[end_index], s[start_index]
        # now we perform an increment on the start_index and a decrement on the 
        # End Index
        start_index += 1
        end_index -+ 1
    
    return "".join(s)



if __name__ == "__main__":
    n = "new day today"