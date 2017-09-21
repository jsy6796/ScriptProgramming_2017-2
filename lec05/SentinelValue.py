sum = 0

data = eval(input("정수를 입력하세요 (입력이 0이면 " +  \
    "종료됩니다): "))

# 입력이 0이 아닐 때까지 데이터를 계속 읽는다.
while data != 0:
    sum += data
    data = eval(input("정수를 입력하세요 (입력이 0이면 " +  \
        "종료됩니다): "))

print("합계는", sum, "입니다.")
