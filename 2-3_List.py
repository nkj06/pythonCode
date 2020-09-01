odd = [1, 3, 5, 7, 9] # 리스트명 = [요소1, 요소2, 요소3, ...]

# 리스트의 생김새
a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

a = list() # 비어있는 리스트, a = []와 같음

# 리스트의 인덱싱
a = [1, 2, 3]
print(a) # [1, 2, 3]
print(a[0]+a[2]) # 1 + 3 
print(a[-1]) # 리스트 a의 마지막 3

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0]) # 1
print(a[-1]) # a[3]과 같음, ['a', 'b', 'c'] 출력

print(a[-1][0]) # 리스트 a에 포함된 'a'
print(a[-1][1]) # b
print(a[-1][2]) # c

# 삼중 리스트에서 인덱싱
a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[2][2][0]) # Life

# 리스트의 슬라이싱
a = [1, 2, 3, 4, 5]
b = a[:2] 
c = a[2:] 

print(a[0:2])  # [1, 2]
print(b) # [1, 2]
print(c) # [3, 4, 5]

# 중첩된 리스트에서 슬라이싱
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5]) # [3, ['a', 'b', 'c'], 4]
print(a[3][:2]) # ['a', 'b']

# 리스트 연산하기
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b) # 리스트 a, b 합치기 / [1, 2, 3, 4, 5, 6]
print(a * 3) # 리스트 반복 / [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(len(a)) # 리스트 길이 / 3

# 리스트 수정과 삭제
a = [1, 2, 3]
a[2] = 4
print(a) # [1, 2, 4]

# del 함수 사용해 리스트 요소 삭제
a = [1, 2, 3]
del a[1]
print(a) # print 안에 del a[1]을 넣으면 오류 남 / [1, 3]

a = [1, 2, 3, 4, 5]
del a[2:]
print(a) # [1, 2]

# 리스트 관련 함수들
a = [1, 2, 3]
a.append(4) # 리스트에 요소 추가
print(a) # [1, 2, 3, 4]
a.append([5, 6])
print(a) # [1, 2, 3, 4, [5, 6]]

a = [1, 4, 3, 2]
a.sort() # 리스트 정렬
print(a) # [1, 2, 3, 4]

a = ['a', 'c', 'b']
a.sort() 
print(a) # [a, b, c]

a = ['a', 'b', 'c']
a.reverse() # 리스트 뒤집기
print(a) # ['c', 'b', 'a']

a = [1, 2, 3]
print(a.index(3)) # 위치 반환 / 2
print(a.index(1)) # 0, 존재하지 않는 값은 오류 발생

a.insert(0, 4) # 리스트에 요소 삽입
print(a) # [4, 1, 2, 3]
a.insert(3, 5)
print(a) # [4, 1, 2, 5, 3]

a = [1, 2, 3, 1, 2, 3]
a.remove(3) # 리스트 요소 제거
print(a) # [1, 2, 1, 2, 3]
a.remove(3) 
print(a) # [1, 2, 1, 2]

a = [1, 2, 3]
print(a.pop()) # 리스트 맨 마지막 요소를 돌려주고 삭제 / 3
print(a) # [1, 2]
a = [1, 2, 3]
print(a.pop(1)) # 1의 요소를 돌려주고 삭제 / 2
print(a) # [1, 3]

a = [1, 2, 3, 1]
print(a.count(1)) # 리스트에 포함된 요소 x의 개수 세기 / 2

a = [1, 2, 3]
a.extend([4, 5]) # 리스트 확장, a += [4, 5]와 동일
print(a) # [1, 2, 3, 4, 5]
b = [6, 7]
a.extend(b)
print(a) # [1, 2, 3, 4, 5, 6, 7]