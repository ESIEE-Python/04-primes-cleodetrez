"""
On importe la fonction racine carrée du module math
"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
    Fonction renvoyant si un nombre est premier ou non
    """
    for i in range(2,int(sqrt(p))) :
        if p%i == 0 :
            return False
    return True



#### Fonction principale


def main():
    """
    Renvoie tous les nombres premiers compris entre 0 et 100
    """
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print(n)


if __name__ == "__main__":
    main()
