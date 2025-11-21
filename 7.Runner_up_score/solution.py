if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    result = sorted(set(arr), reverse=True)[1]
    print(result)

