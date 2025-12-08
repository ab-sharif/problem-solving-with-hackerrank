c = '.|.'
msg = 'WELCOME'
n, m = list(map(int, input().split(' ')))

for i in range(1, n//2 +1):
    print( (c*(2*i-1)).center(m, '-'))

print(msg.center(m, '-'))

for i in range(n // 2, 0, -1):
    print( (c*(2*i-1)).center(m, '-'))