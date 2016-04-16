
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i = 0
        # �����հ׺������ַ�
        while i < len(str) and str[i].isspace():
            i += 1
        if i == len(str) or (str[i] != "+" and str[i] != "-" and not str[i].isdigit()):
            return 0
        # �õ� "+" or "-"
        sign = 1
        if str[i] == "-":
            sign = -1
        # �õ����ֲ���
        if str[i] == "+" or str[i] == "-":
            i += 1
        start = i
        while i < len(str) and str[i].isdigit():
            i += 1
        numStr = str[start:i]
        # ��ȡ���
        if len(numStr) == 0:
            return 0
        #�Ƿ����
        if sign == 1:
            INTMAX = 2 ** 31 - 1
            INTMAXstr = "2147483647"
            if len(numStr) > len(INTMAXstr):
                return INTMAX
            elif len(numStr) == len(INTMAXstr):
                for i in range(len(numStr)):
                    value = ord(numStr[i]) - ord(INTMAXstr[i])
                    if value > 0:
                        return INTMAX
                    elif value < 0:
                        break
        elif sign == -1:
            INTMIN = -1 * (2 ** 31)
            INTMINstr = "2147483648"
            if len(numStr) > len(INTMINstr):
                return INTMIN
            elif len(numStr) == len(INTMINstr):
                for i in range(len(numStr)):
                    value =ord(numStr[i]) - ord(INTMINstr[i])
                    if value > 0:
                        return INTMIN
                    elif value < 0:
                        break
        # ���û�������
        res = 0
        for i in range(len(numStr)):
            res = res * 10 + (ord(numStr[i]) - ord("0"))
        return sign*res






