from numpy import array, zeros, fabs, linalg

a = array([[14, -1, 2, 1, 8], [-1, 5, -1, -2, 0], [-2, -1, 6, -1, 1], [1, -2, -1, 5, 0], [2, 0, 1, 0, 4]])

b = array([4, 1, -2, 1, 8])

n = len(b)
x = zeros(n,float)

# Gauss
for k in range(n-1):
    # fabs επιστρεφει τα απολυτα
    if fabs(a[k,k]) < 1.0e-12:
        for i in range(k+1,n):
            if fabs(a[i,k]) > fabs(a[k,k]):
                a[[k,i]] = a[[i,k]]
                b[[k,i]] = b[[i,k]]
    for i in range(k+1,n):
        if a[i,k] == 0:
            continue
        factor = a[k,k]/a[i,k] # με τι νουμερο να πολλαπλασιασουμε
        for j in range(k,n):
            a[i,j] == a[k,j] - a[i,j]*factor
        b[i] = b[k] - b[i]*factor
print(f"A:{a}")
print(f"b:{b}")


x[n-1] = b[n-1] / a[n-1,n-1]
for i in range(n-2,-1,-1):
    sum_ax = 0
    for j in range(i+1,n):
        sum_ax += a[i,j] * x[j]
    x[i] = (b[i] - sum_ax) / a[i,i]

print(f"x:{x}")

print(f"DetA:{linalg.det(a)}")

print(f"InvereA:{linalg.inv(a)}")
