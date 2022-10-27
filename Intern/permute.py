def permute(inp):
    lsans = []
    inp.reverse()
    lsans.append(inp)

    for round in range(1,len(inp)-1):
        copyls = inp.copy()

        for i in range(len(inp)-1):
            if i != 0:
                copyls[i], copyls[i+1] = copyls[i +1], copyls[i]
                lsans.append(copyls.copy())
            newls = copyls.copy()
            for j in range(len(newls)-1):
                newls[j], newls[j+1] = newls[j+1], newls[j]
                lsans.append(newls.copy())

        if round < len(inp)-2:
            inp[round + 1], inp[round +2] = inp[round + 2], inp[round +1]
            lsans.append(inp.copy())
    return lsans

inp = list(map(int,input("input : ").split(',')))
op = permute(inp)
# print(op)
# k = []
# op = [list(i) for i in set([tuple(i) for i in op])]
# for i, e in enumerate(op):
#     print(e)
#     for o in range(i):
#         if e not in k:
#             k.append(e)
#         else:
#             pass
print('Original Cofllection: ', inp)
print('Collection of distinct numbers:')
print('', op)