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
