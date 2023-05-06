import numpy as np
from wykres import rysuj_wykres
def deflacja_zespolone(poly, root):
    """
    Funkcja dokonująca deflacji wielomianu poly przez usunięcie pierwiastka root.
    Argumenty:
    poly - lista współczynników wielomianu, zaczynając od najwyższej potęgi,
    root - pierwiastek do usunięcia.
    """
    n = len(poly)  # n-ty st. wielomianu
    if n > 1:
        q = np.zeros(n - 1, dtype=np.complex128)  # lista zer o długości n-1

        q[-1] = poly[-1]  # przypisanie ostatniej wartości do listy q

        for i in range(n - 2, -1):
            q[i] = poly[i + 1] + root * q[i + 1]

        q[0] = poly[0] + root * q[0]

        return q[:-1]
    else:
        print("Deflacja możliwa jest tylko dla wielomianów st. większego od 1")
        return poly

def oblicz_pierwiastki_zespolone(poly):
    roots = np.roots(poly)
    return roots


