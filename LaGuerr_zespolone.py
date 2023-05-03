import numpy as np

def laguerre_zesp(coeffs, x0, tol=1e-12, max_iter=100):
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
        a = n / (G + np.sign(G) * np.sqrt((n - 1) * (n * H - G ** 2)))  # obliczenie a
        x_new = x - a  # wyznaczenie nowego punktu x
        if abs(x_new - x) < tol:  # warunek stopu - znaleziono pierwiastek z dostateczną dokładnością
            return x_new
        x = x_new  # aktualizacja punktu początkowego
    return x

if __name__ == '__main__':
    # Przykładowe wielomiany
    poly1 = [1, -2, -3, 4]
    poly2 = [2, 0, -2, 1, -5]

    # Szukanie pierwiastków wielomianów
    roots1 = np.roots(poly1)
    roots2 = np.roots(poly2)
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
1) Na początku definiujemy stopień wielomianu jako n (liczba współczynników minus jeden, ponieważ najwyższy współczynnik nie bierze udziału w obliczeniach).
2) Przypisujemy wartość punktu początkowego do zmiennej x.
3) W pętli for wykonujemy kolejne iteracje algorytmu.
4) W każdej iteracji obliczamy wartość wielomianu p dla aktualnego punktu x.
5) Jeśli p jest równe zero, to ustawiamy wartość p na wartość tol (ma to na celu uniknięcie dzielenia przez zero).
6) Obliczamy wartości pierwszej i drugiej pochodnej wielomianu w punkcie x i przypisujemy je do zmiennych dp i d2p.
7) Obliczamy wartość G i H na podstawie wzorów z metody Laguerre'a.
8) Na podstawie wartości G i H obliczamy wartość a, która jest współczynnikiem do kolejnego punktu przybliżonego (zgodnie z wzorem z metody Laguerre'a).
9) Obliczamy wartość kolejnego punktu przybliżonego x_new na podstawie wartości x i a.
10) Jeśli różnica między x_new i x jest mniejsza niż zadaną tolerancję tol, to uznajemy, że znaleźliśmy pierwiastek i zwracamy wartość x_new.
11) W przeciwnym przypadku aktualizujemy wartość x na x_new i kontynuujemy pętlę for.
12) Jeśli liczba iteracji przekroczy wartość max_iter, to kończymy działanie funkcji i zwracamy ostatnią wartość x.
"""
