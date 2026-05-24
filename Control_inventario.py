# ==========================================
# Programa de Control de Inventario
# Fase 5 - Evaluación Final POA
# Fundamentos de Programación
# Desarrollado por: Jose Luis Salazar Avila
# ==========================================

# Matriz de artículos
# [Código, Nombre, Stock Actual, Stock Mínimo]

articulos = [
    ["A01", "Teclado", 3, 10],
    ["A02", "Mouse", 15, 10],
    ["A03", "Monitor", 2, 5],
    ["A04", "Impresora", 8, 8],
    ["A05", "Memoria USB", 1, 6]
]

# Función para calcular la cantidad a solicitar
def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        pedido = stock_minimo - stock_actual
    else:
        pedido = 0

    return pedido


# Título del reporte
print("========================================")
print("   REPORTE DE REABASTECIMIENTO")
print("========================================")

# Recorrer la matriz de artículos
for articulo in articulos:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    # Llamado de la función
    cantidad_pedido = calcular_pedido(stock_actual, stock_minimo)

    # Mostrar resultados
    print(f"\nCódigo: {codigo}")
    print(f"Artículo: {nombre}")
    print(f"Stock Actual: {stock_actual}")
    print(f"Stock Mínimo: {stock_minimo}")
    print(f"Cantidad a Solicitar: {cantidad_pedido}")

print("\n========================================")
print("     FIN DEL REPORTE")
print("========================================")