import numpy as np
from deflacja import oblicz_pierwiastek, deflation
from deflacja_zespolone import qr_deflation
from laGuerr import laguerre
from LaGuerr_zespolone import laguerre_zesp
from wykres import rysuj_wykres

if __name__ == '__main__':
    ###Deflacja na liczbach rzeczywistych

    f = [1, 3, -5, -9]  # x^3 + 3x^2 - 5x -9
    pom_f = f  # funkcja pomocnicza
    stopien = len(pom_f)  # stopien wielomianu
    roots = []  # pierwiastki wielomianu
    root = oblicz_pierwiastek(f)
    roots.append(round(root, 5))
    while root is not None and stopien > 1:
        deflacja_wielomianu = deflation(pom_f, root)
        root = oblicz_pierwiastek(deflacja_wielomianu)
        roots.append(round(root, 5))
        pom_f = deflacja_wielomianu
        stopien = len(pom_f)
    print("Deflacja na liczbach rzeczywistych : \n")
    print("Pierwiastki: ", roots)
    print("Pierwotny wielomian: ", f)
    print("Wielomian po deflacji: ", pom_f)
    rysuj_wykres(roots,f)

"""
    ###deflacja na liczbach zespolonych

    coeffs = np.array([1, 3, -3, -13, -10])
    roots = np.array([-2, 1, 5])
    for root in roots:
        coeffs = qr_deflation(coeffs, root)
    print("Deflacja na liczbach zespolonych: \n")
    print(coeffs)

    ###metoda LaGuerr'a na liczbach rzeczywistych

    coeffs = [1, -2, 4, -8]
    x0 = 3.0
    root = laguerre(coeffs, x0)
    roots = []
    while len(coeffs) > 1:
        x0 = np.random.randn()
        root = laguerre(coeffs, x0)
        coeffs = np.polydiv(coeffs, [1, -root])[0]
        roots.append(root)
    if len(coeffs) == 1:
        roots.append(-coeffs[0])
    print("Metoda LaGuerr'a na liczbach rzeczywistych: \n")
    print(roots)

    ###metoda LaGuerr'a na liczbach zespolonych

    # Przykładowe wielomiany
    poly1 = [1, -2, -3, 4]
    poly2 = [2, 0, -2, 1, -5]

    # Szukanie pierwiastków wielomianów
    roots1 = np.roots(poly1)
    roots2 = np.roots(poly2)
    print("Metoda LaGuerr'a na liczbach zespolonych: \n")
    print("Pierwiastki wielomianu 1 (numpy.roots):", roots1)
    print("Pierwiastki wielomianu 1 (Laguerre):")
    for i in range(len(roots1)):
        root = laguerre_zesp(poly1, roots1[i])
        print(f"x_{i + 1} =", root)
    print("Pierwiastki wielomianu 2 (numpy.roots):", roots2)
    print("Pierwiastki wielomianu 2 (Laguerre):")
    for i in range(len(roots2)):
        root = laguerre_zesp(poly2, roots2[i])
        print(f"x_{i + 1} =", root)
"""