#input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
#output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]

def open_or_senior(data):
    customers = []
    for element in data:
        if element[0] > 55 and element[1] > 7:
            customers.append("Senior")
        else:
            customers.append("Open")
            
    return customers



input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]

open_or_senior(input)