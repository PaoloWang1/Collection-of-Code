def str_count(str_text, pattern):
    if len(str_text) == 0:
        return 0

    length = len(pattern)
    num = 0
    if str_text[:length] == pattern:
        num += 1

    num += str_count(str_text[1:], pattern)

    return num

print(str_count("aaaaaaaaaaaaaaaa", "aa"))
