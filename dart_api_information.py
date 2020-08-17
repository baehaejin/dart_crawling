class DartKey:
    """
    dart key class
    """
    @staticmethod
    def get_key():
        __privateApi_key = 'input your api key'
        return __privateApi_key


class DartUrl:
    """
    dart api urls
    """
    @staticmethod
    def get_corp_code_url():
        # this url can corp_code by stock_code or corp_name
        __privateGetCorpCodeUrl = "https://opendart.fss.or.kr/api/corpCode.xml"
        """
        you need to add
        : ?crtfc_key=your own api key
        :return: this return url that you can get corp_code
        """
        return __privateGetCorpCodeUrl

    @staticmethod
    def get_rcept_no_url():
        # this url get rcept_no by input corp_code and bgn_de and end_de
        __privateGetReceptionNoUrl = "https://opendart.fss.or.kr/api/list.xml"
        """
        you need to add
        : ?crtfc_key=your own api key
        : &corp_code=corporation code
        : &bgn_de=beginning day to search public notice
        : &end_de=ending day to search public notice
        : &page_no=
        : &page_count=
        :return: this return url that you can get rcept_no
        """
        return __privateGetReceptionNoUrl
