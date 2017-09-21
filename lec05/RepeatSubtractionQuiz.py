import random

# 1. 두 개의 한 자리 정수를 랜덤으로 생성한다.
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# 2. number1 < number2이면, number1과 number2를 교환한다.
if number1 < number2:
    number1, number2 = number2, number1

# 3. 사용자료부터 "number1 - number2는 얼마입니까?"에 대한 답을 입력받는다.
answer = eval(input(str(number1) + " - "
    + str(number2) + "은/는 얼마입니까? "))

# 4. 정확한 답을 입력할 때까지 질문을 반복한다.
while number1 - number2 != answer:
    answer = eval(input("틀렸습니다. 다시 해보세요. "
        + str(number1) + " - " + str(number2) + "은/는 얼마입니까? "))

print("정답!")
