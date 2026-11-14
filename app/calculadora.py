"""Operaciones aritméticas usadas por la aplicación de la calculadora."""

AUTOR = "Manuela Jimenez Arredondo | David Moreno Moran | Angélica Martínez Carmona"


def sumar(a, b):
    """Devuelve la suma de dos números."""
    return a + b


def restar(a, b):
    """Devuelve la diferencia entre dos números."""
    return a - b


def multiplicar(a, b):
    """Devuelve el producto de dos números."""
    return a * b


def dividir(a, b):
    """Devuelve el cociente de dos números; falla si el divisor es cero."""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
