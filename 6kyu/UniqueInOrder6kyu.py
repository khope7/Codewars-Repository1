#unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
#unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
#unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
#unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
 
def unique_in_order(sequence):
    full_list = []
    previous_char = None  # Track the previous character
    
    for char in sequence:
        if char != previous_char:  # Compare with the previous character
            full_list.append(char)  # Append if it’s different
        previous_char = char  # Update the previous character

    return full_list  # Return the result

# Test the function
result = unique_in_order('AAAABBBCCDAABBB')
                         
print(result)  # Expected output: [‘A’, ‘B’, ‘C’, ‘D’, ‘A’, ‘B’]

'''
listexample = ["a", "b", "c", "d"]
for index, element in enumerate(listexample):
    print(f"Index: {index}, Element: {element}")

listexample = ["a", "b", "c", "d"]
# Access the second element (index 1)
if len(listexample) > 1:
    print(f"Index: 1, Element: {listexample[1]}")
else:
    print("List is too short!")'''