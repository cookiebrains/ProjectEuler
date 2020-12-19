
maxp = 0
for i in range(100, 1000):
    for j in range(i, 1000):
        p = i * j
        if str(p) == str(p)[::-1] and p > maxp:
            maxp = p

print(maxp)
