import math
h = "False"
while True:
    if h == "False":
        m = input("What kind of unit? in, ft, cm, m. ").casefold()
    while m != "in" and m != "ft" and m != "cm" and m != "m":
        print("\nInvalid unit. Try again.\n")
        m = input("What kind of unit? in, ft, cm, m. ").casefold()
    h = "True"
    print(h)
    d = input("Enter Diameter: ")
    try:
        d = float(d)
    except ValueError:
        print("\nInvalid. Try again.\n")
        continue

    r = d/2

    A = round(math.pi * (r**2), 2)
    C = round(2 * math.pi * r, 2)

    print("\nThe Area is " + str(A) + str(m))
    print("The Circumference is " + str(C) + str(m))

    break