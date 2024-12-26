#unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
#unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
#unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
#unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
 
def unique_in_order(sequence):
    full_list = []
    position = -1
    for char in sequence:
        position = position + 1
        if char not in full_list:
            full_list.append(char)


    print(full_list)


unique_in_order('AAAABBBCCDAABBB')