def reorganizeString(S):
    if S is None:
        return ''
    len_str = len(S)
    if len_str <= 1:
        return S
    if len_str == 2 and S[0] == S[1]:
        return ''
    
    split_str = sorted(S)

    i = 1
    should_arr = False
    while i < len_str and not should_arr:
        if split_str[i - 1] == split_str[i]:
            print("reached")
            should_arr = True
            j = i + 1
            while j < len_str:
                if split_str[i] != split_str[j]:
                    
                    split_str[i], split_str[j] = split_str[j], split_str[i]
                    print(split_str)
                    should_arr = False
                    break
                else:
                    j += 1
        else:
            i += 1
                    
    if should_arr:
        return 'No result'
    else:
        return ''.join(split_str)

print(reorganizeString('vvvlo'))