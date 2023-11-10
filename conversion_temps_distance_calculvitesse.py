
def conversion_temps(h, m, s):
    return h * 3600 + m * 60 + s

def temps_ecoule(h1, m1, s1, h2, m2, s2):
    temps1 = conversion_temps(h1, m1, s1)
    temps2 = conversion_temps(h2, m2, s2)
    return abs( temps2 - temps1 )

def conversion_distance(km, m, cm):
    return km * 1000 + m + cm / 100

def vitesse(distance, temps):
    distance_metres = conversion_distance(*distance)
    temps_secondes = conversion_temps(*temps)
    return distance_metres / temps_secondes

