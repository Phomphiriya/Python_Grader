n = int(input("Enter Number of Limit : "))
count = 0

if n <= 500:
    for c in range(1,n+1):
        for b in range(1,c+1):
            for a in range(1,b+1):
                if c*c == (a*a) + (b*b):
                    count += 1
    print(count)
else:
    print("Error")