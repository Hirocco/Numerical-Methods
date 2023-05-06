import numpy as np
from deflacja import oblicz_pierwiastek, deflation
from deflacja_zespolone import deflacja_zespolone, oblicz_pierwiastki_zespolone
from laGuerr import laguerre
from LaGuerr_zespolone import laguerre_zesp
from wykres import rysuj_wykres

if __name__ == '__main__':
    """ DZIALA
    print("Deflacja na liczbach rzeczywistych : \n")

    f = [1, 3, -5, -9]  # x^3 + 3x^2 - 5x -9
    pom_f = f
    roots = oblicz_pierwiastek(f)
    for i in range(0, len(roots)):
        root = roots[i]
        deflacja_wielomianu = deflation(pom_f, root)
        rysuj_wykres(np.roots(deflacja_wielomianu), deflacja_wielomianu)
        print(i,")Pomniejszony wielomian:" ,deflacja_wielomianu)
        pom_f = deflacja_wielomianu

    print("Pierwotny wielomian: ", f)
    print("Pierwiastki: ", roots)
    
    ###deflacja na liczbach zespolonych

    print("Deflacja dla liczb zespolonych : \n")

    poly = [1, -3, 3, -1]  # x^3 - 3x^2 + 3x - 1
    pom_poly = poly
    roots = oblicz_pierwiastki_zespolone(poly)
    for i in range(0, len(roots)):
        root = roots[i]
        deflacja_zespolona_wielomianu = deflacja_zespolone(pom_poly , root)
        print(i, ") Pomniejszony wielomian: ", deflacja_zespolona_wielomianu)
        pom_poly = deflacja_zespolona_wielomianu
    print("Poczatkowa funkcja : " , poly)
    rysuj_wykres(roots, poly)
    print("Pierwiastki : " , roots)


    """
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

    """
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