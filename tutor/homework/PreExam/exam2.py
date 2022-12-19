patient = {'Andy':1,'Bill':2,'Alex':1,'Carl':3,'Frank':3}
room1 = []
room2 = []
room3 = []

for i in patient.keys():
    print(i)
    if patient[i] == 1 and len(room1) < 3:
        room1.append(i)
        # print(len(room1))
    elif patient[i] == 2 and len(room1) < 3:
        room2.append(i)
    elif patient[i] == 3 and len(room1) < 3:
        room3.append(i)

print("Room1 have {} | Room2 have {} | Room3 have {}".format(room1,room2,room3))