def Hash(pattern, text):
    p = 1000000007
    x = 263
    h_patt = 0
    result = []
    P = len(pattern) - 1
    for i in range(len(pattern)):
        h_temp = (ord(pattern[i]) % p * pow(x, i, p)) % p
        h_patt += h_temp
    h_patt = h_patt % p
    h_text = 0
    j = 0
    for i in range(len(text) - len(pattern), len(text)):
        h_temp = (ord(text[i]) % p * pow(x, j, p)) % p
        h_text += h_temp
        i = 0
        j += 1
    h_text = h_text % p
    j = len(text) - len(pattern)
    while j >= 0:
        flag = True
        if h_text == h_patt:
            while i < len(pattern) and flag:
                if pattern[i] != text[j+i]:
                    flag = False
                i += 1
            if flag:
                result.append(j)
        h_temp = ord(text[j + len(pattern) - 1]) % p * pow(x, P, p) % p
        j -= 1
        h_text = ((h_text - h_temp) * x + ord(text[j])) % p

    return result


def main():
    pattern = input()
    text = input()
    result = Hash(pattern, text)
    print(' '.join(str(result[i]) for i in range(len(result) - 1, -1, -1)))

main()
