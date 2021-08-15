# Coin Change


def coin_change(coins, amount):
  mem = {}
  # for coin in coins:
  #   mem[coin] = [coin]
  # coins.sort()
  # coins.reverse()
  def dfs(target, mem):
    if target in mem: return mem[target]
    if target == 0: return []
    if target < 0: return None
    
    comb = None
    
    for coin in coins:
        remainder = target - coin
        res = dfs(remainder, mem)
        
        if res is not None:
            if comb is None or len(res) < len(comb):
                comb = res + [coin]
    mem[target] = comb
    return mem[target]
  return len(dfs(amount, {}))

print(coin_change([1,2,3,4,5,6,7,8,9,10,25], 1000))