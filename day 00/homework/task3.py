def task3(a,b,c,d,e):
    num = a 

    if b > num:
        num = b
    if c > num:
        num = c
    if d > num:
        num = d 
    if e > num:
        num = e
    return num 

print(task3(11, 22, 0, 0, 0))
print(task3(1,2,3,4,5))
print(task3(2,8,3,4,11))
print(task3(2,42,3,12,8))
print(task3(2,21,63,9,9))

# გამოიკვლიეთ მასივში მაქსიმუმის მოძებნის ამოცანა 5
#  ელემენტის შემთხვევაში (ვარიანტისთვის [4]3გვ:21ეგვ): 
#დაწერეთ
# ფსევდოკოდი, ბლოკ-სქემა, ანალიზი