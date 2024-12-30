def move_zeros(lst):
    adjusted_lst = []
    index = 1

    for elem in lst:
        if elem != 0:
            adjusted_lst.append(elem)
    zeros = lst.count(0)
    
    while index <= zeros:
        adjusted_lst.append(0)
        index += 1

    return adjusted_lst

#    print(adjusted_lst)


move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]