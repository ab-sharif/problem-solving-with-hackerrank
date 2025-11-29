def count_substring(string, sub_string):
    start = 0
    end = len(sub_string)
    counter = 0

    while end <= len(string):
        if sub_string == string[start:end]:
            counter += 1
        start += 1
        end += 1
    return counter


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)