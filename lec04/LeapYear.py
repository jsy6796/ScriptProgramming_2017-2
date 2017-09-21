year = eval(input("연도를 입력하세요: "))

# 연도가 윤년인지 검사한다.
isLeapYear = (year % 4 == 0 and year % 100 != 0) or \
                (year % 400 == 0)

# 결과를 출력한다.
print(year, "년은 윤년입니까?", isLeapYear)
