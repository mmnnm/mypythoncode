import os
import re
import random

rule=re.compile('\*.*')
group_1=[]
st1=os.popen('net localgroup').readlines()
for i in st1:
    if rule.search(i):
        #print('1:',i)
        group_1.append(i.strip('\n').strip('*'))
       # print(len(i))
    # else:
    #     print('0:',i)
print('\n\n','↓↓↓↓↓↓↓↓↓↓↓↓')
for i in group_1:
    command='net localgroup '+'"'+i+'"'
    st2=os.popen(command).readlines()
    # print(len(st2))
    # print(st2)
    if len(st2)==8:
        pass
    else:
        # print(st2)
        print('用户组<',st2[0].strip('别名').strip(),'>下有用户：')
        for j in range(6,len(st2)-2):
            print(st2[j].strip())
        print('--------------')
print('↑↑↑↑↑↑↑↑↑↑↑↑','\n\n')
input()
s='1234567890abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
