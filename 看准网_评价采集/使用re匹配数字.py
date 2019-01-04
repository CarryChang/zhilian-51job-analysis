# -*- coding: utf-8 -*-
import re

string="A1.45，b5，6.45，8.82"
print (re.findall(r"\d+\.?\d*",string))

# ['1.45', '5', '6.45', '8.82']