# -*- coding: utf-8 -*-
import pymysql
import random
import datetime
from beautifultable import BeautifulTable
import requests

valueList = []


def get_weekday(num):
    if (num == 0):
        return "Mon"
    elif (num == 1):
        return 'Tue'
    elif (num == 2):
        return 'Wen'
    elif (num == 3):
        return 'Thr'
    elif (num == 4):
        return 'Fri'
    elif (num == 5):
        return 'Sat'
    elif (num == 6):
        return 'Sun'


if __name__ == '__main__':

    print('''
ZZZZZZZZZZZZZZ9zE95w, W WjWyw wW,jBEZ8ZZZZZZZZZZZZZZZ
ZZZZZZZZZZZZZwZ8   W,   WZZZ    ,w   98jZZZZZZZZZZZZZ
ZZZZZZZZZZZE Z   wZZZZ         ZZZZ   ,Z ZZZZZZZZZZZZ
ZZZZZj    EyZB y5ZZZZZZ9EEEEE9ZZZZZZzj 9ZjZ    8ZZZZZ
ZZZZZZZZZ     y5w                   Wyj     ZZZZZZZZZ
ZZZZZZZ9    ,      , y5jjjWWjjy, w,,,,,W  ,  ZZZZZZZZ
ZZZZZD  ZZz8WZE98888zy9988zzBzB 5yjjjy5D yzBy  zZZZZZ
ZZZZW  ZZ5zZBWj5jjWWyy Wj95E55 yB555yDD DZzDZj  BZZZZ
ZZZZ  Ww,j 5 wyZZZZZZZ5wZEjZZWjZZZZZZZB, zwyy,z WZZZZ
ZZZZ   8EZEZZZ yZZZZZZZ5,ZZZ WZZZZZZZy ZZZzz8j   ZZZZ
ZZZZjZz                                      w9 ZZZZZ
ZZZZ  WWW                                   WWW  ZZZZ
ZZZZ  ZWzZZZZ ZZZZZZZZZZZZZZZZZZZZZZZZZ ZZZZ9yZ  ZZZZ
ZZZZW ZZZZZZ wZZZZEZZZZZZZZZZZZZZZEZZZZ  ZZZZZZ zZZZZ
ZZZZj        ZZ99E98z8BDDBBz8zzzz89E99ZZ        WZZZZ
ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
    ''')

    # conn = pymysql.connect(host='project-car.comzsnafugrl.us-east-2.rds.amazonaws.com', port=3306, user='admin',password='rlatjrwn123', db='car', charset='utf8')
    # curs = conn.cursor()

    while True:
        try:
            mainmenu = '메 인 메 뉴'
            print(mainmenu.center(50, "#"))
            cmd = int(input('1) 고객 2) 자동차 3) 구매 4) 서비스 5) 종료->'))
        except:
            print('다시 입력 해주세요')
            continue
        if cmd == 1:
            while True:
                sidemenu = '고 객 메 뉴'
                print(sidemenu.center(40, "-"))
                customer = int(input('1) 가입 2) 조회 3) 수정 4) 탈퇴 5) 메인으로 ->'))

                if customer == 1:  # 가입
                    # id 생성
                    custid_f = 'C'
                    URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/getId?tName=customer&tAttr=customer_id&pLen=1"
                    response = requests.get(URL)
                    res = response.json()

                    if (res is None):
                        custid = 'C0001'
                    else:
                        custid_b = res[0]['id']
                        custid = custid_f + custid_b

                    custinfo = input('이름,번호,주소를 입력해주세요 *한글 또는 영어로 입력(,로 구분)*->').split(',')
                    URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/addCustomer?custid=" + custid + "&name=" + \
                          custinfo[0] + "&phone=" + str(custinfo[1]) + "&addr=" + custinfo[2]
                    response = requests.get(URL)
                    # http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/addCustomer?custid=C0030&name=wonjae&phone=010&addr=seoul
                elif customer == 2:  # 조회
                    URL = 'http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/customers'
                    response = requests.get(URL)
                    res = response.json()
                    table = BeautifulTable()
                    table.columns.header = ["고객 ID", "이름", "전화번호", "주소"]
                    valueList = []
                    for i in range(len(res)):
                        for key, value in res[i].items():
                            valueList.append(str(value))
                        table.rows.append([valueList[0], valueList[1], valueList[2], valueList[3]])
                        del valueList[:]
                    print(table)
                elif customer == 3:  # 수정

                    custid = input('고객아이디를 입력해주세요 ex)C0001 ->').upper()
                    URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/customer?id=" + custid
                    response = requests.get(URL)
                    res = response.json()

                    if (res is None):
                        print("존재하지 않는 고객입니다.")
                        break
                    else:
                        del valueList[:]
                        table = BeautifulTable()
                        table.columns.header = ["고객 ID", "이름", "전화번호", "주소"]
                        for key, value in res[0].items():
                            valueList.append(str(value))
                        table.rows.append([valueList[0], valueList[1], valueList[2], valueList[3]])
                        print(table)

                    select = int(input('수정할 정보를 선택해주세요 1)이름 2)핸드폰번호 3)주소->'))
                    while (True):
                        if select == 1:  # 이름 수정
                            new_name = input('변경할 이름을 입력하세요 ->')
                            URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/updateCustomer?type=customer_name&content=" + new_name + "&id=" + custid
                            response = requests.get(URL)
                            break
                        elif select == 2:  # 번호 수정
                            new_phone = input('변경할 번호를 입력하세요 ->')
                            URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/updateCustomer?type=phone_number&content=" + new_phone + "&id=" + custid
                            response = requests.get(URL)
                            break
                        elif select == 3:  # 주소 수정
                            new_address = input('변경할 주소를 입력하세요 ->')
                            URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/updateCustomer?type=address&content=" + new_address + "&id=" + custid
                            response = requests.get(URL)
                            break
                        else:
                            print("번호를 잘못 입력하였습니다.")
                            break
                elif customer == 4:
                    custid = input('삭제할 고객아이디를 입력해주세요 ex)C0001 ->').upper()
                    URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/customer?id=" + custid
                    response = requests.get(URL)
                    res = response.json()

                    if (res is None):
                        print("존재하지 않는 고객입니다.")
                        break
                    else:
                        del valueList[:]
                        table = BeautifulTable()
                        table.columns.header = ["고객 ID", "이름", "전화번호", "주소"]
                        for key, value in res[0].items():
                            valueList.append(str(value))
                        table.rows.append([valueList[0], valueList[1], valueList[2], valueList[3]])
                        print(table)

                    try:
                        URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/customerdelete?id=" + custid
                        response = requests.get(URL)
                        print("성공적으로 삭제되었습니다.")
                    except:
                        print("삭제에 실패하였습니다.")

                elif customer == 5:
                    break
                else:
                    print("번호를 잘못 입력하였습니다.")
        elif cmd == 2:
            while True:
                sidemenu = '자 동 차 메 뉴'
                print(sidemenu.center(40, "-"))
                car = int(input('1) 추가 2) 조회 3) 수정 4) 삭제 5) 메인메뉴로->'))

                if car == 1:  # 추가
                    # 자동차 아이디 생성
                    carid_f = 'CAR'
                    URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/getId?tName=car_menu&tAttr=car_id&pLen=3"
                    response = requests.get(URL)
                    res = response.json()

                    if (res is None):
                        carid = 'CAR0001'
                    else:
                        carid_b = res[0]['id']
                        carid = carid_f + carid_b

                    carinfo = input('모델명,색,상태(NEW|OLD),일련번호,제작년도,가격 *한글 또는 영어로 입력(,로 구분)*->').split(',')
                    URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/addCar?carid=" + carid + "&model=" + \
                          carinfo[0] + "&color=" + str(carinfo[1]) + "&status=" + carinfo[2] + "&number=" + carinfo[
                              3] + "&year=" + carinfo[4] + "&price=" + carinfo[5]
                    response = requests.get(URL)
                elif car == 2:  # 조회

                    URL = 'http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/cars'
                    response = requests.get(URL)
                    res = response.json()
                    if (res is None):
                        print('자동차 제고가 없습니다')
                    else:
                        print("구매 가능한 자동차 목록 입니다.")
                        table = BeautifulTable()
                        table.columns.header = ["자동차 ID", "모델명", "색상", "상태", '일련번호', '제작년도', '가격']
                        valueList = []
                        for i in range(len(res)):
                            for key, value in res[i].items():
                                valueList.append(str(value))
                            table.rows.append(
                                [valueList[0], valueList[1], valueList[2], valueList[3], valueList[4], valueList[5],
                                 valueList[6]])
                            del valueList[:]
                        print(table)
                elif car == 3:  # 수정

                    carid = input('자동차 아이디를 입력해주세요 ex)CAR0001 ->').upper()
                    URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/car?id=" + carid
                    response = requests.get(URL)
                    res = response.json()

                    if (res is None):
                        print("존재하지 않는 자동차입니다.")
                        break
                    else:
                        del valueList[:]
                        table = BeautifulTable()
                        table.columns.header = ["자동차 ID", "모델명", "색상", "상태", '일련번호', '제작년도', '가격']
                        for key, value in res[0].items():
                            valueList.append(str(value))
                        table.rows.append(
                            [valueList[0], valueList[1], valueList[2], valueList[3], valueList[4], valueList[5],
                             valueList[6]])
                        print(table)

                    select = int(input('수정할 정보를 선택해주세요 1)모델명 2)색상 3)상태(NEW|OLD) 4)가격 ->'))
                    while (True):
                        if select == 1:  # 모델명
                            new_car_model = input('변경할 모델명을 입력하세요 ->')
                            URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/updateCar?type=car_model&content=" + new_car_model + "&id=" + carid
                            response = requests.get(URL)
                            break
                        elif select == 2:  # 색
                            new_color = input('변경할 색상을 입력하세요 ->').upper()
                            URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/updateCar?type=car_color&content=" + new_color + "&id=" + carid
                            response = requests.get(URL)
                            break
                        elif select == 3:  # 상태
                            new_state = input('변경할 상태를 입력하세요(NEW|OLD) ->').upper()
                            URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/updateCar?type=new_old_state&content=" + new_state + "&id=" + carid
                            response = requests.get(URL)
                            break
                        elif select == 4:  # 가격
                            new_price = input('변경할 가격을 입력하세요 ->')
                            URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/updateCar?type=car_price&content=" + new_price + "&id=" + carid
                            response = requests.get(URL)
                            break
                        else:
                            print("번호를 잘못 입력하였습니다.")
                            break
                elif car == 4:  # 삭제

                    carid = input('삭제할 자동차 아이디를 입력해주세요 ex)CAR0001 ->').upper()
                    URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/car?id=" + carid
                    response = requests.get(URL)
                    res = response.json()

                    if (res is None):
                        print("존재하지 않는 자동차입니다.")
                        break
                    else:
                        del valueList[:]
                        table = BeautifulTable()
                        table.columns.header = ["자동차 ID", "모델명", "색상", "상태", '일련번호', '제작년도', '가격']
                        for key, value in res[0].items():
                            valueList.append(str(value))
                        table.rows.append(
                            [valueList[0], valueList[1], valueList[2], valueList[3], valueList[4], valueList[5],
                             valueList[6]])
                        print(table)

                    try:
                        URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/cardelete?id=" + carid
                        response = requests.get(URL)
                        print("성공적으로 삭제되었습니다.")
                    except:
                        print("삭제에 실패하였습니다.")

                elif car == 5:
                    break
                else:
                    print("번호를 잘못 입력하였습니다.")
        elif cmd == 3:
            while True:
                '''
                #직원이 고객에게 보여주면서 판매하는 시나리오 
                #1. 자동차 목록을 보여준다.
                #2. 직원번호를 입력 
                #3. 사용자 아이디를 입력 받는다. 
                #4. 사용자가 자동차를 골라 id로 (오더 테이블 저장)
                #5. 결제생략-> 송장을 보여줘 (송장 테이블 저장)
                '''
                # 1 - 구매 가능한 자동차 조회
                URL = 'http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/cars'
                response = requests.get(URL)
                res = response.json()
                if (res is None):
                    print('자동차 제고가 없습니다')
                else:
                    print("구매 가능한 자동차 목록 입니다.")
                    table = BeautifulTable()
                    table.columns.header = ["자동차 ID", "모델명", "색상", "상태", '일련번호', '제작년도', '가격']
                    valueList = []
                    for i in range(len(res)):
                        for key, value in res[i].items():
                            valueList.append(str(value))
                        table.rows.append(
                            [valueList[0], valueList[1], valueList[2], valueList[3], valueList[4], valueList[5],
                             valueList[6]])
                        del valueList[:]
                    print(table)
                car_select_chk = 0
                car_select = input('구매할 자동차를 선택해주세요. ex)CAR0001 ->').upper()

                # 2 - 직원 선택
                salesid = input('직원번호를 입력해주세요 ex)S0001 ->').upper()
                URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/salesperson?id=" + salesid
                response = requests.get(URL)
                res = response.json()
                try:
                    del valueList[:]
                    print("직원 정보를 확인합니다.")
                    table = BeautifulTable()
                    table.columns.header = ["직원 ID", "이름", "전화번호", "이메일"]
                    for key, value in res[0].items():
                        valueList.append(str(value))
                    table.rows.append([valueList[0], valueList[1], valueList[2], valueList[3]])
                    print(table)
                except:
                    print("존재하지 않는 직원입니다.")
                    break

                # 3 - 고객아이디 입력
                custid = input('고객아이디를 입력해주세요 ex)C0001 ->').upper()
                URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/customer?id=" + custid
                response = requests.get(URL)
                res = response.json()
                try:
                    del valueList[:]
                    table = BeautifulTable()
                    table.columns.header = ["고객 ID", "이름", "전화번호", "주소"]
                    for key, value in res[0].items():
                        valueList.append(str(value))
                    table.rows.append([valueList[0], valueList[1], valueList[2], valueList[3]])
                    print(table)
                except:
                    print("존재하지 않는 고객입니다.")
                    break

                # 4 - 주문 내역 생성
                orderid_f = 'O'
                URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/getId?tName=order_details&tAttr=order_id&pLen=1"
                response = requests.get(URL)
                res = response.json()

                if (res is None):
                    orderid = 'O0001'
                else:
                    orderid_b = res[0]['id']
                    orderid = orderid_f + orderid_b

                # 가격 조회
                URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/carprice?carid=" + car_select
                response = requests.get(URL)
                res = response.json()
                car_price = res[0]['car_price']

                # 주문내용 저장
                try:
                    URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/addOrder?orderid=" + orderid + "&custid=" + custid + "&carid=" + car_select + "&carprice=" + str(
                        car_price)
                    response = requests.get(URL)
                except:
                    print("자동차 구매에 실패하였습니다.")
                    break

                # 5 - 결제생략, 송장 생성 및 출력
                invoiceid_f = 'I'
                URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/getId?tName=sales_invoice&tAttr=invoice_id&pLen=1"
                response = requests.get(URL)
                res = response.json()

                if (res is None):
                    invoiceid = 'I0001'
                else:
                    invoiceid_b = res[0]['id']
                    invoiceid = invoiceid_f + invoiceid_b

                URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/addInvoice?invoiceid=" + invoiceid + "&custid=" + custid + "&salesid=" + salesid + "&orderid=" + orderid
                response = requests.get(URL)
                print("(+) 구매가 완료되었습니다.")

                # 송장 출력
                # 고객 id, 자동차 정보, 판매직원, 가격,
                URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/lookupInvoice?invoiceid=" + invoiceid
                response = requests.get(URL)
                res = response.json()

                print("(+) 송장이 발급되었습니다. 송장번호 : ", invoiceid)
                table = BeautifulTable()
                table.columns.header = ["고객 이름", "자동차 모델", "색상", "상태", "일련번호", "제작년도", "가격", "판매 직원이름"]
                del valueList[:]
                for key, value in res[0].items():
                    valueList.append(str(value))
                table.rows.append(
                    [valueList[0], valueList[1], valueList[2], valueList[3], valueList[4], valueList[5], valueList[6],
                     valueList[6]])
                print(table)
                break
        elif cmd == 4:
            while True:
                sidemenu = '서 비 스 메 뉴'
                print(sidemenu.center(40, "-"))
                try:
                    service = int(input('1) 서비스 신청 2) 서비스 기록 조회 3) 메인으로 ->'))
                except:
                    print("메인으로 돌아갑니다.")
                    break
                '''
                #1 고객아이디를 받거나 없으면 가입하고 오라고 알랴줌
                    1. 서비스를 보여줌
                    2. 서비스 yes or no?
                        3. product가 필요하면 product_parts를 보여줌 
                        4. product_parts를 선택
                    5. 서비스 받을 요일을 입력받음
                    6. 요일에 가능한 메카닉을 보여줌
                    7. 메카닉 선택
                    8. service_records에 데이터베이스 저장, 서비스 티켓 없으면 발행
                    9. 
                '''
                if (service == 1):
                    custid = input('고객아이디를 입력해주세요 ex)C0001 ->').upper()
                    URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/customer?id=" + custid
                    response = requests.get(URL)
                    res = response.json()
                    del valueList[:]
                    table = BeautifulTable()
                    table.columns.header = ["고객 ID", "이름", "전화번호", "주소"]
                    for key, value in res[0].items():
                        valueList.append(str(value))
                    table.rows.append([valueList[0], valueList[1], valueList[2], valueList[3]])
                    print(table)
                    if (res is None):
                        print("가입 후에 사용 가능합니다.")
                        break
                    else:

                        print("\n서비스 목록 입니다.")

                        URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/service"
                        response = requests.get(URL)
                        res = response.json()
                        table = BeautifulTable()
                        table.columns.header = ["서비스 ID", "서비스 이름", "가격", "부품 필요 여부"]

                        del valueList[:]
                        for i in range(len(res)):
                            for key, value in res[i].items():
                                valueList.append(str(value))
                            table.rows.append([valueList[0], valueList[1], valueList[2], valueList[3]])
                            del valueList[:]
                        print(table)

                        service_answer = input("서비스를 받으시겠습니까? (Y/N)->").lower()
                        if (service_answer == 'y'):
                            service_select = input("서비스를 선택해주세요 ex)SV0001->").upper()
                            URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/serviceChoice?id=" + service_select
                            response = requests.get(URL)
                            res = response.json()
                            try:
                                if (res[0]['need_product'] == 'Y'):
                                    # tire / handle
                                    URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/serviceChoice/yes?id=" + service_select

                                    response = requests.get(URL)
                                    res = response.json()
                                    table = BeautifulTable()
                                    del valueList[:]
                                    for i in range(len(res)):
                                        for key, value in res[i].items():
                                            valueList.append(str(value))
                                        table.rows.append([valueList[i]])
                                    print(table)

                                    select_product = input("부품 종류를 선택하세요 ex)Tire ->")

                                    # 파츠 보여주는거
                                    select_product = '%' + select_product
                                    try:
                                        print("\n부품 목록 입니다.")
                                        URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/parts?parts_name=" + select_product
                                        response = requests.get(URL)
                                        res = response.json()
                                        table = BeautifulTable()
                                        table.columns.header = ["부품 ID", "부품 상세 종류", "가격"]
                                        del valueList[:]
                                        for i in range(len(res)):
                                            for key, value in res[i].items():
                                                valueList.append(str(value))
                                            table.rows.append([valueList[0], valueList[1], valueList[2]])
                                            del valueList[:]
                                        print(table)
                                    except:
                                        print("부품 종류 선택이 잘못되었습니다.")
                                        break

                                    select_parts = input("부품을 선택하세요 ex)PA0001->").upper()
                                    select_product = select_product.replace('%', '')

                                    URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/product?id=" + select_parts
                                    response = requests.get(URL)
                                    res = response.json()
                                    table = BeautifulTable()
                                    del valueList[:]
                                    for i in range(len(res)):
                                        for key, value in res[i].items():
                                            valueList.append(str(value))
                                        table.rows.append([valueList[i]])
                                    print(table)
                                else:  # N 파츠없을때
                                    select_parts = ''
                                    select_product = ''
                            except:
                                print("서비스 선택이 잘못되었습니다.")
                                break

                            # 사용자  요일 함수
                            day = input("서비스 받을 날짜를 입력해주세요 ex)2020.02.20 ->")
                            day_list = []
                            day_list = day.split('.')
                            service_day = datetime.datetime(int(day_list[0]), int(day_list[1]),
                                                            int(day_list[2])).weekday()
                            service_day_weekday = get_weekday(int(service_day))  # Mon~Sun이 반환됨
                            print('서비스 날짜', day, '는 ', service_day_weekday, '입니다.')

                            # 요일 비교해서 가능한 메카닉만 출력해줌
                            URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/lookupMechanics"
                            response = requests.get(URL)
                            res = response.json()
                            print("\n서비스 가능한 메카닉 목록입니다.")

                            table = BeautifulTable()
                            table.columns.header = ["메카닉 ID", "전화번호", "이메일", "이름", "서비스 가능 요일"]
                            del valueList[:]
                            meca_chk = []
                            for i in range(len(res)):
                                for key, value in res[i].items():
                                    valueList.append(str(value))
                                weekday_list = []
                                weekday_list = valueList[5].split(' ')
                                for j in weekday_list:
                                    if (service_day_weekday == j):
                                        table.rows.append(
                                            [valueList[0], valueList[1], valueList[2], valueList[3], valueList[4]])
                                        meca_chk.append(valueList[0])
                                        break
                                del valueList[:]
                            print(table)

                            mecha_select_list = []
                            mecha_select = input("메카닉을 선택해주세요 (중복선택 가능) ex)M0001,M0002->").upper()

                            try:
                                if (',' in mecha_select):
                                    mecha_select_list = mecha_select.split(',')
                                else:
                                    mecha_select_list.append(mecha_select)
                            except:
                                print("메카닉 선택이 잘못되었습니다.")
                                break

                            _break = True
                            for i in mecha_select_list:
                                meca_chk_num = 0
                                for j in meca_chk:
                                    if (i == j):
                                        meca_chk_num += 1
                                if (meca_chk_num == 0):
                                    print("메카닉 선택이 잘못되었습니다.")
                                    _break = False
                                    break
                            if (_break == False):
                                break

                            # 서비스 아이디 생성
                            service_record_id_f = 'SR'
                            URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/getId?tName=service_records&tAttr=service_record_id&pLen=2"
                            response = requests.get(URL)
                            res = response.json()

                            if (res[0]['id'] == None):
                                service_record_id = 'SR0001'
                            else:
                                service_record_id_b = res[0]['id']
                                service_record_id = service_record_id_f + str(service_record_id_b)

                            # 서비스 티켓 확인
                            URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/lookupTicket?custid=" + custid
                            response = requests.get(URL)
                            res = response.json()

                            # 서비스 티켓 생성
                            if (len(res) < 1):
                                # 서비스 티켓 처음 발급
                                while (True):
                                    service_ticket = ''
                                    for i in range(0, 10):
                                        service_ticket += str(random.randint(1, 9))
                                    URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/checkTicket?ticket=" + service_ticket
                                    response2 = requests.get(URL)
                                    res2 = response2.json()
                                    if (len(res2) < 1):
                                        break
                                    else:
                                        continue
                            else:  # 서비스 티켓이 이미 존재
                                service_ticket = res[0]['service_ticket_id']

                            # 서비스 레코드 테이블 데이터 저장
                            if (select_product==''):
                                URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/addServiceRecords?serviceid=" + service_record_id + "&serviceselect=" + service_select + "&ticket=" + service_ticket + "&day=" + day + "&custid=" + custid
                                response = requests.get(URL)
                            else:
                                try:
                                    URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/addServiceRecords_parts?serviceid=" + service_record_id + "&serviceselect=" + service_select + "&selectparts=" + select_parts + "&ticket=" + service_ticket + "&day=" + day + "&custid=" + custid
                                    response = requests.get(URL)
                                except:
                                    print("잘못된 서비스 신청입니다.")
                                    break

                            # management 테이블
                            try:
                                for i in mecha_select_list:
                                    URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/addManagement?mecaid=" + i + "&serviceid=" + service_record_id
                                    response = requests.get(URL)
                            except:
                                print("서비스 신청에 실패하였습니다.")
                                break

                            print("서비스 신청이 완료되었습니다.")
                            # 서비스 신청 메카닉이름, 날짜, 서비스 이름, 고객 이름
                            print("서비스 신청 내역입니다.\n")
                            resultstr = '서비스 신청 내역'
                            print(resultstr.center(50, "-"))
                            # 서비스 신청 결과 출력

                            print("- 서비스 아이디 : ", service_record_id)

                            URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/service/getMecanic?serviceid=" + service_record_id
                            response = requests.get(URL)
                            res = response.json()

                            mecaList = []
                            del mecaList[:]
                            for j in range(len(res)):
                                for key, value in res[j].items():
                                    mecaList.append(str(value))

                            mecas = ' '.join(mecaList)
                            print("- 서비스 할 기술자 : ", mecas)
                            print("- 서비스 날짜 : ", day)

                            URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/service/getName?serviceid=" + service_record_id
                            response = requests.get(URL)
                            res = response.json()
                            print("- 서비스 이름 : ", res[0]['service_name'])
                            print("- 보유중인 서비스 티켓 번호 : ", service_ticket)

                            # custid로 네임가져오기
                            URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/service/getCustName?serviceid=" + service_record_id
                            selectSQL = "SELECT c.customer_name FROM customer c, service_records sr WHERE c.customer_id=sr.customer_customer_id AND sr.service_record_id=%s"
                            response = requests.get(URL)
                            res = response.json()
                            print("- 고객 이름 : ", res[0]['customer_name'])
                            resultstr = ''
                            print(resultstr.center(60, "-"))
                            print('\n')

                elif (service == 2):  # 서비스 기록 조회
                    # 고객 id로 조회
                    # 서비스_레코즈 테이블에서
                    #
                    custid = input('고객 아이디를 입력해주세요 ex)C0001->').upper()
                    print("\n모든 서비스 기록을 조회합니다.")

                    URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/lookupService?custid=" + custid
                    response = requests.get(URL)
                    res = response.json()

                    table = BeautifulTable()
                    table.columns.header = ["서비스 기록 ID", "티켓  ID", "서비스 날짜", "부품 종류", "세부 부품", "부품 가격", "서비스 이름",
                                            "서비스 가격", "메카닉 이름"]
                    valueList = []

                    for i in range(len(res)):
                        for key, value in res[i].items():
                            valueList.append(str(value))

                        # 서비스 기록 가져옴
                        URL = "http://module-project2-lb-167245876.us-east-2.elb.amazonaws.com:8000/lookupMechanic?serviceid=" + \
                              valueList[0]
                        response2 = requests.get(URL)
                        res2 = response2.json()

                        # 예약된 메카닉 조회
                        mecaList = []
                        for j in range(len(res2)):
                            for mkey, mvalue in res2[j].items():
                                mecaList.append(str(mvalue))
                        mecas = ' / '.join(mecaList)
                        table.rows.append(
                            [valueList[0], valueList[3], valueList[4], valueList[7], valueList[8], valueList[9],
                             valueList[10], valueList[11], mecas])
                        del valueList[:]
                        del mecaList[:]
                    print(table)

                else:
                    print("메인으로 돌아갑니다.")
                    break
        elif cmd == 5:
            # conn.close()
            break
        else:
            print('잘못 선택하셨습니다.')