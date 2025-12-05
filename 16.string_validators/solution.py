if __name__ == '__main__':
    s = input()
    alnum = False
    alph = False
    digit = False
    lw = False
    up = False

    for c in s:
        if c.isalnum():
            alnum = True
        if c.isalpha():
            alph = True
        if c.isdigit():
            digit = True
        if c.islower():
            lw = True
        if c.isupper():
            up = True

    print(alnum, alph, digit, lw, up, sep="\n")