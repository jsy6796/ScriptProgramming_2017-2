import random

# 랜덤 숫자를 생성한다.
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# 사용자로부터 답을 입력받는다.
answer = eval(input(str(number1) + " + "
    + str(number2) + "은/는 얼마입니까? "))

# 결과를 출력한다.
print(number1, "+", number2, "=", answer,
    "은/는", number1 + number2 == answer)
