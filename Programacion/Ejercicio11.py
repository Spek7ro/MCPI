A = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

B = [
    [1, -1, 2],
    [2, -1, 2],
    [3, -3, 0]
]

# Producto de matrices A x B
# A es de 3x3, B es de 3x3, el resultado será una matriz de 3x3
producto = [
    [
        sum(A[i][k] * B[k][j] for k in range(3))  # producto fila i por columna j
        for j in range(3)
    ]
    for i in range(3)
]

print("Producto de matrices A x B:")
for fila in producto:
    print(fila)