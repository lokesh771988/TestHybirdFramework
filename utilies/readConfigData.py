import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\configData.ini")


class ReadConfig:

    @staticmethod
    def getBaseUrl():
        url = config.get("commonData", "base_url")
        return url

    @staticmethod
    def getUserName():
        userName = config.get("commonData", "userName")
        return userName

    @staticmethod
    def getCommonData(rowKey, key_value):
        value = config.get(rowKey, key_value)
        return value

