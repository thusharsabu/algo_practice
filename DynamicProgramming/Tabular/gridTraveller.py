def gridTraveller1(m, n):
    if m == 0 or n == 0:
        return 0
    n1 = n + 1
    m1 = m + 1
    matrix = [[0 for _ in range(n1)] for _ in range(m1)]
    matrix[1][1] = 1

    for i in range(m1):
        for j in range(n1):
            if i + 1 <= m:
                matrix[i + 1][j] += matrix[i][j]
            if j + 1 <= n:
                matrix[i][j + 1] += matrix[i][j]
    # print(matrix)
    return matrix[m][n]


def gridTraveller(m, n):
    if m == 0 or n == 0:
        return 0

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    dp[1][1] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i + 1 < m + 1:
                dp[i + 1][j] += dp[i][j]

            if j + 1 < n + 1:
                dp[i][j + 1] += dp[i][j]
    return dp[m][n]


print(gridTraveller(1, 1))
print(gridTraveller(2, 3))
print(gridTraveller(3, 2))
print(gridTraveller(3, 3))
print(gridTraveller(18, 18))
