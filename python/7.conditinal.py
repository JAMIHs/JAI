from re import T


print(1)
if True:
    print(2)
    print(3)
print(4)

print(1)
if True:
    print(2.1)
    print(3.1)
else:
    print(2.2)
    print(3.3)
print(4)

input_id = input('아이디? ')
input_pwd = input('비밀번호? ')
if input_id == 'egoing' :
    if input_pwd == '111111':
        print('안녕하세요')
    else:
        print('비밀번호가 다릅니다')
else:
    print('아이디가 다릅니다?')