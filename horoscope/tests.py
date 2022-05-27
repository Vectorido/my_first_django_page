from django.test import TestCase
from datetime import date

dict_date = {"aries": [date(2000, 3, 21), date(2000, 4, 20)],
             "taurus": [date(2000, 4, 21), date(2000, 5, 21)],
             "gemini": [date(2000, 5, 22), date(2000, 6, 21)],
             "cancer": [date(2000, 6, 22), date(2000, 7, 22)],
             "leo": [date(2000, 7, 23), date(2000, 8, 21)],
             "virgo": [date(2000, 8, 22), date(2000, 9, 23)],
             "libra": [date(2000, 9, 24), date(2000, 10, 23)],
             "scorpio": [date(2000, 10, 24), date(2000, 11, 22)],
             "sagittarius": [date(2000, 11, 23), date(2000, 12, 22)],
             "capricorn": [date(2000, 12, 23), date(2000, 1, 20)],
             "aquarius": [date(2000, 1, 21), date(2000, 2, 19)],
             "pisces": [date(2000, 2, 20), date(2000, 3, 20)]
             }


# Create your tests here.
def get_info_by_date(month, day):
    req_date = date(2000, month, day)
    try:
        for k, v in dict_date.items():
            if v[0] < req_date < v[1]:
                return k
    except ValueError:
        return False

print(get_info_by_date(1, 15))
