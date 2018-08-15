def DistanceFinderOne(u, a, t):
    distance = float(u * t + 1/2 * a * pow(t, 2))
    print("The distance is " + str(distance) + " metres")

def FinalVelocityFinderOne(u, a, t):
    final_velocity = float(u + a * t)
    print("The final velcoity is " + str(final_velocity) + " m/s")
