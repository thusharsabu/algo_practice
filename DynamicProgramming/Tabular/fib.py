def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    mem = [0] * (n + 1)
    mem[1] = 1
    for i in range(n + 1):
        print(f"Mem: {mem} and I: {i}")
        if i + 2 < n + 1:
            mem[i + 2] += mem[i]
        mem[i + 1] += mem[i]

    return mem[n]


print(fib(4))
