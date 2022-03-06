from django.test import TestCase

# Create your tests here.

import decimal
from datetime import datetime, date

a = datetime(2019, 1, 1, 1, 1, 1).hour
b = date(2019, 1, 1).strftime('%Y-%m-%d %H:%M:%S')


import re

# p = r'(?![a-z]+$)[0-8]'
#
# print(re.search(p, 'c1'))

str = '<div>hello world</div>'
print(re.search('(?=he).*',str))

s = 'finished going done doing'
p = re.compile(r'\b\w+(?=ing\b)')
print ([x for x in re.findall(p,s)])

s = 'done run going'
p = re.compile(r'\b\w{2,3}(?!ing\b)')
print(re.findall(p,s))

a = {'name' :1}