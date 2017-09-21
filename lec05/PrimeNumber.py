NUMBER_OF_PRIMES = 50  # 출력되어야 하는 소수의 개수
NUMBER_OF_PRIMES_PER_LINE = 10 # 한 행당 출력되는 소수의 개수
count = 0 # 소수의 개수를 센다.
number = 2 # 소수성을 검사해야 하는 숫자

print("첫 50개의 소수")

# 반복적으로 소수를 찾는다.
while count < NUMBER_OF_PRIMES:
    # number가 수소라고 가정한다.
    isPrime = True # 현재 number가 소수인가?

    # number가 소수인지 검사한다.
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # 참이라면 number는 소수가 아니다.
            isPrime = False  # isPrime을 거짓으로 설정한다.
            break  # while 루프를 종료한다.
        divisor += 1

    # 소수를 출력하고 count를 증가시킨다.
    if isPrime:
        count += 1 # count를 증가시킨다.

        print(format(number, '5d'), end = '')
        if count % NUMBER_OF_PRIMES_PER_LINE == 0:
            # number를 출력하고 다음 행으로 진행한다.
            print() # 다음행으로 건너뛴다.

    # 다음 number가 소수인지 검사한다.
    number += 1
