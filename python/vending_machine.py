#거스름돈 계산
def selectCalculate(ver, temp, dic, money):
    selected=temp.get(ver) #음료수 이름
    selectedPrice=dic.get(selected) #음료수의 가격

    if (money >= selectedPrice):
        print("{}을 선택하였습니다. 거스름 돈은 {}원 입니다.".format(selected, money-selectedPrice))
        money-=selectedPrice

#살 수 있는 음료수 재딕셔너리화
def selectList(dic, money):
    i=1
    temp={}
    for key, value in dic.items():
        if(int(money)>=int(value)):
            print("[{}]. {}({}원)".format(i, key, value))
            temp[i]=key #temp= { 1 : '물' , 2 : '우유'} ...
            i = i + 1

    ver = int(input('음료를 선택하세요 >'))
    selectCalculate(ver, temp, dic, money) #거스름돈 계산

# main start
dic = {'커피': 300, '물': 100, '주스': 700, '우유': 200}

while True:
    print("커피 {}원, 생수 {}원, 쥬스 {}원, 우유 {}원을 선택하실 수 있습니다.".format(dic['커피'], dic['물'], dic['주스'],dic['우유']))
    money = int(input('돈을 넣으세요 ->'))
    if (money<min(dic.values())):
        while True:
            money_add=int(input('돈이 부족합니다. 돈을 넣으세요 ->'))
            money+=money_add
            if(money>=min(dic.values())):
                break
    selectList(dic, money) #살수 있는 음료수 리스트

    more=input('추가 주문을 하시겠습니까? (Y/N) -> ')
    if(more=='N' or more=='n'):
        break
    else:
        print('------------------------------')


