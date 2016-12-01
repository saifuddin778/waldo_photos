import arrow
from dateutil.parser import parse


class null_support:
    printable = "N/A"


class helpers(object):
    """some helper functions for parsing data types"""

    def __init__(self):
        pass

    @staticmethod
    def int_(val):
        return int(val)

    @staticmethod
    def float_(val):
        return float(val)

    @staticmethod
    def date_(val):
        try:
            return arrow.get(val).datetime.strftime("%Y-%m-%d")
        except:
            return parse(val).strftime("%Y-%m-%d")

    @staticmethod
    def str_(val):
        return val.strip('"').replace("\\", "")

    @staticmethod
    def null(val):
        return val

    @staticmethod
    def vnull(val):
        if val == 'None':
            return None
        else:
            return val
