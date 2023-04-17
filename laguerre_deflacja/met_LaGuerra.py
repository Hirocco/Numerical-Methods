import numpy as np

def laguerre(coeffs, x0, tol=1e-12, max_iter=100):
    """
    Oblicza pierwiastki wielomianu reprezentowanego przez wektor współczynników `coeffs`
    zaczynając od punktu początkowego `x0` z tolerancją `tol` i maksymalną liczbą iteracji `max_iter`.
    """
    n = len(coeffs) - 1  # stopień wielomianu
    x = x0  # punkt początkowy
    for i in range(max_iter):  # pętla iteracyjna
        p = np.polyval(coeffs, x)  # wartość wielomianu w punkcie x
        if p == 0:
            p = tol  # unikanie dzielenia przez zero - zamiast zera używamy wartości tolerancji
        dp = np.polyval(np.polyder(coeffs), x)  # wartość pochodnej wielomianu w punkcie x
        d2p = np.polyval(np.polyder(coeffs, 2), x)  # wartość drugiej pochodnej wielomianu w punkcie x
        G = dp / p  # pomocnicza wartość G
        H = G ** 2 - d2p / p  # pomocnicza wartość H
        if (n - 1) * (n * H - G ** 2) < 0:  # wybór lepszego mianownika a
            a = n / (G + np.sign(G) * np.sqrt(abs((n - 1) * (n * H - G ** 2))))  # obliczenie a z dodatkową wartością bezwzględną w pierwiastku, aby uniknąć problemów z liczbami zespolonymi
        else:
            a = n / (G + np.sign(G) * np.sqrt((n - 1) * (n * H - G ** 2)))  # obliczenie a
        x_new = x - a  # wyznaczenie nowego punktu x
        if abs(x_new - x) < tol:  # warunek stopu - znaleziono pierwiastek z dostateczną dokładnością
            return x_new
        x = x_new  # aktualizacja punktu początkowego
    return x




if __name__ =='__main__':
    coeffs = [1, -2, 4, -8]
    x0 = 3.0
    root = laguerre(coeffs, x0)
    print(root)  # powinno wypisać 2.0
    roots = []
    while len(coeffs) > 1:
        x0 = np.random.randn()
        root = laguerre(coeffs, x0)
        coeffs = np.polydiv(coeffs, [1, -root])[0]
        roots.append(root)
    if len(coeffs) == 1:
        roots.append(-coeffs[0])
    print(roots)


