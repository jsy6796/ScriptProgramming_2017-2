year = eval(input("연도를 입력하세요: "))
zodiacYear = year % 12
if zodiacYear == 0:
    print("원숭이")
elif zodiacYear == 1:
    print("닭")
elif zodiacYear == 2:
    print("개")
elif zodiacYear == 3:
    print("돼지")
elif zodiacYear == 4:
    print("쥐")
elif zodiacYear == 5:
    print("소")
elif zodiacYear == 6:
    print("범")
elif zodiacYear == 7:
    print("토끼")
elif zodiacYear == 8:
    print("용")
elif zodiacYear == 9:
    print("뱀")
elif zodiacYear == 10:
    print("말")
else:
    print("양")
