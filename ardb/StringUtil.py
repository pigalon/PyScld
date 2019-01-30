class StringUtil:
    
    @staticmethod
    def tagsStr_to_list(tagsStr):
        trimStr = tagsStr.replace ("\" \"", ",")
        trimStr = trimStr.replace("\" ", ",")
        trimStr = trimStr.replace("\"", "")
        return trimStr.split(",")