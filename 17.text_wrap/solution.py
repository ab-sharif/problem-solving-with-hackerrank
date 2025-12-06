import textwrap

def wrap(string, max_width):
    stringlist = textwrap.wrap(string, max_width)
    return ("\n".join(stringlist))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)