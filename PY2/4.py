
string = input('string: ')
str_sn_case = string[0].lower()
for c in string[1:]:
    if c.isupper():
        str_sn_case = str_sn_case + '_'
        str_sn_case = str_sn_case + c.lower()
    else:
        str_sn_case = str_sn_case + c

print(str_sn_case)