def will_you(young, beautiful, loved):
    if loved == True:
        if young == True or beautiful == True:
            print("This one")
            return True
        else:
            return False
    
    elif loved == False:
        young == True or beautiful == True
        print("That one")
        return True
    
will_you(True, True, False)