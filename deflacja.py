import sympy as sp

def oblicz_pochodna(f):
    x = sp.symbols('x')
    f_sym = sp.Poly(f, x)
    df_sym = f_sym.diff(x)
    coeffs = df_sym.coeffs()
    degree = df_sym.degree()
    df = []
    for i in range(degree, -1, -1):
        df.append(coeffs[i])
    return df



def oblicz_pierwiastek(f, x0=1, epsilon=0.0001, max_iter=1000):
    pochodna_f = oblicz_pochodna(f)
    x = x0
    iteracja = 0
    wartosc_f = sum([f[i] * x ** (len(f) - 1 - i) for i in range(len(f))])
    while abs(wartosc_f) > epsilon and iteracja < max_iter:
        mianownik = sum([pochodna_f[i] * x ** (len(pochodna_f) - 1 - i) for i in range(len(pochodna_f))])
        if abs(mianownik) < epsilon:
            break
        x = x - wartosc_f / mianownik
        wartosc_f = sum([f[i] * x ** (len(f) - 1 - i) for i in range(len(f))])
        iteracja += 1
    return x



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


if __name__ == '__main__':
    f = [1, 3, -5, -9]  # x^3 + 3x^2 - 5x -9
    pom_f = f #funkcja pomocnicza
    stopien = len(pom_f) #stopien wielomianu
    roots = [] #pierwiastki wielomianu
    root = oblicz_pierwiastek(f)
    roots.append(round(root,5))
    while (root is not None and stopien>1):
        deflacja_wielomianu = deflation(pom_f,root)
        root = oblicz_pierwiastek(deflacja_wielomianu)
        roots.append(round(root,5))
        pom_f = deflacja_wielomianu
        stopien = len(pom_f)
    if len(roots) != len(f) - 1:
        missing_roots = len(f) - 1 - len(roots)
        print("Uwaga: brakuje", missing_roots, "pierwiastków")

    print("Pierwiastki: ", roots)
    print("Pierwotny wielomian: ", f)
    print("Wielomian po deflacji: ", pom_f)
