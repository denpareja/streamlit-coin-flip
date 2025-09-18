import math

def is_prime(n: int) -> bool:
    """
    Determina si un número entero es primo.

    Parámetros
    ----------
    n : int
        Número entero a evaluar.

    Retorna
    -------
    bool
        True si el número es primo, False en caso contrario.
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    """
    Imprime todos los números primos menores de 100.
    """
    for i in range(100):
        if is_prime(i):
            print(i, end=" ")
        print()  # salto de línea final

if __name__ == "__main__":
    main()
