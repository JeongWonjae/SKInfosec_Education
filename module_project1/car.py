import pymysql
import random
import datetime

def get_weekday(num):
    if(num==0): return "Mon"
    elif(num==1): return 'Tue'
    elif(num==2): return 'Wen'
    elif(num==3): return 'Thr'
    elif(num==4): return 'Fri'
    elif(num==5): return 'Sat'
    elif(num==6): return 'Sun'


if __name__=='__main__':

    conn = pymysql.connect(host='mysql',
                port=3306,
                user='root',
                password='mysql',
                db='car',
                charset='utf8')
    curs = conn.cursor()


    while True:
        try:
            mainmenu='메 인 메 뉴'
            print(mainmenu.center(40, "#"))
            cmd = int(input('1) 고객 2) 자동차 3) 구매 4) 서비스 5) 종료->'))
        except:
            print('다시 입력 해주세요')
            continue
        if cmd == 1:
                while True:
                    sidemenu='고 객 메 뉴'
                    print(sidemenu.center(40, "-"))
                    customer = int(input('1) 가입 2) 조회 3) 수정 4) 탈퇴 5) 메인으로 ->'))

                    if customer==1: #가입
                        #id 생성
                        selectSQL="select customer_id from customer limit 1"
                        curs.execute(selectSQL)
                        fetch_data = curs.fetchone()
                        
                        if(fetch_data is None):
                            custid='C0001'
                        else:
                            custid_f='C'
                            selectSQL="select lpad(max(convert(substr(customer_id,2,5),signed)+1),4,0) from customer"
                            curs.execute(selectSQL)
                            fetch_data = curs.fetchone()
                            custid_b=fetch_data[0]
                            custid=custid_f+custid_b

                        custinfo=input('이름,번호,주소를 입력해주세요 *한글 또는 영어로 입력(,로 구분)*->').split(',')
                        insertSQL = "insert into customer values(%s,%s,%s,%s)"
                        curs.execute(insertSQL, (custid,custinfo[0], custinfo[1], custinfo[2]))
                        conn.commit()

                    elif customer==2: #조회
                        selectSQL="select * from customer"
                        rows = curs.execute(selectSQL)
                        for row in curs.fetchall():
                            print(row)

                    elif customer==3: #수정
                        custid=input('고객아이디를 입력해주세요 ex)C0001 ->').upper()
                        selectSQL="select * from customer where customer_id=%s"
                        curs.execute(selectSQL, (custid))
                        fetch_data = curs.fetchone()
                        print("현재 정보 -> ", fetch_data)

                        select=int(input('수정할 정보를 선택해주세요 1)이름 2)핸드폰번호 3)주소->'))
                        while(True):
                            if select==1: #이름 수정
                                new_name=input('변경할 이름을 입력하세요 ->')
                                updateSQL="update customer set customer_name=%s where customer_id=%s"
                                curs.execute(updateSQL, (new_name, custid))
                                conn.commit()
                                break
                            elif select==2: #번호 수정
                                new_phone=input('변경할 번호를 입력하세요 ->')
                                updateSQL="update customer set phone_number=%s where customer_id=%s"
                                curs.execute(updateSQL, (new_phone, custid))
                                conn.commit()
                                break
                            elif select==3: #주소 수정 
                                new_address=input('변경할 주소를 입력하세요 ->')
                                updateSQL="update customer set address=%s where customer_id=%s"
                                curs.execute(updateSQL, (new_address, custid))
                                conn.commit()
                                break
                            else: print("번호를 잘못 입력하였습니다.")
                    elif customer==4:
                        custid=input('삭제할 고객아이디를 입력해주세요 ex)C0001 ->').upper()
                        selectSQL="select * from customer where customer_id=%s"
                        curs.execute(selectSQL, (custid))
                        fetch_data = curs.fetchone()
                        print("현재 정보 -> ", fetch_data)

                        ask=input("정말 삭제하시겠습니까? (Y/N)->").lower()
                        if ask=='y':
                            deleteSQL="delete from customer where customer_id=%s"
                            curs.execute(deleteSQL, (custid))
                            conn.commit()
                        else: print()
                            
                    elif customer==5:break
                    else : print("번호를 잘못 입력하였습니다.") 

        elif cmd == 2:
                while True:
                    sidemenu='자 동 차 메 뉴'
                    print(sidemenu.center(40, "-"))
                    car = int(input('1) 추가 2) 조회 3) 수정 4) 삭제 5) 메인메뉴로->'))

                    if car==1: #추가
                        #자동차 아이디 생성
                        selectSQL="select car_id from car_menu limit 1"
                        curs.execute(selectSQL)
                        fetch_data = curs.fetchone()
                        
                        if(fetch_data is None):
                            carid='CAR0001'
                        else:
                            carid_f='CAR'
                            selectSQL="select lpad(max(convert(substr(car_id,4,7),signed)+1),4,0) from car_menu"
                            curs.execute(selectSQL)
                            fetch_data = curs.fetchone()
                            carid_b=fetch_data[0]
                            carid=carid_f+carid_b
                        
                        carinfo=input('모델명,색,상태(NEW|OLD),일련번호,제작년도,가격 *한글 또는 영어로 입력(,로 구분)*->').split(',')
                        insertSQL = "insert into car_menu values(%s,%s,%s,%s,%s,%s,%s)"
                        curs.execute(insertSQL, (carid,carinfo[0],carinfo[1], carinfo[2],carinfo[3],carinfo[4],carinfo[5]))
                        conn.commit()

                    #살 수 있는 차가 없어서 조회 반복됨    (예외처리)
                    elif car==2: #조회
                        selectSQL="SELECT * FROM car_menu WHERE car_id NOT IN(SELECT car_menu_car_id FROM order_details)"
                        rows = curs.execute(selectSQL)
                        fetch_data = curs.fetchone()
                        if(fetch_data is None):
                            print('자동차 제고가 없습니다')
                        else:
                            selectSQL="SELECT * FROM car_menu WHERE car_id NOT IN(SELECT car_menu_car_id FROM order_details)"
                            rows = curs.execute(selectSQL)
                            for row in curs.fetchall():
                                print(row)

                    elif car==3: #수정
                        carid=input('자동차 아이디를 입력해주세요 ex)CAR0001 ->').upper()
                        selectSQL="select * from car_menu where car_id=%s"
                        curs.execute(selectSQL, (carid))
                        fetch_data = curs.fetchone()
                        print("현재 정보 -> ", fetch_data)

                        select=int(input('수정할 정보를 선택해주세요 1)모델명 2)색상 3)상태(NEW|OLD) 4)가격 ->'))
                        while(True):
                            if select==1: #모델명
                                new_car_model=input('변경할 모델명을 입력하세요 ->')
                                updateSQL="update car_menu set car_model=%s where car_id=%s"
                                curs.execute(updateSQL, (new_car_model, carid))
                                conn.commit()
                                break
                            elif select==2: #색
                                new_color=input('변경할 색상을 입력하세요 ->').upper()
                                updateSQL="update car_menu set car_color=%s where car_id=%s"
                                curs.execute(updateSQL, (new_color, carid))
                                conn.commit()
                                break
                            elif select==3: #상태 
                                new_state=input('변경할 상태를 입력하세요(NEW|OLD) ->').upper()
                                updateSQL="update car_menu set new_old_state=%s where car_id=%s"
                                curs.execute(updateSQL, (new_state, carid))
                                conn.commit()
                                break
                            elif select==4: #가격
                                new_price=input('변경할 가격을 입력하세요 ->')
                                updateSQL="update car_menu set car_price=%s where car_id=%s"
                                curs.execute(updateSQL, (new_price, carid))
                                conn.commit()
                                break
                            else: print("번호를 잘못 입력하였습니다.")
                    elif car==4: #삭제
                        carid=input('삭제할 자동차 아이디를 입력해주세요 ex)CAR0001 ->').upper()
                        selectSQL="select * from car_menu where car_id=%s"
                        curs.execute(selectSQL, (carid))
                        fetch_data = curs.fetchone()
                        print("현재 정보 -> ", fetch_data)

                        ask=input("정말 삭제하시겠습니까? (Y/N)->").lower()
                        if ask=='y':
                            deleteSQL="delete from car_menu where car_id=%s"
                            curs.execute(deleteSQL, (carid))
                            conn.commit()
                        else: print()
                    elif car==5:break
                    else : print("번호를 잘못 입력하였습니다.")

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
                    #1
                    #구매할 수 있는 자동차 조회
                    selectSQL="SELECT * FROM car_menu WHERE car_id NOT IN(SELECT car_menu_car_id FROM order_details)"
                    curs.execute(selectSQL)
                    fetch_data = curs.fetchone()
                    if(fetch_data is None):
                        print('구입할 수 있는 자동차가 없습니다.')
                        break
                    else:
                        selectSQL="SELECT * FROM car_menu WHERE car_id NOT IN(SELECT car_menu_car_id FROM order_details)"
                        rows = curs.execute(selectSQL)
                        for row in curs.fetchall():
                            print(row)
                    car_select=input('구매할 자동차를 선택해주세요. ex)CAR0001 ->').upper()
                    
                    #2
                    salesid=input('직원번호를 입력해주세요 ex)S0001 ->').upper()
                    selectSQL="select * from salesperson where salesperson_id=%s"
                    curs.execute(selectSQL, (salesid))
                    fetch_data = curs.fetchone()
                    print("직원 정보 -> ", fetch_data)
                    #3
                    custid=input('고객아이디를 입력해주세요 ex)C0001 ->').upper()
                    selectSQL="select * from customer where customer_id=%s"
                    curs.execute(selectSQL, (custid))
                    fetch_data = curs.fetchone()
                    print("고객 정보 -> ", fetch_data)
                    #4 처음주문 예외처리

                    selectSQL="select order_id from order_details limit 1"
                    curs.execute(selectSQL)
                    fetch_data = curs.fetchone()
                    
                    if(fetch_data is None):
                        orderid='O0001'
                    else:
                        orderid_f='O'
                        selectSQL="select lpad(max(convert(substr(order_id,2,5),signed)+1),4,0) from order_details"
                        curs.execute(selectSQL)
                        fetch_data = curs.fetchone()
                        orderid_b=fetch_data[0]
                        orderid=orderid_f+orderid_b

                    #가격조회
                    selectSQL="select car_price from car_menu where car_id=%s"
                    curs.execute(selectSQL, (car_select))
                    fetch_data = curs.fetchone()

                    #주문내용 저장
                    insertSQL="insert into order_details values(%s,%s,%s,%s,%s)"
                    curs.execute(insertSQL, (orderid, custid, '', car_select, fetch_data[0]))
                    conn.commit()

                    #5 결제생략-> 송장을 보여줘 (송장 테이블 저장)
                    #송장 아이디 생성
                    invoiceid_f='I'
                    selectSQL="select lpad(max(convert(substr(invoice_id,2,4),signed)+1),4,0) from sales_invoice"
                    curs.execute(selectSQL)
                    fetch_data = curs.fetchone()
                    invoiceid_b=fetch_data[0]
                    invoiceid=invoiceid_f+invoiceid_b
                    #저장
                    insertSQL="insert into sales_invoice values(%s,%s,%s,%s)"
                    curs.execute(insertSQL, (invoiceid, custid, salesid, orderid))
                    conn.commit()

                    print("(+) 구매가 완료되었습니다.")
                    #송장을 보여줌
                    #고객 id, 자동차 정보, 판매직원, 가격, 
                    selectSQL="SELECT ct.customer_name, cm.car_model, cm.car_color, cm.new_old_state, cm.serial_number, cm.car_year, cm.car_price, sp.salesperson_name FROM customer ct, car_menu cm, sales_invoice si, order_details od, salesperson sp WHERE si.customer_customer_id=ct.customer_id AND si.order_details_order_id=od.order_id AND od.car_menu_car_id=cm.car_id AND sp.salesperson_id=si.salesperson_salesperson_id AND si.invoice_id=%s"
                    curs.execute(selectSQL, (invoiceid))
                    print("(+) 송장이 발급되었습니다. 송장번호 : ",invoiceid)
                    for row in curs.fetchall():
                        print(row)
                    break
        
        elif cmd == 4:
                while True:
                    sidemenu='서 비 스 메 뉴'
                    print(sidemenu.center(40, "-"))
                    service = int(input('1) 서비스 신청 2) 서비스 기록 조회 3) 메인으로 ->'))
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
                    if(service==1):
                        custid=input('고객 아이디를 입력해주세요 ex)C0001->').upper()

                        selectSQL="select customer_id from customer where customer_id=%s"
                        curs.execute(selectSQL, (custid))
                        fetch_data = curs.fetchone()
                        if(fetch_data is None):
                            print("가입 후에 사용 가능합니다.")
                            break
                        else:
                            selectSQL="select * from service_menu"
                            rows = curs.execute(selectSQL)
                            for row in curs.fetchall():
                                print(row)
                            service_answer=input("서비스를 받으시겠습니까? (Y/N)->").lower()
                            if(service_answer=='y'):
                                service_select=input("서비스를 선택해주세요 ex)SV0001->").upper()

                                selectSQL="select need_product from service_menu where service_id=%s"
                                curs.execute(selectSQL, (service_select))
                                fetch_data = curs.fetchone()
                                
                                if(fetch_data[0]=='Y'):
                                    # tire / handle
                                    selectSQL="SELECT DISTINCT product_name FROM product WHERE service_menu_service_id=%s"
                                    rows=curs.execute(selectSQL, (service_select))
                                    for row in curs.fetchall():
                                        print(row[0])
                                    # 
                                
                                    select_product=input("부품 종류를 선택하세요 ex)Tire ->").upper()
                                    
                                    #파츠 보여주는거
                                    select_product='%'+select_product
                                    selectSQL="select * from product_menu where parts_name like %s"
                                    rows=curs.execute(selectSQL, (select_product))
                                    for row in curs.fetchall():
                                        print(row)

                                    select_parts=input("부품을 선택하세요 ex)PA0001->").upper()
                                    select_product=select_product.replace('%','')

                                else: #N 파츠없을때
                                    select_parts=''
                                    select_product=''

                                #사용자  요일 함수
                                day=input("서비스 받을 날짜를 입력해주세요 ex)2020.02.20 ->")
                                day_list=[]
                                day_list=day.split('.')
                                service_day=datetime.datetime(int(day_list[0]),int(day_list[1]),int(day_list[2])).weekday()
                                service_day_weekday=get_weekday(int(service_day)) #Mon~Sun이 반환됨
                                print('서비스 날짜',day,'는 ',service_day_weekday,'입니다.')

                                #요일 비교해서 가능한 메카닉만 출력해줌
                                selectSQL="select * from mechanic"
                                rows=curs.execute(selectSQL)
                                #row[5] 가 'mon thu 
                                
                                for row in curs.fetchall(): #한줄씩
                                    weekday_list=[]
                                    weekday_list=row[5].split(' ')
                                    for i in weekday_list:
                                        if(service_day_weekday==i):
                                            print(row)
                                            break
                                
                                mecha_select_list=[]
                                mecha_select=input("메카닉을 선택해주세요 (중복선택 가능) ex)M0001,M0002->").upper()
                                
                                if(',' in mecha_select):
                                    mecha_select_list=mecha_select.split(',')
                                else:
                                    mecha_select_list.append(mecha_select)
                                
                                #서비스 아이디 생성
                                selectSQL="select service_record_id from service_records limit 1"
                                curs.execute(selectSQL)
                                fetch_data = curs.fetchone()
                                
                                if(fetch_data is None):
                                    service_record_id='SR0001'
                                else:
                                    service_record_id_f='SR'
                                    selectSQL="select lpad(max(convert(substr(service_record_id,3,6),signed)+1),4,0) from service_records"
                                    curs.execute(selectSQL)
                                    fetch_data = curs.fetchone()
                                    service_record_id_b=fetch_data[0]
                                    service_record_id=service_record_id_f+service_record_id_b

                                # 서비스 티켓 확인
                                selectSQL="select service_ticket_id from service_records where customer_customer_id=%s"
                                curs.execute(selectSQL, (custid))
                                fetch_data = curs.fetchone()

                                if(fetch_data is None):
                                # 서비스 티켓 생성
                                    while(True):
                                        service_ticket=''
                                        for i in range(0, 10):
                                            service_ticket+=str(random.randint(1,9))
                                        selectSQL="select service_ticket_id from service_records where service_ticket_id=%s"
                                        curs.execute(selectSQL, (service_ticket))
                                        fetch_data = curs.fetchone()

                                        if(fetch_data is None):
                                            break
                                        else:
                                            continue
                                else:
                                    service_ticket=fetch_data[0]
                                    
                                

                                #서비스 레코드 테이블 데이터 저장
                                if(select_product is None):
                                    insertSQL="insert into service_records values(%s, %s, Null, %s, %s, %s)"
                                    curs.execute(insertSQL, (service_record_id, service_select, service_ticket, day, custid))
                                else:
                                    insertSQL="insert into service_records values(%s, %s, (select product_id from product where parts_id=%s), %s, %s, %s)"
                                    curs.execute(insertSQL, (service_record_id, service_select, select_parts,service_ticket, day, custid))
                                conn.commit()

                                #management 테이블
                                for i in mecha_select_list:
                                    insertSQL="insert into management values(%s, %s)"
                                    curs.execute(insertSQL, (i, service_record_id))
                                    conn.commit()

                                print("서비스 신청이 완료되었습니다.")
                                #서비스 신청 메카닉이름, 날짜, 서비스 이름, 고객 이름
                                print("서비스 신청 내역입니다.\n")
                                resultstr='서비스 신청 내역'
                                print(resultstr.center(50, "-"))
                                #서비스 신청 결과 출력
                                print("- 서비스 아이디 : ", service_record_id)
                                selectSQL="SELECT mc.mechanic_name from management ma, mechanic mc where ma.mechanic_mechanic_id=mc.mechanic_id AND service_record_id=%s"
                                curs.execute(selectSQL, (service_record_id))
                                print("- 서비스 할 기술자 : ",end='')
                                for row in curs.fetchall():
                                        print(row[0],end=' ')                                
                                selectSQL="select appointment from service_records where service_record_id=%s"
                                curs.execute(selectSQL, (service_record_id))
                                fetch_data = curs.fetchone()
                                print("- 서비스 날짜 : ",end='')
                                print(fetch_data[0])

                                selectSQL="SELECT sm.service_name FROM service_menu sm, service_records sr WHERE sm.service_id=sr.service_id AND sr.service_record_id=%s"
                                curs.execute(selectSQL, (service_record_id))
                                fetch_data = curs.fetchone()
                                print("- 서비스 이름 : ",end='')
                                print(fetch_data[0])

                                selectSQL="SELECT service_ticket_id FROM service_records WHERE service_record_id=%s"
                                curs.execute(selectSQL, (service_record_id))
                                fetch_data = curs.fetchone()
                                print("- 보유중이신 서비스 티켓 번호 : ",end='')
                                print(fetch_data[0])

                                selectSQL="SELECT c.customer_name FROM customer c, service_records sr WHERE c.customer_id=sr.customer_customer_id AND sr.service_record_id=%s"
                                curs.execute(selectSQL, (service_record_id))
                                fetch_data = curs.fetchone()
                                print("- 고객 이름 : ",end='')
                                print(fetch_data[0])
                                resultstr=''
                                print(resultstr.center(60, "-"))
                                print('\n')
                                
                    elif (service==2): #서비스 기록 조회
                    # 고객 id로 조회
                    # 서비스_레코즈 테이블에서
                    # 
                        custid=input('고객 아이디를 입력해주세요 ex)C0001->').upper()

                        selectSQL="SELECT * FROM service_records sr LEFT JOIN (SELECT product_id, service_menu_service_id, product_name, parts_name, parts_price from product p1, product_menu pm WHERE p1.parts_id=pm.parts_id) AS p ON sr.product_id=p.product_id LEFT JOIN (select * from management m1 left join mechanic mc on m1.mechanic_mechanic_id=mc.mechanic_id) AS m ON sr.service_record_id=m.service_record_id LEFT JOIN service_menu sm ON sr.service_id=sm.service_id WHERE sr.customer_customer_id=%s"
                        curs.execute(selectSQL, (custid))
                        for row in curs.fetchall():
                            print(row)

                    else: 
                        print("메인으로 돌아갑니다.")
                        break
            
        elif cmd == 5:
                conn.close()
                break
        else:
            print('잘못 선택하셨습니다.')