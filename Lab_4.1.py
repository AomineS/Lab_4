# Дано текст. Замінити всі входження найбільшої цифри її словесним написанням
from re import sub

Text = input("Text = ")
B = max(filter(str.isdigit, Text))
B1 = " нуль ", " один ", " два ", " три ", " чотири ", " п'ять ", " шість ", " сім ", " вісім ", " дев'ять ",
C = sub(B, lambda mo: B1[int(mo.group())], Text)
print(C)
