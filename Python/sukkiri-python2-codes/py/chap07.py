#!/usr/bin/env python
# coding: utf-8

# In[ ]:


text = input('何を記録しますか? >>')
file = open('diary.txt', 'a')
file.write(text + '\n')
file.close()


# In[ ]:


text = input('今日は何をした? >>')
with open('diary.txt', 'a') as file:
    file.write(text + '\n')


# In[ ]:


import math

print(f'円周率は{math.pi}です')
print(f'小数点以下を切り捨てれば{math.floor(math.pi)}です')
print(f'小数点以下を切り上げれば{math.ceil(math.pi)}です')


# In[ ]:


import math as m

print(f'円周率は{m.pi}です')
print(f'小数点以下を切り捨てれば{m.floor(m.pi)}です')
print(f'小数点以下を切り上げれば{m.ceil(m.pi)}です')


# In[ ]:


from math import pi
from math import floor

print(f'円周率は{pi}')
print(f'小数点以下を切り捨てれば{floor(pi)}です')


# In[ ]:


from math import log

def log(msg):
    print(f'{msg}を記録します')
log(10)


# In[ ]:


from math import pi as ensyuritsu
from math import floor as kirisute

print(f'円周率は{ensyuritsu}')
print(f'小数点以下を切り捨てれば{kirisute(ensyuritsu)}です')


# In[ ]:


from math import *

print(f'円周率は{pi}です')
print(f'小数点以下を切り捨てれば{floor(pi)}です')
print(f'小数点以下を切り上げれば{ceil(pi)}です')


# In[ ]:


import http.client

conn = http.client.HTTPConnection('www.python.org')
# ：


# In[ ]:


from http import client

conn = client.HTTPConnection('www.python.org')
# ：


# In[ ]:


from http.client import HTTPConnection

conn = HTTPConnection('www.python.org')
# ：


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

weight = [68.4, 68.0, 69.5, 68.4, 68.6, 70.2, 71.4, 70.8, 68.5, 68.6, 68.3, 68.4]
plt.plot(weight)


# In[ ]:


import requests

response = requests.get('https://www.python.org/downloads/')
text = response.text
print(text)


# In[ ]:


import http.client

conn = http.client.HTTPSConnection('www.python.org')
conn.request('GET', '/downloads/')
response = conn.getresponse()
text = response.read().decode('UTF-8')
print(text)
conn.close()

