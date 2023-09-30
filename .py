def rgb_to_hex(rgb):
    # Asegúrate de que los valores RGB estén en el rango correcto (0-255)
    r, g, b = rgb
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))

    # Convierte los valores RGB a formato hexadecimal
    hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)

    return hex_color

# Solicitar valores RGB al usuario
try:
    r = int(input("Introduce el valor de R (0-255): "))
    g = int(input("Introduce el valor de G (0-255): "))
    b = int(input("Introduce el valor de B (0-255): "))
except ValueError:
    print("Por favor, introduce números enteros válidos para los valores RGB.")
else:
    rgb_values = (r, g, b)
    hex_color = rgb_to_hex(rgb_values)
    print("Valor hexadecimal:", hex_color)
