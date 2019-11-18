# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mlx-WDG8dnziLGm9NU4VV-Dw8QEvUB5y
"""

shoplist=['牛奶','蛋','咖啡豆','西瓜','鳳梨']
print('顯示shoplist[0]為',shoplist[0])

shoplist=['牛奶','蛋','咖啡豆','西瓜','鳳梨']
print('購物清單shoplist長度為',len(shoplist))

shoplist=['牛奶','蛋','咖啡豆','西瓜','鳳梨']
shoplist[1]='皮蛋'
print("執行shoplist[1]='皮蛋'後")
print(shoplist)

shoplist=['牛奶','蛋','咖啡豆','西瓜','鳳梨']
index=shoplist.index('咖啡豆')
print("執行index=shoplist.index('咖啡豆')後")
print('index=',index)

shoplist=['牛奶','蛋','咖啡豆','西瓜','鳳梨']
shoplist.append('麵包')
print("執行shoplist.append('麵包')後")
print(shoplist)

shoplist=['牛奶','蛋','咖啡豆','西瓜','鳳梨']
shoplist.insert(4,'蘋果')
print("執行shoplist.insert(4,'蘋果'後)")
print(shoplist)

shoplist=['牛奶','蛋','咖啡豆','西瓜','鳳梨']
shoplist.remove('蛋')
print("執行shoplist.remove('蛋')後)")
print(shoplist)

shoplist=['牛奶','蛋','咖啡豆','西瓜','鳳梨']
del shoplist[0]
print("執行del shoplist[0]後")
print(shoplist)

shoplist=['牛奶','蛋','咖啡豆','西瓜','鳳梨']
shoplist.pop(0)
print("執行shoplist.pop(0)後")
print(shoplist)
shoplist.pop()
print("執行shoplist.pop()後")
print(shoplist)
shoplist.pop(-1)
print("執行shoplist.pop(-1)後")
print(shoplist)

shoplist=['牛奶','蛋','咖啡豆','西瓜']
shoplist.sort()
print("執行shoplist.sort()後")
print(shoplist)

listm=[1,2.0,'python']
print("串列可以包含各種資料類別的元素")
print(listm)

shoplist=['牛奶','蛋','咖啡豆','西瓜']
for item in shoplist:
   print(item)

shoplist1=['牛奶','蛋','咖啡豆']
shoplist2=['西瓜','鳳梨'] 
shoplist_all=shoplist1+shoplist2
print(shoplist_all)

list1=list('python')
print(list1)
tuple2=('a','b',1,2)
list2=list(tuple2)
print(list2)

list3="2016/1/1".split('/')
print(list3)

a=list('abcdefghijk')
print('a[:]為',a[:])

a=list('abcdefghijk')
print('a[:5]為',a[:5])
print('a[5:]為',a[5:])
print('a[:-5]為',a[:-5])
print('a[-5:]為',a[-5:])

a=list('abcdefghijk')
print('a[0:4]為',a[0:4])
print('a[-5:-3]為',a[-5:-3])

a=list('abcdefghijk')
print('a[1:10:3]為',a[1:10:3])
print('a[-1:-4:-1]為',a[-1:-4:-1])

a=list('abcdefghijk')
print('a[::-1]為',a[::-1])

list1=[1,2,3,4]
list2=list1
print('list1=',list1)
print('list2=',list2)
list1[2]=19
print('list1=',list1)
print('list2=',list2)
list2[2]=18
print('list1=',list1)
print('list2=',list2)

list1=[1,2,3,4]
list3=list1[:]
list3[2]=19
print('list1=',list1)
print('list3=',list3)
list4=list1.copy()
list4[2]=19
print('list1=',list1)
print('list4=',list4)

dict1={}
print(dict1)
lang={'早安':'Good Morning','你好':'Hello'}
print(lang)

lang={'早安':'Good Morning','你好':'Hello'}
print('[你好]的英文為',lang['你好'])

lang={'早安':'Good Morning','你好':'Hello'}
print('[你好嗎]的英文為',lang['你好嗎'])

lang={'早安':'Good Morning','你好':'Hello'}
print('[你好]的英文為',lang.get('你好'))
print('[你好嗎]的英文為',lang.get('你好嗎'))
print('[你好嗎]的英文為',lang.get('你好嗎','不再字典內'))

lang={'早安':'Good Morning','你好':'Hello'}
lang['你好']='Hi'
print(lang)
lang['學生']='Student'
print(lang)

lang={'早安':'Good Morning','你好':'Hello'}
del lang['早安']
print(lang)

lang={'早安':'Good Morning','你好':'Hello'}
lang.clear()
print(lang)

a=[['早安','Good Morning'],['你好','Hello']]
dict1=dict(a)
print(dict1)
b=[('早安','Good Morning'),('你好','Hello')]
dict2=dict(b)
c=(['早安','Good Morning'],['你好','Hello'])
dict3=dict(c)
d=(('早安','Good Morning'),('你好','Hello'))
dict4=dict(d)
print(dict4)

lang1={'你好':'Hello'}
lang2={'學生':'Student'}
lang1.update(lang2)
print(lang1)
lang1={'早安':'Good Morning','你好':'Hello'}
lang2={'你好':'Hi'}
lang1.update(lang2)
print(lang1)

lang1={'早安':'Good Morning','你好':'Hello'}
lang2=lang1
lang2['你好']='Hi'
print('lang1為',lang1)
print('lang2為',lang2)
lang1={'早安':'Good Morning','你好':'Hello'}
lang3=lang1.copy()
lang3['你好']='Hi'
print('lang1為',lang1)
print('lang3為',lang3)

lang={'早安':'Good Morning','你好':'Hello'}
for ch, en in lang.items():
    print('中文為',ch,'英文為',en)
for ch in lang.keys(): 
    print(ch,lang[ch])
for en in lang.values():
    print(en)

s={1,2,3,4}
print(s)
s=set(('a',1,'b',2))
print(s)
s=set(['apple','banana','apple'])
print(s)
s=set({'早安':'Good Morning','你好':'Hello'})
print(s)
s=set('racecar')
print(s)

s=set('tiger')
print(s)
s.add('z')
print(s)
s.remove('t')
print(s)