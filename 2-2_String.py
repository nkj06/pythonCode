# '와 " 표현
food = "Python's favorite food is perl"
say = '"Python is very easy." he says.'

print(food)
print(say)

# 문자열 여러 개 사용
multlint = """
Life is too short
You need python
"""
print(multlint)

#문자열 연산
head = "Python"
tail = " is fun!"
print(head + tail) #연결
print(head * 2) #반복

print(len(head)) #문자열 길이

# 문자열 인덱싱 (문자마다 번호를 매김, 공백 포함)
a = "Life is too short, You need Python"
print(a[12]) 
print(a[-1]) #뒤에서부터

# 문자열 슬라이싱 a[시작 번호:끝 번호]
print(a[0:4]) # 끝 번호에 해당하는 것은 포함하지 않는다.
print(a[19:]) # 문자열의 끝까지 출력
print(a[:17]) # 문자열의 처음부터 끝 번호까지 출력
print(a[:]) # 문자열의 처음부터 끝까지 출력
print(a[19:-7]) # 19에서부터 -8까지

b = "20010331Rainy"
year = b[:4]
day = b[4:8]
weather = b[8:]
print(year)
print(day)
print(weather)

# 문자열 변경 (슬라이싱 이용)
c = "pithon"
c = c[:1] + 'y' + c[2:]
print(c)

# 문자열 포매팅
print("I eat %d apples." % 3)
print("I eat %s apples." % "five")

number = 3
print("I eat %d apples." % number)

number = 10
day = "three"
print("I ate %d apples. so I was sick for %s day." % (number, day))

# 문자열 포맷 코드 
# (%s 문자열, %c 문자 1개, %d 정수, %f 부동소수, %o 8진수, %x 16진수, %% 문자%)

# 포맷 코드와 숫자 사용
print("%10s" % "hi")
print("%-10sjane." % 'hi')
print("%0.4f" % 3.42134234)
print("%10.4f" % 3.42134234)

# fornat 함수를 사용한 포매팅
print("I eat {0} apples".format(3)) # 숫자 대입
print("I eat {0} apples".format("five")) # 문자열 대입
print("I eat {0} apples".format(number)) # 숫자 값을 가진 변수로 대입
print("I ate {0} apples. so I was sick for {1} days.".format(number, day)) # 2개 이상의 값
print("I ate {number} apples. so I was sick for {day} days.".format(number=3, day=3))
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))

# 정렬
print("{0:<10}".format("hi")) # 왼쪽
print("{0:>10}".format("hi")) # 오른쪽
print("{0:^10}".format("hi")) # 가운데
print("{0:=^10}".format("hi")) # 공백에 = 채우기
print("{0:!<10}".format("hi")) # 공백에 ! 채우기 2

# 소수점 표현
x = 3.42134234
print("{0:0.4f}".format(x))
print("{0:10.4f}".format(x))
print("{{ and }}".format())

# f 문자열 포매팅
name = '남경진'
age = 25
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print(f'나는 내년이면 {age+1}살이 된다.')

d = {'name':'남경진', 'age':25}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

print(f'{"hi":<10}') # 왼쪽 정렬
print(f'{"hi":>10}') # 오른쪽 정렬
print(f'{"hi":^10}') # 가운데 정렬

print(f'{"hi":=^10}') # 가운데 정렬하고 '=' 문자로 공백 채우기
print(f'{"hi":!<10}') # 왼쪽 정렬하고 '!' 문자로 공백 채우기

y = 3.42134234
print(f'{y:0.4f}') # 소수점 4자리까지만 표현
print(f'{y:10.4f}') # 소수점 4자리까지 표현하고 총 자리수를 10으로 맞춤

print(f'{{and}}') # 문자 { } 표시

# 문자열 관련 함수들
a = "hobby"
print(a.count('b')) # 문자 개수 세기

a = "Python is the best choice"
print(a.find('b')) # 위치 알려주기 
print(a.find('k')) # 존재하지 않는 문자는 -1을 반환

a = "Life is too short"
print(a.index('t')) # 위치 알려주기 2, 존재하지 않는 문자면 오류

print(",".join('abcd')) # 문자열 삽입
print(",".join(['a', 'b', 'c', 'd']))

a = "hi"
print(a.upper()) # 소문자를 대문자로 바꾸기
a = "HI"
print(a.lower()) # 대문자를 소문자로 바꾸기

a = " hi "
print(a.lstrip()) # 왼쪽 공백 지우기
print(a.rstrip()) # 오른쪽 공백 지우기
print(a.strip()) # 양쪽 공백 지우기

a = "Life is too short"
print(a.replace("Life", "Your leg")) # 문자열 바꾸기

print(a.split()) # 문자열 나누기

b = "a:b:c:d"
print(b.split(':')) # 문자열 나누기