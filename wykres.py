import numpy as np
import matplotlib.pyplot as plt

def rysuj_wykres(roots,coeffs):
    # Określenie granic przedziału
    x_min, x_max = -10, 10
    y_min,y_max = -10, 10
    # Tworzenie listy punktów x
    x = np.linspace(x_min, x_max, 1000)

    # Obliczanie wartości funkcji dla każdego punktu x
    y = np.polyval(coeffs, x)

    # Tworzenie wykresu
    plt.plot(x, y, label="f(x)")
    plt.plot(roots, np.zeros_like(roots), "ro", label="pierwiastki")
    plt.legend()
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')

    # ustawienie zakresów osi x i y
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    # ustawienie podziałki osi x i y
    plt.xticks(range(int(x_min), int(x_max) + 1, 1))
    plt.yticks(range(int(y_min), int(y_max) + 1, 10))
    plt.show()
