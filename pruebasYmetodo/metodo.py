
def sumar(num1, num2):
    """Suma dos números."""
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Ambos valores deben ser numéricos.")
    return num1 + num2

if __name__ == "__main__":
    # Solicitar los números al usuario
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = sumar(num1, num2)
        print(f"La suma de {num1} y {num2} es {resultado}")
    except ValueError as e:
        print(f"Error: {e}")