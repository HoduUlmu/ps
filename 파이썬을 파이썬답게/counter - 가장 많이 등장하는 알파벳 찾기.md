# 가장 많이 등장하는 알파벳 찾기 - Counter

내 코드
````
import collections
my_str = input().strip()
doc = collections.defaultdict(int)
for char in my_str:
    doc[char] += 1

print(''.join(sorted([k for k, v in doc.items() if max(doc.values()) == v])))
````

보통 언어
````
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = {}
for number in my_list:
    try:
        answer[number] += 1
    except KeyError:
        answer[number] = 1

print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100])  # =  raise KeyError
````

파이썬에서 collections.Counter 클래스를 쓰면 간단히 작성 가능

````
import collections
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = collections.Counter(my_list)

print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100]) # = 0
````