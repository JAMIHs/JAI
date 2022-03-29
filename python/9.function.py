def sum(l,r):
    return l+r
def min(l,r):
    return l-r
def mul(l,r):
    return l*r
def div(l,r):
    return l/r

num1 = float(input('첫번째 숫자? '))
num2 = input('기호? ')
num3 = float(input('두번째 숫자? '))

if num2 =='+':
    print(sum(num1,num3))
else: 
    if num2 == '-':
        print(min(num1,num3))
    else:
        if num2=='*':
            print(mul(num1,num3))
        else:
            if num2=='/': 
                print(div(num1,num3))
            else:
                print('기호를 잘못입력하셨습니다')
                
