# a company would like to know how much inventory exists in their closed inventory compartments. Given a string sconsisting of items as "*" and closed compartments as an open and close "|", an array of starting indices startIndices, and an array of ending indices endIndices, determine the number of items in closed compartments within the substring between the two indices, inclusive.

# An item is represented as an asterisk ('*' = ascii decimal 42)

# A compartment is represented as a pair of pipes that may or may not have items between them ('|' = ascii decimal 124).


def countItems(s, starts, ends):

    new_out = []
    temp = 0
    total = 0
    seen = False

    for val in s:
        if seen:
            if val == "|":
              if temp == 0:
                total = 0
              else:
                total += temp
              temp = 0
            else:
                temp += 1
            new_out.append(total)
        else:
          if val == '|':
            seen = True
          new_out.append(total)
    res = []
    print(new_out)
    for i in range(len(starts)):
        res.append(new_out[ends[i] - 1] - new_out[starts[i] - 1])
    return res

    # res = []
    # for i in range(len(starts)):
    #   splitted = (s[starts[i] - 1:ends[i]]).split('|')

    #   count = 0
    #   for value in splitted[1:-1]:
    #     count += len(value)
    #   res.append(count)

    # return res


# print(countItems("|**|*|*", [1, 1], [5, 6]))
# print(countItems("*|*|", [2], [3]))

# print(countItems("|***|*|**|*|*|", [10], [12]))

# print(countItems('******|******||***||||||||**|8|', [2, 7, 8], [9, 14, 20]))
print(countItems('*|*|*|', [1], [6]))
