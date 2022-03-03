def grid_traveller(m, n, mem={}):
    if m == 0 or n == 0:
        return 0

    if m == 1 and n == 1:
        return 1

    if (m, n) in mem:
        return mem[(m, n)]

    mem[(m - 1, n)] = grid_traveller(m - 1, n)
    mem[(m, n - 1)] = grid_traveller(m, n - 1)

    return mem[(m, n - 1)] + mem[(m - 1, n)]


print(grid_traveller(1, 1))
print(grid_traveller(2, 3))
print(grid_traveller(3, 2))
print(grid_traveller(3, 3))
print(grid_traveller(18, 18))
