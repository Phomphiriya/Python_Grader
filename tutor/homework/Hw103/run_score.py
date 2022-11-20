# 1.มีนักเรียน n คนมาวิ่ง สร้างลิสต์ขึ้นมาใหม่แล้วใช้วิธีการเพิ่มจาก input 
# นักเรียน n คน, แล้ว input คะแนนของ n คน เพิ่มเข้าไปนลิสต์แล้วให้วิเคราะห์
# คะแนนที่ดีที่สุดแล้ว output ออกมา เช่น
# input จำนวนนักเรียน n จากนั้นตั้งแต่ข้อมูลที่ 2 ไปจนถึง n+1 คือคะแนนของนักเรียน n
# output คะแนนที่ดีที่สุด

mem = int(input("Enter number of students : "))
score = []

for i in range(1,mem+1):
    mem_score = int(input("Enter {} score of student : ".format(i)))
    score.append(mem_score)
# print(score)
print("The Highest score is",max(score))