from math import *
const=e
flag=[0]#счетчик,где находится курсор
def first_prior():#число,унарный минус,скобки
    start=flag[0]
    if s[flag[0]] == 'e':#экспонента,ввод: e^x
        flag[0]+=2
        st=first_prior()
        return const**st
    if  s[flag[0]]=='-':
        flag[0]+=1
        value=first_prior()
        return -value
    if s[flag[0]]=='(':
        flag[0]+=1
        v_skobkax=third_prior()
        flag[0]+=1
        return v_skobkax
    while len(s)>flag[0] and (s[flag[0]].isdigit() or s[flag[0]]=='.'):
        flag[0]+=1
    return float(s[start:flag[0]])
def second_prior():#умножение и деление
    res=first_prior()
    while len(s)>flag[0] and s[flag[0]] in '*/':
        if s[flag[0]]=='*':
             flag[0]+=1
             second_num=first_prior()
             res*=second_num
        elif s[flag[0]]=='/':
            flag[0]+=1
            second_num=first_prior()
            res/=second_num
    return res
def third_prior():#плюс,минус
    res=second_prior()
    while len(s)>flag[0] and s[flag[0]] in '+-':
        if s[flag[0]]=='+':
            flag[0]+=1
            second_num=second_prior()
            res+=second_num
        elif s[flag[0]]=='-':
            flag[0]+=1
            second_num=second_prior()
            res-=second_num
    return res
def fourth_prior():
    res=third_prior()
    if len(s)>flag[0] and s[flag[0]]=='<':
        flag[0]+=2
        second_num=third_prior()
        if res<=second_num:
            return "YES"
        else:
            return "NO"
    return res
s=input("введите выражение:")
flag[0]=0
result=fourth_prior()
if result=="YES" or result=="NO":
    print(str(result))
elif result.is_integer():
    print(int(result))
else:
    print(round(result,10))














