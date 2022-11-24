"""
Verify using a regular expression whether a string is a valid CNP.
"""
import re


def get_control_digit(text):
    constant = "279146358279"
    result = 0
    for i, j in zip(constant, text):
        result += int(i) * int(j)
    result = result % 11
    if result == 10:
        result = 1
    return str(result)


def get_days_from_months(year, month):
    days_per_month = [
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|1\d|2[0-8])",
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|[1-2]\d|30)",
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|[1-2]\d|30)",
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|[1-2]\d|30)",
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|[1-2]\d|30)",
        r"(0[1-9]|[1-2]\d|3[0-1])",
    ]
    if int(year) % 4 == 0:
        days_per_month[1] = r"(0[1-9]|1\d|2[0-9])"
    return days_per_month[int(month) - 1]


def check_cnp(text):
    first_digit = r"[1-8]"
    year = r"\d{2}"
    month = r"(0[1-9]|1[0-2])"
    day = get_days_from_months(text[1:3], text[3:5])
    county = r"(0[1-9]|1[0-9]|2[0-9]|3[0-9]|4[0-6]|5[1-2])"
    random_digits = r"(\d\d\d)"
    control_digit = get_control_digit(text[:-1])

    cnp_check_string = r"^" + first_digit + year + month + day + county + random_digits + control_digit + r"$"
    print(cnp_check_string)

    return bool(re.match(cnp_check_string, text))


if __name__ == '__main__':
    my_cnp = "1980424225161"
    fake_cnp = "1990229024525"
    print(check_cnp(my_cnp))
    print(check_cnp(fake_cnp))