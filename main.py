# imports

# logic here

while True:
    print("""
    1 => Find Distance, and I have U, A and T
    2 => Find Final Velocity, and I have U, A and T
    """)
    answer = int(input("Please enter one of the options: "))
    if answer == 1:
        u_1 = float(input("Please enter U: "))
        a_1 = float(input("Please enter A: "))
        t_1 = float(input("Please enter T: "))

        s_1 = float(u_1 * t_1 + 1/2 * a_1 * pow(t_1, 2))
        print("The distance is " + str(s_1) + " metres")
    if answer == 2:
        print("You chose 2")
