def grid_traveller1(m, n, mem={}):
    if m == 0 or n == 0:
        return 0

    if m == 1 and n == 1:
        return 1

    if (m, n) in mem:
        return mem[(m, n)]

    val = grid_traveller(m - 1, n) + grid_traveller(m, n - 1)
    mem[(m, n)] = val
    return val


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


def grid_traveller2(m, n):
    if m == 0 or n == 0:
        return 0

    def dp(i, j, mem={}):
        if i > m or j > n:
            return 0
        if i == m and j == n:
            return 1

        if (i, j) in mem:
            return mem[(i, j)]

        right = dp(i, j + 1, mem)
        left = dp(i + 1, j, mem)

        mem[(i, j)] = right + left

        return mem[(i, j)]

    return dp(1, 1, {})


print(grid_traveller(1, 1))
print(grid_traveller(2, 3))
print(grid_traveller(3, 2))
print(grid_traveller(3, 3))
print(grid_traveller(18, 18))
