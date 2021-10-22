

def cacheContents(callLogs):
  sortedLogs = sorted(callLogs, key = lambda x:x[0])
  counterDict = {}
  cache = set()

  for t, id in callLogs:
    if id not in counterDict:
      counterDict[id] = [2, t]
    else:
      value = counterDict[id][0] - (t-counterDict[id][1]) + 1
      value = 0 if value < 0 else value
      counterDict[id] = [value + 2, t]

      if counterDict[id][0] > 5:
        cache.add(id)

  lastTime = sortedLogs[-1][0]

  newCache = list(cache)
  for value in newCache:
    current = counterDict[value]
    if current[0] - (lastTime - current[1]) <= 3:
      cache.remove(value)

  return list(cache)

print(cacheContents([[1, 25], [1, 17], [1, 10], [1, 28], [1, 4], [1, 27], [2, 37], [2, 11], [3, 13], [3, 37], [3, 3], [3, 6], [4, 25], [4, 30], [4, 9], [4, 9], [4, 31], [4, 18], [5, 12], [5, 1], [5, 20], [5, 8], [5, 8], [6, 2], [6, 31], [6, 28], [6, 11], [6, 28], [6, 9], [6, 35], [7, 21], [7, 6], [7, 19], [7, 28], [7, 29], [7, 5], [7, 18], [8, 29], [8, 34], [9, 9], [9, 2], [9, 26], [9, 29], [10, 36], [10, 6], [10, 37], [10, 13], [10, 31], [10, 19], [11, 15], [11, 16], [11, 2], [11, 3], [11, 40], [12, 17], [12, 17], [12, 23], [12, 2], [12, 14], [12, 33], [13, 22], [13, 11], [13, 34], [13, 38], [13, 39], [13, 28], [13, 36], [13, 11], [14, 20], [14, 11], [14, 10], [14, 4], [14, 14], [14, 22], [14, 34], [15, 26], [15, 9], [15, 21], [15, 18], [15, 7], [16, 5], [16, 2], [16, 13], [17, 35], [18, 9], [18, 4], [18, 19], [18, 23], [18, 8], [18, 38], [18, 35], [18, 10], [19, 4], [19, 34], [19, 31], [19, 27], [20, 19], [20, 4], [20, 9], [20, 27], [20, 16], [20, 22], [21, 20], [21, 24], [21, 26], [21, 19], [21, 2], [21, 7], [22, 14], [22, 12], [22, 13], [22, 40], [22, 6], [23, 27], [23, 3], [23, 20], [23, 12], [23, 27], [23, 25], [23, 13], [23, 26], [23, 30], [24, 32], [24, 10], [24, 38], [25, 18], [25, 5], [25, 8], [25, 37], [25, 19], [25, 31], [25, 27], [26, 29], [26, 11], [26, 37], [27, 9], [27, 21], [27, 13], [27, 10], [27, 16], [27, 5], [27, 35], [27, 10], [27, 27], [28, 7], [28, 12], [28, 29], [28, 16], [28, 8], [29, 25], [29, 12], [29, 19], [29, 11], [29, 29], [29, 25], [29, 3], [29, 33], [30, 16], [30, 3], [30, 36], [30, 36], [30, 20], [30, 37], [30, 5], [30, 23], [30, 25], [31, 2], [32, 10], [32, 12], [32, 12], [32, 2], [32, 1], [33, 30], [33, 16], [33, 40], [33, 32], [33, 17], [33, 17], [33, 17], [33, 31], [34, 11], [34, 14], [35, 40], [35, 6], [35, 8], [35, 11], [35, 21], [35, 27], [35, 31], [35, 27], [36, 38], [36, 32], [36, 5], [37, 16], [37, 8], [37, 1], [37, 34], [37, 23], [37, 10], [37, 19], [37, 13], [37, 10], [38, 31], [38, 35], [38, 32], [38, 19], [38, 34], [39, 19], [39, 7], [39, 21], [39, 9], [40, 9], [40, 25], [40, 4], [40, 15], [40, 10], [41, 28], [41, 7], [41, 20], [41, 36], [41, 24], [41, 9], [41, 29], [41, 21], [41, 12], [41, 20], [41, 9], [41, 30], [41, 35], [42, 7], [42, 29], [42, 21], [43, 3], [43, 11], [43, 5], [43, 22], [43, 29], [44, 36], [44, 8], [44, 5], [44, 31], [44, 17], [44, 29], [44, 5], [44, 5], [44, 30], [44, 36], [45, 27], [45, 10], [45, 6], [45, 17], [45, 36], [45, 20], [45, 23], [46, 20], [46, 28], [47, 11], [47, 26], [47, 30], [47, 6], [47, 24], [47, 30], [47, 26], [47, 10], [48, 2], [48, 38], [48, 17], [48, 25], [48, 2], [48, 11], [49, 18], [49, 5], [49, 13], [49, 3], [49, 34], [50, 13], [50, 29], [50, 4], [50, 22], [50, 38], [50, 18], [50, 30], [50, 12], [50, 21]]))