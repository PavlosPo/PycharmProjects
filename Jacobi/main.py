from numpy import array, diag, diagflat, dot

def jacobi(A,b,N=25,x=None):

    # Create a vector of the diagonal elements of A
    # and subtract them from A
    # Δημιουργια διαγωνιου πινακα και αφαιρεση απο το Α
    D = diag(A)
    R = A - diagflat(D)

    # 25 κυκλοι
    for i in range(N):
        x = (b - dot(R,x)) / D
    return x

A = array([[14, -1, 2, 1, 8], [-1, 5, -1, -2, 0], [-2, -1, 6, -1, 1], [1, -2, -1, 5, 0], [2, 0, 1, 0, 4]])
b = array([4, 1, -2, 1, 8])
guess = array([0,0,0,0,0])

sol = jacobi(A, b , N=25 , x=guess)

print(f"A:{A}")

print(f"b:{b}")

print(f"x:{sol}")