from urllib.request import urlopen
from bs4 import BeautifulSoup
import dart_api_information


def get_rcrpt_no(corp_name, corp_code, bgn_de, end_de, page_no, page_count):
    # temp
    corp_name = "삼천당제약"
    corp_code = "00128546"
    bgn_de = "20200217"
    end_de = "20200817"
    page_no = "1"
    page_count = "10"
    # get url and api_key from dart_api_information
    api_key = dart_api_information.DartKey.get_key()
    url = dart_api_information.DartUrl.get_rcept_no_url()
    url = (url +
           "?crtfc_key=" + api_key +
           "&corp_code=" + corp_code +
           "&bgn_de=" + bgn_de +
           "&end_de=" + end_de +
           "&page_no=" + page_no +
           "&page_count=" + page_count)

    openurl = urlopen(url)
    html = openurl.read().decode()
    soup = BeautifulSoup(html, 'html.parser')
    res = soup.find_all('list')

    print("기간 " + bgn_de + " ~ " + end_de + "사이의 회사" + corp_name +" 공시검색 결과입니다.")

    for i, n in enumerate(res, 1):
        corp_name = n.find('corp_name')
        report_nm = n.find('report_nm')
        rcept_no = n.find('rcept_no')
        rcept_dt = n.find('rcept_dt')
        print(str(i) + ". " + corp_name +
              "보고서 종류: " + report_nm +
              "보고서 날짜: " + rcept_dt)
        print(n)

