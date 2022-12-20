# print('\'i am so happy\'') #이스케이프 코드
# print("'i am so happy'") # 다른 따옴표 쓰기
#-----
# b = 'super man'
# print('i am a %s'%b)
#------
# a = 3
# print('i have %d dollor'%a)
#-------
# a = 3.5
# print('i have %f dollor'%a)
# print('i have %.1f dollor'%a)
# print('i have %.2f dollor'%a)
# print('i have %.f dollor'%a)
# print('i have %.d dollor'%a)
#-------
# a = 'apple'
# b = 10
# print('i ate an %s for %d days'%(a,b))
#-------
# a = 3
# b = 'so happy'
# print('i have {0} dollar {1}'.format(a,b))
# print('i have {0} dollar {feel}'.format(a,feel='happy'))
#-----
# a = 'i am a boy'
# print(a.upper())
# print(a.lower())
# print(a.islower())
# a = a.capitalize()
# print(a.islower())
#------
# a = 'haha i am a boy ha'
# print(a.lstrip('ah i'))
#------
# aa = 'i am a good boy'
# print(aa.replace('boy','girl'))
# b = aa.split()
# print(b)
#--------
# a = [1,2,3]
# print(a*2)
# del a[3:]
# print(a)
#---------
# a += [7,8,9]
# a = a+[7,8,9]
# a.extend([7,8,9])
#--------
# a = [1,5,2,3,8,45,5]
# a,sort()
# print(a)
# a.sort(reverse=True)
# print(a)

b = [1,5,2,3,8,45,3,5]
# c = sorted(b)
t = b.pop(3)
print(t)
print(b)
# print(c)