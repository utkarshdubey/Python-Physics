# imports
from functions.functions import DistanceFinderOne, FinalVelocityFinderOne
import sys
# logic here

while True:
    print("""
    1 => Find Distance, and I have U, A and T
    2 => Find Final Velocity, and I have U, A and T
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
        a_2 = float(input("Please enter A: "))
        t_2 = float(input("Please enter T: "))
        FinalVelocityFinderOne(u_2, a_2, t_2)

    if answer == 0:
        sys.exit()
    else:
        print("Please enter a right option!")
