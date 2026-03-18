"""Module de calcul - Opération de base """
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

 feature/2-divide
def divide(a, b):
    if b == 0:
        raise ValueError("Division par zero est impossible")
    return a / b
def power(base, exp):
    return base ** exp
 main
