from datetime import datetime

class StringUtil:
    
    @staticmethod
    def tagsStr_to_list(tagsStr):
        trimStr = tagsStr.replace ("\" \"", ",")
        trimStr = trimStr.replace("\" ", ",")
        trimStr = trimStr.replace("\"", "")
        return trimStr.split(",")

class DateUtil:

    @staticmethod
    def dateStr_to_datetime(dateStr):
        return datetime.strptime(dateStr, '%Y/%m/%d %H:%M:%S %z')

    @staticmethod
    def dateJson_to_datetime(dateStr):
        return datetime.strptime(dateStr, '%Y-%m-%dT%H:%M:%S%z')

