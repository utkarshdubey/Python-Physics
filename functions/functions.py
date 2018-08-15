def DistanceFinderOne(u, a, t):
    distance = float(u * t + 1/2 * a * pow(t, 2))
    print("The distance is " + str(distance) + " metres")

def DistanceFinderTwo(u, v, a):
    time = float(v / (u + a))
    distance = float(u * time + 1/2 * a * pow(time, 2))
    print("The distance is " + str(distance) + " metres")

def FinalVelocityFinderOne(u, a, t):
    final_velocity = float(u + a * t)
    print("The final velcoity is " + str(final_velocity) + " m/s")

def FinalVelocityFinderTwo(u, a, s):
    x = 2 * a * s
    final_velocity = float(pow(x, 1/2) + u)
    print("The final velcoity is " + str(final_velocity) + " m/s")

def TimeFinderOne(u, v, a):
    time = float(v / (u + a))
    print("The time is " + str(time) + " seconds")

def AccelarationFinderOne(u, v, t):
    accelaration = float((v - u) / t)
    print("The accelaration is " + str(accelaration) + " m/s^2")

def UniformVelocityFinderOne(v, a, t):
    uniform_velocity = float(v + a * t)
    print("The uniform velocity is " + str(uniform_velocity) + " m/s")
