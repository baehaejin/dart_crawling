class DartKey:
    """
    dart key class
    """
    __privateApi_key = 'input your api key'

    def get_key(self):
        return self.__privateApi_key


class DartUrl:
    """
    dart api urls
    """
    # this url can get corp_code by stock_code or corp_name
    __privateGetCorpCodeUrl = "https://opendart.fss.or.kr/api/corpCode.xml"

    def get_corp_code_url(self):
        return self.__privateGetCorpCodeUrl
