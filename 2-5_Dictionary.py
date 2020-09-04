# 딕셔너리? 
# 순차적으로 해당 요솟값을 구하지 않고 Key를 통해 Value를 얻음

# 딕셔너리 생성
# Key는 name, phone, birth / Value는 nam, 01012341234, 0610
dic = {'name':'nam', 'phone':'01012341234', 'birth':'0610'}
a = {1:'hi'}
a = {'a':[1,2,3]}

# 딕셔너리 쌍 추가
a = {1:'a'}
a[2] = 'b'
print(a) # {1:'a', 2:'b'}

a['name'] = 'pey'
print(a) # {1:'a', 2:'b', 'name':'pey'}

a[3] = [1, 2, 3]
print(a) # {1:'a', 2:'b', 'name':'pey', 3:[1,2,3]}

# 딕셔너리 요소 삭제
del a[1] # del a[key]
print(a) # {2:'b', 'name':'pey', 3:[1,2,3]}

# 딕셔너리 사용 방법
grade = {'pey':10, 'julliet':99}
print(grade['pey']) # 10
print(grade['julliet']) #99

a = {1:'a', 2:'b'}
print(a[1]) # a

dic = {'name':'nam', 'phone':'01012341234', 'birth':'0610'}
print(dic['name']) # nam
print(dic['phone']) # 01012341234
print(dic['birth']) # 0610

# 딕셔너리 만들 때 주의할 사항
# 동일한 Key가 2개 존재할 경우 1:'a' 쌍이 무시 됨
# Key에 리스트 불가능, 튜플은 가능
# Value에는 아무 값이나 넣을 수 있다.

# 딕셔너리 관련 함수들
a = {'name':'nam', 'phone':'01012341234', 'birth':'0610'}
print(a.keys()) # Key 리스트 만들기 / dict_keys(['name', 'phone', 'birth'])

for k in a.keys():
    print(k) 

print(list(a.keys())) # dict_keys 객체를 리스트로 변환

print(a.values()) # Value 리스트 만들기