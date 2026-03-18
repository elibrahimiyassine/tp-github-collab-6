"""Module de calcul - Opération de base """
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
def divide(a, b):
    if b == 0:
        raise ValueError("Division par zero est impossible")
    return a / b