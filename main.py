## 함수
def add_func(n1, n2):
    return n1 + n2

def sub_func(n1, n2):
    return n1 - n2

def mul_func(n1, n2):
    return n1 * n2

def div_func(n1, n2):
    return n1 / n2


## 변수
num1, num2, res = 100, 200, 0


##메인
res = add_func(num1, num2)
print(num1, '+', num2, '=', res)

res = sub_func(num1, num2)
print(num1, '-', num2, '=', res)

res = mul_func(num1, num2)
print(num1, '*', num2, '=', res)

<<<<<<< Updated upstream
res = div_func(num1, num2)
print(num1, '/', num2, '=', res)
=======
res = pow_func(num1, num2)
print(num1, '**', num2, '=', res)
>>>>>>> Stashed changes
