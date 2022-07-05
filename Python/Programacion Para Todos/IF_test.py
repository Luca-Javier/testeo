""" anidamiento estructural """
p1 = int(input("2 + 2 = "))
if p1 == 4:
    print("Correcto")
    p2 = int(input("3 + 3 = "))
    if p2 == 6:
        print("Correcto")
        p3 = int(input("4 + 4 = "))
        if p3 == 8:
            print("Correcto, acertaste todo")
        else:
            print("Fail")
    else:
        print("Fail")
else:
    print("Fail")
