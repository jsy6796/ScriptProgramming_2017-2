import random

# 1. 한 자리 정수를 생성한다.
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# 2. number1 < number2이면  두 수를 교환한다.
if number1 < number2:
    number1, number2 = number2, number1 # 동시 할당문

# 3. "number1 - number2은/는 얼마입니까?"라고 묻는다.
answer = eval(input(str(number1) + " - " + str(number2) + \
        "은/는 얼마입니까? "))

# 4. 답을 검사하고 결과를 출력한다.
if number1 - number2 == answer:
    print("정답입니다!")
else:
    print("틀렸습니다.\n", number1 , "-",
          number2, "은/는", number1 - number2, "입니다.")
