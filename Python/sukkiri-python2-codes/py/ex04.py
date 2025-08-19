#!/usr/bin/env python
# coding: utf-8

# In[ ]:


count = 0
while count < 5:
    count += 1


# In[ ]:


count = 1
while count <= 5:
    count += 1


# In[ ]:


data = [88, 21, 65, 160, 57]
count = 0
while count < len(data):
    count += 1


# In[ ]:


for num in range(5):
    print(num)


# In[ ]:


for item in [88, 21, 65, 160, 57]:
    print(item)


# In[ ]:


data = [88, 21, 65, 160, 57]
for item in data:
    print(item)


# In[ ]:


for item in [88, 21, 65, 160, 57]:
    if item >= 100:
        break
    print(item)


# In[ ]:


for item in [88, 21, 65, 160, 57]:
    if item >= 100:
        continue
    print(item)


# In[ ]:


count = 1
ans = True
print('カレーを召し上がれ')
while ans == True:
    print(f'{count}皿のカレーを食べました')
    key = input('おかわりはいかがですか?(y/n)>>')
    if key == 'y':
        count += 1
    else:
        ans = False
print('ごちそうさまでした')


# In[ ]:


for n in range(10):
    print(f'{10 - n}、', end='')
print('Lift off!')


# In[ ]:


for i in range(9):
    for j in range(9):
        print(f'{i+1}×{j+1}={(i+1)*(j+1)}')


# In[ ]:


for i in range(9):
    if (i+1) % 2 == 0:
        continue
    for j in range(9):
        print(f'{i+1}×{j+1}={(i+1)*(j+1)}')


# In[ ]:


for i in range(9):
    if (i+1) % 2 == 0:
        continue
    for j in range(9):
        if (i+1)*(j+1) > 50:
            break
        print(f'{i+1}×{j+1}={(i+1)*(j+1)}')


# In[ ]:


temp = list()
for n in range(10):
    data = float(input(f'{n+1}個目のデータを入力 >>'))
    temp.append(data)


# In[ ]:


for count in range(len(temp)):
    print(f'{count+8}時 {temp[count]}度')


# In[ ]:


temp_new = list()
for count in range(len(temp)):
    if count == 5:
        temp_new.append('N/A')
    else:
        temp_new.append(temp[count])
print(temp)
print(temp_new)


# In[ ]:


total = 0
for data in temp_new:
    if isinstance(data, float):
        total = total + data
print(total / (len(temp_new) - 1))


# In[ ]:


numbers = [1, 1]
data = sum(numbers)
count = 2
while data <= 1000:
    numbers.append(data)
    data = data + numbers[count-1]
    count += 1
print(numbers)


# In[ ]:


ratios = list()
for count in range(len(numbers)):
    if count == len(numbers) - 1:
        break
    ratios.append(numbers[count+1] / numbers[count])
print(ratios)


# In[ ]:


for count in range(len(ratios)):
    ratios[count] = int(ratios[count] * 1000) / 1000
print(ratios)

