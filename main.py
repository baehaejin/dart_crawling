import get_corp_code
import get_recpt_no
import get_document
import export_excel
import time


def main():

    while True:
        print("====================================================================")
        corp_name = input("주식회사 이름을 입력하신 후 enter를 눌러주세요. (모를경우 enter): ")
        stock_code = input("주식회사  종목번호를 입력하신 후 enter를 눌러주세요. (모를경우 enter): ")
        corp_code, corp_name = get_corp_code.get_corp_code(corp_name, stock_code)
        if corp_code == -1:
            print("잘못 입력하셨습니다. 다시 입력 해주세요.")
            print()
            continue
        print()
        print(corp_name + "에 관한 공시검색을 시작하겠습니다. 잠시만 기다려 주세요")
        today = time.strftime('%Y%m%d', time.localtime(time.time()))
        end_de = today
        bgn_de = str(int(today) - 600)
        print()

        print("오늘의 날짜 : " + bgn_de)
        print("6개월전 : " + end_de)

        if input("현재 날짜를 원하지 않으시면 n키를 누른 후 enter를 입력해 주세요.(enter를 누르면 위 날짜로 공시검색)") == "n":
            bgn_de = input("시작일을 입력해 주세요 20XXXXXX : ")
            end_de = input("마지막 일을을 입력해 주세요 20XXXXXX : ")
        print()
        print("검색중입니다 잠시만 기다려 주세요")
        print()
        rcept_no_list, report_nm_list = get_recpt_no.get_rcrpt_no(corp_name, corp_code, bgn_de, end_de, '1', '100')

        for rcept_no, report_nm in zip(rcept_no_list, report_nm_list):
            document = get_document.get_document(rcept_no, report_nm)
            export_excel.export_excel(corp_name, document, report_nm)
        print()
        print("====================================================================")
        print()
        end_or_not = input("공시검색을 더 원하시면 y키를 누르신다음 enter를 입력해 주세요 : ")
        print()
        if end_or_not == 'y' or end_or_not == 'Y':
            continue
        break


if __name__ == '__main__':
    main()
