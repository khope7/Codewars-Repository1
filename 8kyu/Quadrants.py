def quadrant(x, y):
    if x >= 1 and y >= 1:
        a = 1
    elif x <= 1 and y >= 1:
        a = 2
    elif x >= 1 and y <= 1:
        a = 3
    else:
        a = 4
    
    return a
    
    print(a)

quadrant(1, 2)
quadrant(3,5)
quadrant(-10, 100)
quadrant(-1, -9)
quadrant(19, -56)