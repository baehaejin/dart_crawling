import get_corp_code
import get_recpt_no
import get_document
import time


def main():

    while True:
        corp_name = input("주식회사 이름을 입력하신 후 enter를 눌러주세요. (모를경우 enter): ")
        stock_code = input("주식회사  종목번호를 입력하신 후 enter를 눌러주세요. (모를경우 enter): ")
        corp_code, corp_name = get_corp_code.get_corp_code(corp_name, stock_code)
        if corp_code == -1:
            print("잘못 입력하셨습니다. 다시 입력 해주세요.")
            print()
            continue
        print()
        print(corp_name + "에 관한 공시검색을 시작하겠습니다.")
        today = time.strftime('%Y%m%d', time.localtime(time.time()))
        print()
        print("오늘의 날짜 : " + today)
        print("6개월전 : " + today-600)
        end_de = today
        bgn_de = today-600
        if input("현재 날짜를 원하지 않으시면 n키를 누른 후 enter를 입력해 주세요.(enter를 누르면 위 날짜로 공시검색)") == "n":
            bgn_de = input("시작일을 입력해 주세요 20XXXXXX : ")
            end_de = input("마지막 일을을 입력해 주세요 20XXXXXX : ")

        rcept_no_list = get_recpt_no.get_rcrpt_no(corp_name, corp_code, bgn_de, end_de, 1, 100)

        for rcept_no in rcept_no_list:
            document = get_document(rcept_no)


if __name__ == '__main__':
    main()