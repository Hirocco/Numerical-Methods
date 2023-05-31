import numpy as np
from wykres import rysuj_wykres

def deflation(poly, root):
    """
    Funkcja dokonująca deflacji wielomianu poly przez usunięcie pierwiastka root.
    Argumenty:
    poly - lista współczynników wielomianu, zaczynając od najwyższej potęgi,
    root - pierwiastek do usunięcia.
    """
    n = len(poly) - 1
    if n <= 1:
        print("Deflacja mozliwa jest tylko dla wielomianow st. wiekszego od 1")
        return poly
    else:
        # krok 1: pobranie listy współczynników oraz pierwiastka
        print("Pobrany wielomian: ", poly)
        print("Pobrany pierwiastek: ", root)

        # krok 2: podzielenie listy przez pierwiastek
        q = [poly[0]]
        for i in range(1, n):
            q.append(poly[i] + root * q[i - 1])
        return q
def laguerre(poly_coeffs, initial_guess, epsilon=1e-6, max_iterations=100):
    n = len(poly_coeffs) - 1  # Stopień wielomianu
    x = initial_guess
    roots = []

    for _ in range(n):
        for _ in range(max_iterations):

            # Obliczanie wartości wielomianu w punkcie x
            p = np.polyval(poly_coeffs, x)

            # Obliczenie pochodnej wielomianu dla obecnego przybliżenia
            poly_deriv = np.polyder(poly_coeffs)
            q = np.polyval(poly_deriv, x)

            # Obliczenie drugiej pochodnej wielomianu dla obecnego przybliżenia
            poly_2nd_deriv = np.polyder(poly_deriv)
            r = np.polyval(poly_2nd_deriv, x)

            if np.abs(p) < epsilon:
                break

            # Wyliczanie współczynników pomocniczych wielomianów
            G = q / p
            H = G**2 - r / p


            # Obliczanie wartości analitycznych mianowników
            sqrt_term = np.sqrt(np.abs((n - 1) * (n * H - G**2)))
            denom_plus = G + sqrt_term
            denom_minus = G - sqrt_term

            # Wybór większego mianownika
            if np.abs(denom_plus) > np.abs(denom_minus):
                a = n / denom_plus
            else:
                a = n / denom_minus

            # Obliczanie nowych przybliżeń
            x_new = x - a

            # Jeżeli różnica między nowym a poprzednim przybliżeniem jest mniejsza niż epsilon,
            # to zakończenie obliczenia
            if np.abs(x_new - x) < epsilon:
                break
            x = x_new
        # Dodajemy nowo znaleziony pierwiastek do listy
        roots.append(np.around(x,5))

        # Wypisujemy współczynniki wielomianu
        print(poly_coeffs)

        # Używamy deflacji aby zmniejszyć stopień wielomianu
        poly_coeffs = deflation(poly_coeffs,x)

        #To jest to stare
        #poly_coeffs = np.polydiv(poly_coeffs, [1, -x])[0]


    return roots

#poly_coeffs = [1, -3, 3, -1]
#poly_coeffs = [1, 3, -5, -9]
#poly_coeffs = [1, 3, -5, -10]
poly_coeffs = [1, 0, -6, 0, 8]

initial_guess = 1

# Znajdź pierwiastki wielomianu
roots = laguerre(poly_coeffs, initial_guess)

# Wypisz wartości pierwiastków
print("Pierwiastki wielomianu:", roots)

pom_f = poly_coeffs

for i in range(0, len(roots)):
    root = roots[i]
    deflacja_wielomianu = deflation(pom_f, root)
    rysuj_wykres(np.roots(deflacja_wielomianu), deflacja_wielomianu)
    print(i, ")Wielomian po deflacji: " ,deflacja_wielomianu)
    pom_f = deflacja_wielomianu

# Rysuj wykres wielomianu z zaznaczonymi miejscami zerowymi
rysuj_wykres(roots, poly_coeffs)