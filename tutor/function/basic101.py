## String
s = "This is a string"
# print(s[-5:-1])

## List
a = [1, 2.2, 'python'] ## List 1D (multi data type)
b = [5,10,15,20,25,30,35,40] ## List 1D
c = [[1,2,3],4,5,6] ## List 2D
# print(a)
# print(type(a[2])) ## แสดง type ของตัวแปรนั้นๆ
# print(b[0:2])
# print(c[0][0])
# b[0] = 4 ## สามารถเปลี่ยนแปลงได้
# print(b[0])
print(a)
a.append("easy") ## เพิ่มค่าเข้าไปด้านหลัง
print(a)
a.insert(1,"makmak") ## แทรกค่าไปตำแหน่งนั้นๆ
print(a)
a.remove(2.2) ## เอาคำนั้นๆออก
print(a)
a.pop(1) ## เอาค่าตำแหน่งนั้นๆออก
print(a)

## Tuple
t = (5, "program", 1.5)
# t[0] = 1 ## ไม่สามารถเปลี่ยนแปลงได้
# print(t[0])

## Set
se = {1,2,2,3,3,3,3,3,3,4,5} ## เลขเดียวกันจะถือว่าเป็นเลขตัวเดียวกัน
# print(se)

## Dictionary
d = { "brand": "Ford", "model": "mustang","year": 1964, "color": ["red", "white"] }
# print(d["color"])