print("            구구단표")

# 표 머리글을 출력한다
print("  |", end = '')
for j in range(1, 10):
    print("  ", j, end = '')
print() # 새로운 행으로 건너뛴다.
print("-----------------------------------------")

# 표 몸체를 출력한다.
for i in range(1, 10):
    print(i, "|", end = '')
    for j in range(1, 10):
        # 곱셈 결과를 출력하고 적절하게 정렬한다.
        print(format(i * j, '4d'), end = '')
    print()# 새로운 행으로 건너뛴다.
    
