ans = 0
num_at = 0

while True:
    for i in range(1,100):
        if ans > 2000:
            pass
        else:
            ans += i
            num_at = i
    break
ans = ans - num_at
num_at = num_at - 1
print(ans)
print(num_at)