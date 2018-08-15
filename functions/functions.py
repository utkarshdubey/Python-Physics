def DistanceFinderOne(u, a, t):
    distance = float(u * t + 1/2 * a * pow(t, 2))
    return str(distance)

def DistanceFinderTwo(u, v, a):
    time = float(v / (u + a))
    distance = float(u * time + 1/2 * a * pow(time, 2))
    return str(distance)

def FinalVelocityFinderOne(u, a, t):
    final_velocity = float(u + a * t)
    return str(final_velocity)

def FinalVelocityFinderTwo(u, a, s):
    x = 2 * a * s
    final_velocity = float(pow(x, 1/2) + u)
    return str(final_velocity)

def TimeFinderOne(u, v, a):
    time = float(v / (u + a))
    return str(time)

def AccelarationFinderOne(u, v, t):
    accelaration = float((v - u) / t)
    return str(accelaration)

def UniformVelocityFinderOne(v, a, t):
    uniform_velocity = float(v + a * t)
    return str(uniform_velocity)
