def string_in(string, pattern):
    yes = False
    string = list(string)
    pattern = list(pattern)
    for x in range(len(string) - len(pattern)+1):
        if string[x:x+len(pattern)] == pattern:
            yes = True
        else:
            yes = False
            
    print(yes)
