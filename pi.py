import math

while True:
    d = input("Enter Diameter: ")
    try:
        d = float(d)
    except ValueError:
        print("\nInvalid\n")
        continue

    r = d/2

    A = math.pi * (r**2)
    C = 2 * math.pi * r

    print("The Area is " + str(A))
    print("The Circumference is " + str(C))

    break