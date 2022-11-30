def seidel(a, x, b):
    n = len(a)
    for j in range(0, n):
        d = b[j]
        for i in range(0, n):
            if j != i:
                d -= a[j][i] * x[i]
        x[j] = d / a[j][j]
    return x


x = [0, 0, 0, 0, 0]
a = [[14, -1, 2, 1, 8], [-1, 5, -1, -2, 0], [-2, -1, 6, -1, 1], [1, -2, -1, 5, 0], [2, 0, 1, 0, 4]]
b = [4, 1, -2, 1, 8]
print(x)

for i in range(0, 25):
    x = seidel(a, x, b)
print(x)
