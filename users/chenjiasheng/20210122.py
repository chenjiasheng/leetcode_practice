# http://3ms.huawei.com/km/groups/3803117/blogs/details/9753875?l=zh-cn


def get_self_insert_gain_table(digit):
    n = len(digit)
    gains = [(n, '0')] * n

    for i in range(1, n):
        for j in range(i, n):
            if digit[j - i] < digit[j]:
                break
            if digit[j - i] > digit[j]:
                gains[i] = (j, digit[j - i])
                break
    return gains


def string_compare(string, pattern_string):
    n = len(pattern_string)
    if len(string) < n:
        string = string + '/' * (n - len(string))

    result = n
    for i in range(n):
        if pattern_string[i] < string[i]:
            break
        if pattern_string[i] > string[i]:
            result = i
            break
    return result


def max_value_after_insert(score: str, digit: str):
    gains = get_self_insert_gain_table(digit)
    for i in range(len(score)):
        pos = string_compare(score[i:], digit)
        if pos is None:
            continue
        elif pos == len(digit):
            continue
        else:
            # 0: (pos, digit[pos])
            # pos: (pos, digit[0])
            _gains = [(pos, digit[pos])] + gains[1:pos]
            if pos != 0:
                _gains += [(pos, digit[0])]

            best_insert_pos = max(range(len(_gains)), key=lambda k: (-_gains[k][0], _gains[k][1]))
            return score[:i + best_insert_pos] + digit + score[i + best_insert_pos:]
    return score + digit


print(max_value_after_insert('123', '45'))
print(max_value_after_insert('789', '5434'))
print(max_value_after_insert('7894', '045'))
print(max_value_after_insert('456', '4567'))
print(max_value_after_insert('1231231234', '123'))

