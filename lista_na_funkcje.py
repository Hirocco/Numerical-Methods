#f = [1, 3, -5, -9]
#x^3 + 3x^2 - 5x -9
import sympy as sp

def lista_na_funkcje(f):
    x = sp.symbols('x')
    fun = sum(c*x**i for i, c in enumerate(f[::-1]))
    return fun
