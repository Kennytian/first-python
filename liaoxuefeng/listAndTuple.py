# coding: utf-8
print('--List--')
classmates = ['Angla', '天天', '森碟']
print(classmates)
print(len(classmates))
print('classmates[-1]:', classmates[-1])
print('classmates[-2]:', classmates[-2])
print('classmates[-3]:', classmates[-3])
classmates.append('Jerry')
print(classmates)
print('classmates[0]:', classmates[0])
print('classmates[1]:', classmates[1])
print('classmates[2]:', classmates[2])
classmates.insert(1, 'Kenny')
print(classmates)

print('--Tuple--')
workmates = ('Tom', '小四', '大佬')
print('workmates:', workmates)
t = (1, 2)
print(t)
t = ()
print('empty tuple t:', t)
t = (1)
print(t)
t = (1,)
print(t)
t = ('a', 'b', ['C', 'D'], 'e')
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
