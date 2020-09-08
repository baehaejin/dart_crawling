from urllib.request import urlopen
from zipfile import ZipFile, BadZipFile
from io import BytesIO
from bs4 import BeautifulSoup
import dart_api_information


def get_document(rcept_no, report_nm):
    print()
    print(report_nm + "검색중입니다. 잠시만 기다려 주세요")

    document = []
    api_key = dart_api_information.DartKey.get_key()
    api_url = dart_api_information.DartUrl.get_document_url()
    url = api_url + "?crtfc_key=" + api_key + "&rcept_no=" + rcept_no

    open_url = urlopen(url)
    try:
        with ZipFile(BytesIO(open_url.read())) as zf:
            file_list = zf.namelist()
            # print(file_list)
            # print(type(file_list[2]))
            # print(rcept_no + ".xml")
            for index, file in enumerate(file_list, 0):
                if (rcept_no + ".xml") == file.replace("/", ""):
                    file_name = file_list[index]
                    # zipfile decode because it is bytes code
                    zf_open = zf.open(file_name).read()
                    break
                # while len(file_list) > 0:
                #     file_name = file_list.pop()
                #     # zipfile decode because it is bytes code
                #     zf_open = zf.open(file_name).read()
                #     break
    except (IOError, BadZipFile):
        return "BadZipFile"
    # print(zf_open)
    soup = BeautifulSoup(zf_open, 'html.parser')
    res = soup.find_all("section-2")

    for n in res:
        # print(n)
        find_title = n.find('title')
        if "4. 재무제표" in find_title.get_text():
            document.append(n)
    return document

