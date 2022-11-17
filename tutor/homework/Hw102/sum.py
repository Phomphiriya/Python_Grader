# 2.ให้ป้อนเลขทั้งหมดแล้วให้ผลลัพท์ออกมาบวกกัน เช่น
# อินพุต 123456789 เอ้าท์พุตให้เป็น 1+2+3+4+5+6+...+9=45
inp = input("Enter Input : ")
ans = 0
text = ""
for i in inp:
    text += i
    if i != inp[-1]:
        text += "+"
    ans += int(i)
print(text,"=",ans)