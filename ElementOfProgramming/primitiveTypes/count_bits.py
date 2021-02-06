def count(value):
    num = 0
    while value:
        print('the value of: {}'.format(value))
        num += value & 1
        value >>= 1

    return num


print(count(12))  # 1100
# print(count(15))  # 1111
