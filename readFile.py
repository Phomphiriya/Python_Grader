import datetime
from typing import List

def date_to_ms(data: str):
    date_split = data.split("-")
    newDate = datetime.datetime(int(date_split[0]), int(date_split[1]), int(date_split[2]))
    return newDate.timestamp()


def sort_by_rank(data):
    str_ans = ""
    workingLis = sorted(data,key=lambda l:l[2], reverse=True)
    for i in workingLis:
        str_ans += " ".join(map(str, i))
        str_ans += "\n"
    return(str_ans)


def sort_by_date(date):
    str_ans = ""
    workingLis = sorted(date,key=lambda l:l[5], reverse=True)
    for i in workingLis:
        str_ans += " ".join(map(str, i[:][:-1]))
        str_ans += "\n"
    return(str_ans)

lis_all = []
lis_all_type = []

with open("df.txt","r") as file:
    data = file.readlines()
    for i in data:
        lis_all.append(i[:-2])
    # print(lis_all)
    # print(lis_all[0])

    for i in lis_all:
        a = i.split(" ")
        lis_all_type.append(a)
    # print(lis_all_type)

    # print(lis_all_type[0][0])
    # print(sort_by_rank(lis_all_type))
    for i in range(len(lis_all_type)):
        lis_all_type[i].append(date_to_ms(lis_all_type[i][0]))
    print(sort_by_date(lis_all_type))