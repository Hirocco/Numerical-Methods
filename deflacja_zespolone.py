import numpy as np

def qr_deflation(coeffs, root, tol=1e-12, max_iter=100):
    """
    Funkcja obliczająca nowe współczynniki wielomianu po wykonaniu QR-deflacji dla danego pierwiastka.

    Argumenty:
    coeffs -- wektor współczynników wielomianu
    root -- pierwiastek do usunięcia z wielomianu
    tol -- tolerancja do zatrzymania algorytmu
    max_iter -- maksymalna liczba iteracji algorytmu

    Zwraca:
    coeffs_new -- wektor współczynników wielomianu po wykonaniu QR-deflacji
    """
    n = len(coeffs)

    # przygotowanie macierzy Hessenberga
    H = np.zeros((n, n))
    for i in range(n):
        H[i, i] = coeffs[i]
        if i < n-1:
            H[i+1, i] = 1

    # iteracyjne wykonanie QR-deflacji
    for k in range(n-1, 0, -1):
        while abs(H[k, k-1]) > tol*(abs(H[k-1, k-1]) + abs(H[k, k])):
            Q, R = np.linalg.qr(H - H[k, k]*np.eye(n))
            H = np.dot(R, Q) + H[k, k]*np.eye(n)

        # usunięcie k-tego pierwiastka
        if abs(H[k, k-1]) < tol*(abs(H[k-1, k-1]) + abs(H[k, k])):
            H[k, k-1] = 0
            H[k-1, k] = 0

        # podstawienie zera w miejscu pierwiastka
        for i in range(k, n-1):
            c, s = H[i:i+2, i:i+2].dot([H[i, i-1], H[i+1, i-1]])
            H[i, i-1] = c
            H[i+1, i-1] = 0
            H[i, i] = s

    # wyznaczenie nowych współczynników
    coeffs_new = np.zeros(n-1)
    for i in range(n-1):
        coeffs_new[i] = H[i, i]

    return coeffs_new

if __name__ == '__main__':
    coeffs = np.array([1, 3, -3, -13, -10])
    roots = np.array([-2, 1, 5])
    for root in roots:
        coeffs = qr_deflation(coeffs, root)
    print(coeffs)
