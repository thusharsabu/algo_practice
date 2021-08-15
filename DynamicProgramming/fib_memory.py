
def fib_memory(n):
  dict_ = {}
  def fib(val):
    if val <= 2: return 1

    if val in dict_: return dict_[val]

    current = fib(val - 1) + fib(val - 2)
    dict_[val] = current
    return current
  return fib(n)

print(fib_memory(500))
