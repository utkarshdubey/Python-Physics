# imports
from functions.functions import DistanceFinderOne, DistanceFinderTwo, FinalVelocityFinderOne, FinalVelocityFinderTwo, TimeFinderOne, AccelarationFinderOne, UniformVelocityFinderOne
import sys
# logic here

while True:
    print("""
    1 => Find Distance, and I have U, A and T
    2 => Find Distance, and I have U, V and A
    3 => Find Final Velocity, and I have U, A and T
    4 => Find Final Velocity, and I have U, A and S
    5 => Find Accelaration, and I have U, V and T
    6 => Find Time, and I have U, V and A
    7 => Find Uniform Accelaration, and I have V, A and T

    0 => Exit
    """)
    answer = int(input("Please enter one of the options: "))
    if answer == 1:
        u_1 = float(input("Please enter U: "))
        a_1 = float(input("Please enter A: "))
        t_1 = float(input("Please enter T: "))
        DistanceFinderOne(u_1, a_1, t_1)

    if answer == 2:
        u_2 = float(input("Please enter U: "))
        v_2 = float(input("Please enter V: "))
        a_2 = float(input("Please enter A: "))

        DistanceFinderTwo(u_2, v_2, a_2)

    if answer == 3:
        u_3 = float(input("Please enter U: "))
        a_3 = float(input("Please enter A: "))
        t_3 = float(input("Please enter T: "))

        FinalVelocityFinderOne(u_3, a_3, t_3)

    if answer == 4:
        u_6 = float(input("Please enter U: "))
        a_6 = float(input("Please enter A: "))
        s_6 = float(input("Please enter S: "))

        FinalVelocityFinderTwo(u_6, a_6, s_6)

    if answer == 5:
        u_5 = float(input("Please enter U: "))
        v_5 = float(input("Please enter V: "))
        t_5 = float(input("Please enter T: "))

        AccelarationFinderOne(u_5, v_5, t_5)

    if answer == 6:
        u_4 = float(input("Please enter U: "))
        v_4 = float(input("Please enter V: "))
        a_4 = float(input("Please enter A: "))

        TimeFinderOne(u_4, v_4, a_4)

    if answer == 7:
        v_7 = float(input("Please enter V: "))
        a_7 = float(input("Please enter A: "))
        t_7 = float(input("Please enter T: "))

        UniformVelocityFinderOne(v_7, a_7, t_7)


    if answer == 0:
        sys.exit()
