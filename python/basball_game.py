#야구 게임
import random
times=3

#컴퓨터 랜덤 값
def getRandom():
    global times
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    randomValue = random.sample(list, times)
    comList = []
    for i in range(0, len(randomValue)):
        comList.append(int(randomValue[i]))
    return comList

#사용자 입력 값
def getUserInput():
    global times
    while(True):
        getNumber=input('[1부터 9까지] 숫자 {}개를 입력해주세요 -> '.format(times))
        if(len(getNumber)!=times):
            print("잘못된 입력입니다.\n")
            continue
        else:
            break
    userList=[]
    for i in range(0, times):
        userList.append(int(getNumber[i]))
    return userList

#스트라이크 체크
def chkStrike(comList, usrList, strikeCount):
    delIndex=[]
    for i in range(0, times):
        if (comList[i] == usrList[i]):
            strikeCount += 1
            delIndex.append(i)
    return strikeCount, delIndex

#볼 체크
def chkBall(comList, usrList, ballCount):
    for i in comList:
        for j in usrList:
            if i==j:
                ballCount+=1
    return ballCount

#스트라이크 된 숫자 삭제
def delStrikeNumber(comList, usrList, delIndex):
    for k in reversed(delIndex):
        del comList[k]
        del usrList[k]
    return comList, usrList

if __name__=='__main__':
    challengeCount=0
    while(True):
        challengeCount += 1  # 사용자 도전 횟수
        print("[{}]번 째 도전".format(challengeCount))
        comList = getRandom()
        usrList = getUserInput()
        print("컴퓨터 랜덤 값은 -> ", comList)  # 컴퓨터 숫자 리스트 comList
        print("사용자 입력 값은 ->", usrList)  # 사용자 숫자 리스트 usrList

        #스트라이크 체크
        strike = 0
        strike, delIndex=chkStrike(comList, usrList, strike)
        #스트라이크 된 숫자 삭제
        comList, usrList=delStrikeNumber(comList, usrList, delIndex)
        #볼 체크
        ball = 0
        ball=chkBall(comList, usrList, ball)

        print("결과는 {}스트라이크 {}볼 입니다.".format(strike, ball))

        if(challengeCount>=20 or strike==times):
            if(challengeCount ==20 and strike<times):
                print("{}번 동안 맞추지 못하였습니다. 게임에 소질이 없습니다.".format(challengeCount))
            elif(challengeCount>=0 and challengeCount<=5):
                print("{}번 만에 맞추셨습니다. 당신은 천재입니다.".format(challengeCount))
            elif (challengeCount >= 6 and challengeCount <= 10):
                print("{}번 만에 맞추셨습니다. 잘 하셨습니다.".format(challengeCount))
            elif (challengeCount >= 11 and challengeCount <= 15):
                print("{}번 만에 맞추셨습니다. 당신은 더 노력해야합니다.".format(challengeCount))
            elif (challengeCount >= 16):
                print("{}번 만에 맞추셨습니다. 게임에 소질이 없습니다.".format(challengeCount))
            break
        print('------------------------')