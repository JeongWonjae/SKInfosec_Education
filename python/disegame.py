import random

diseRes=[]
print("주사위를 던졌습니다.\n")
diseRes.append(random.randint(1,6))
diseRes.append(random.randint(1,6))
diseRes.append(random.randint(1,6))
print("나온 주사위 눈은 {},{},{} 입니다.".format(diseRes[0], diseRes[1],diseRes
[2]))

sameCount=0
sameNum=0

for i in range(0, len(diseRes)-1):
    for j in range(i+1, len(diseRes)):
        if(diseRes[i]==diseRes[j]):
            sameCount+=1
            sameNum=diseRes[i]
        else:
            continue

if(diseRes[0]==diseRes[1]==diseRes[2]):
    sameCount-=1

if (sameCount>0):
    print("{}개의 같은 눈이 나왔습니다.\n".format(sameCount+1))
else:
    print("같은 눈이 나오지 않았습니다.\n")

if(sameCount==2):
    award=10000+sameNum*1000
elif(sameCount==1):
    award=1000+sameNum*100
else:
    award=max(diseRes)*100

print("상금은 {}원 입니다.".format(award))

'''excute result
root@1d85a31b4b10:/home/pythonWork# python q2.py
주사위를 던졌습니다.

나온 주사위 눈은 5,5,3 입니다.
2개의 같은 눈이 나왔습니다.

상금은 1500원 입니다.
root@1d85a31b4b10:/home/pythonWork# python q2.py
주사위를 던졌습니다.

나온 주사위 눈은 3,4,2 입니다.
같은 눈이 나오지 않았습니다.

상금은 400원 입니다.
root@1d85a31b4b10:/home/pythonWork# python q2.py
주사위를 던졌습니다.

나온 주사위 눈은 2,2,2 입니다.
3개의 같은 눈이 나왔습니다.

상금은 12000원 입니다.
root@1d85a31b4b10:/home/pythonWork# python q2.py
주사위를 던졌습니다.

나온 주사위 눈은 6,2,5 입니다.
같은 눈이 나오지 않았습니다.

상금은 600원 입니다.
root@1d85a31b4b10:/home/pythonWork# python q2.py
주사위를 던졌습니다.

나온 주사위 눈은 6,4,3 입니다.
같은 눈이 나오지 않았습니다.

상금은 600원 입니다.

'''
