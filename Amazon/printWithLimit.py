def printWithLimit(arr, limit):
  allLines = []
  arrJoin = ','.join(map(str,arr))
  eachLine = ''
  currentIter = ''
  currentLimt = 0
  for eachChar in arrJoin:
    if currentLimt < limit:
      if eachChar != ',':
        currentIter += eachChar
        currentLimt += 1
      else:
        currentIter += eachChar
        eachLine += currentIter
        currentIter = ''
        currentLimt += 1
    else:
      if eachChar != ',':
        allLines.append(eachLine)
        currentIter += eachChar
      else:
        currentIter += eachChar
        eachLine += currentIter
        allLines.append(eachLine)
        currentIter = ''
      eachLine = ''
      currentLimt = 0
  print(allLines)

print(printWithLimit([23, 14, 317, 49, 8], 6))
