import requests
from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO
from bs4 import BeautifulSoup
import dart_api_information


def get_corp_code(corp_name, stock_code):
    # get url and api_key from dart_api_information
    key_class = dart_api_information.DartKey()
    url_info = dart_api_information.DartUrl()
    api_key = key_class.get_key()
    url = url_info.get_corp_code_url()
    url = url + "?crtfc_key=" + api_key

    corp_code = ""
    corp_name_list = []

    # temp
    corp_name = "삼천당"
    stock_code = "000250"

    # The bytes of the received resp are accumulated in the buffer and the zip file is loaded.
    openurl = urlopen(url)
    html = requests.get(url)
    with ZipFile(BytesIO(openurl.read())) as zf:
        file_list = zf.namelist()
        while len(file_list) > 0:
            file_name = file_list.pop()
            # zipfile decode because it is bytes code
            corpCode = zf.open(file_name).read().decode()
            # print(corpCode)
            break

    soup = BeautifulSoup(corpCode, 'html.parser')
    res = soup.find_all('list')

    # get corp code by input stock_code and corp_name
    for n in res:
        is_stock_code = n.find('stock_code')
        is_corp_name = n.find('corp_name')
        if is_stock_code.get_text() == stock_code or corp_name in is_corp_name.get_text():
            # append list that can be contains stock_code or corp_name
            corp_name_list.append(n)
            if len(corp_name_list) == 1:
                corp_code = n.find('corp_code').get_text()

    # find one corp_code
    if len(corp_name_list) == 0:
        print("해당 기업의 정보가 존재하지 않습니다.")
        return -1
    elif len(corp_name_list) == 1:
        corp_name = corp_name_list[0].find('corp_name').get_text()
        print("선택하신 종목 : " + corp_name)
        corp_code = corp_name_list[0].find('corp_code').get_text()
        stock_code = corp_name_list[0].find('stock_code').get_text()
    elif len(corp_name_list) != 1:
        for i, name_list in enumerate(corp_name_list, 1):
            print_corp_name = name_list.find('corp_name').get_text()
            print(str(i) + ". : " + print_corp_name)

        # uer can select stock by input number
        select_num = input("해당 주식을 입력해주세요 = ")

        # selected stock
        for i, name_list in enumerate(corp_name_list, 1):
            if i == int(select_num):
                corp_name = name_list.find('corp_name').get_text()
                print("선택하신 종목 :" + str(i) + ". : " + corp_name)
                corp_code = name_list.find('corp_code').get_text()
                stock_code = name_list.find('stock_code').get_text()
                break

    return corp_code

