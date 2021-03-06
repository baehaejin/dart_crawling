from urllib.request import urlopen
from bs4 import BeautifulSoup
import dart_api_information
import time


def get_rcrpt_no(corp_name, corp_code, bgn_de, end_de, page_no, page_count):
    today = time.strftime('%Y%m%d', time.localtime(time.time()))
    print("today is : " + today)

    report_nm_list = []
    rcept_no_list = []

    # get url and api_key from dart_api_information
    api_key = dart_api_information.DartKey.get_key()
    api_url = dart_api_information.DartUrl.get_rcept_no_url()


    url = (api_url +
           "?crtfc_key=" + api_key +
           "&corp_code=" + corp_code +
           "&bgn_de=" + bgn_de +
           "&end_de=" + end_de +
           "&page_no=" + page_no +
           "&page_count=" + page_count)

    open_url = urlopen(url)
    html = open_url.read().decode()
    soup = BeautifulSoup(html, 'html.parser')

    total_count = soup.find_all('result')
    total_count = total_count[0].find('total_count').get_text()
    page_count = total_count
    url = (api_url +
           "?crtfc_key=" + api_key +
           "&corp_code=" + corp_code +
           "&bgn_de=" + bgn_de +
           "&end_de=" + end_de +
           "&page_no=" + page_no +
           "&page_count=" + page_count)
    open_url = urlopen(url)
    html = open_url.read().decode()
    soup = BeautifulSoup(html, 'html.parser')
    res = soup.find_all('list')
    print("기간 " + bgn_de + " ~ " + end_de + "사이의 회사 " + corp_name +" 공시검색 결과입니다.")
    print()
    i = 1
    for n in res:
        corp_name = n.find('corp_name').get_text()
        report_nm = n.find('report_nm').get_text()
        rcept_no = n.find('rcept_no').get_text()
        rcept_dt = n.find('rcept_dt').get_text()
        if "반기보고서" in report_nm or "분기보고서" in report_nm or "사업보고서" in report_nm:
            print()
            print(str(i) + ". " + corp_name + "    보고서 종류: " + report_nm + "    보고서 날짜: " + rcept_dt)
            i += 1
            rcept_no_list.append(rcept_no)
            report_nm_list.append(report_nm)
            print(report_nm + " 가 추가되었습니다")
    return rcept_no_list, report_nm_list



