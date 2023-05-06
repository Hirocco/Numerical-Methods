from sympy import *
import numpy as np
from lista_na_funkcje import lista_na_funkcje

def oblicz_pochodna(f): #f = [1, 3, -5, -9]  x^3 + 3x^2 - 5x -9
    x = symbols('x') #wybieramy zmienną która będzie respektowana
    fun = lista_na_funkcje(f)
    df = diff(fun, x)  #obliczamy pierwszą pochodną
    df_poly = Poly(df, x) #Aby obliczyć współczynniki wielomianu, musimy utworzyć obiekt typu Poly z obiektu Expr
    coeffs = df_poly.coeffs()
    return coeffs


def oblicz_pierwiastek(f):
    return np.roots(f).real


def deflation(poly, root):
    """
    Funkcja dokonująca deflacji wielomianu poly przez usunięcie pierwiastka root.
    Argumenty:
    poly - lista współczynników wielomianu, zaczynając od najwyższej potęgi,
    root - pierwiastek do usunięcia.
    """
    n = len(poly) #n- ty st. wielomianu
    if n>1:
        q = [0] * (n - 1) #lista zer o długości n-1
        q[-1] = poly[-1] #przypisanie ostatniej wartości do listy q

        for i in range(n - 2, -1):
            q[i] = poly[i + 1] + root * q[i + 1]

        q[0] = poly[0] + root * q[0]

        return q
    else:
        print("Deflacja możliwa jest tylko dla wielomianów st. większego od 1")
        return poly





