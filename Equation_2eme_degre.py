import math

def delta(a, b, c):
    deltaa = (b * b) - 4*(a * c)
    return deltaa


def nb_solutions(a, b, c):
    deltmp = delta( a, b, c )
    if deltmp > 0:
        return 2
    elif deltmp < 0:
        return 0
    else:
        return 1


def AfficheNombreRacine(a, b, c):
    nb_racines = nb_solutions( a, b, c )
    if nb_racines == 2:
        print( "Il y a deux racines reelles" )
    elif nb_racines == 1:
        print( "Il y a une racine reelle" )
    else:
        print( "Il n'y a pas de racine" )


def Racine1(a, b, c):
    delt = delta(a, b, c)
    if delt >= 0:
        return (-b + math.sqrt(delt)) / (2 * a)
    else:
        return None


def Racine2(a, b, c):
    delt = delta(a, b, c)
    if delt >= 0:
        return (-b - math.sqrt(delt)) / (2 * a)
    else:
        return None

print("Zakaria's birthdays is :"+str(Racine1(1,-6,8))+"/"+str(Racine2(1,-6,8)))

