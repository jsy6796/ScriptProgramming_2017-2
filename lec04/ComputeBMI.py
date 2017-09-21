# 사용자로부터 파운드 단위의 몸무게를 입력받는다.
weight = eval(input("몸무게(파운드)를 입력하세요: "))

# 사용자로부터 인치 단위의 키를 입력받는다.
height = eval(input("키(인치)를 입력하세요: "))

KILOGRAMS_PER_POUND = 0.45359237 # 상수
METERS_PER_INCH = 0.0254 # 상수

# BMI를 계산한다.
weightInKilograms = weight * KILOGRAMS_PER_POUND
heightInMeters = height * METERS_PER_INCH
bmi = weightInKilograms / (heightInMeters * heightInMeters)

# 결과를 출력한다.
print("BMI는", format(bmi, ".2f"), "입니다.")
if bmi < 18.5:
    print("저체중")
elif bmi < 25:
    print("정상")
elif bmi < 30:
    print("과체중")
else:
    print("비만")
