
def print_pyramid(n):
    # Calcular el número total de espacios en blanco en la primera línea
    total_spaces = n - 1
    
    for i in range(1, n*2, 2):
        # Calcular los espacios en blanco para la línea actual
        space = total_spaces - i // 2
        print(" " * space + "*" * i)

ask = int(input("Introduce n niveles de la piramide: "))
print_pyramid(ask)
