n = int(input()) # 3- 5000

if n == 4 or n == 7:
    print(-1)

else:
    n5 = n // 5
    m5 = n % 5
    
    if m5 == 0:
        print(n5)
    else:
        lst3 = [0, 2, 4, 1, 3]
        lst5 = [0, -1, -2, 0, -1]
        print((n5 + lst5[m5]) + lst3[m5])
