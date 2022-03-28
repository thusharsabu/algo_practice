def fib_memory(n, mem={}):
    if n <= 2:
        return 1
    if n in mem:
        return mem[n]

    mem[n] = fib_memory(n - 1, mem) + fib_memory(n - 2, mem)
    return mem[n]


print(fib_memory(50))
