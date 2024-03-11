def calcular_descuento(monto_compra, porcentaje_descuento=10):
    """
    Calcula el descuento aplicando el porcentaje al monto total de la compra.

    Args:
        monto_compra (float): El monto total de la compra.
        porcentaje_descuento (float, optional): El porcentaje de descuento a aplicar. Por defecto es 10%.

    Returns:
        float: El monto del descuento calculado.
    """
    descuento = monto_compra * (porcentaje_descuento / 100)
    return descuento


# Llamada a la función con el monto total de la compra y el porcentaje de descuento por defecto
monto_compra_1 = 100.0
descuento_1 = calcular_descuento(monto_compra_1)
monto_final_1 = monto_compra_1 - descuento_1
print(f"Monto de la compra 1: {monto_compra_1:.2f}")
print(f"Descuento aplicado (10%): {descuento_1:.2f}")
print(f"Monto final a pagar: {monto_final_1:.2f}")
print()

# Llamada a la función con el monto total de la compra y un porcentaje de descuento específico
monto_compra_2 = 200.0
porcentaje_descuento_2 = 15
descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)
monto_final_2 = monto_compra_2 - descuento_2
print(f"Monto de la compra 2: {monto_compra_2:.2f}")
print(f"Descuento aplicado ({porcentaje_descuento_2}%): {descuento_2:.2f}")
print(f"Monto final a pagar: {monto_final_2:.2f}")