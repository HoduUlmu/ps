# 2차원 리스트 뒤집기 - zip

내 코드

````
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def solution(mylist):
    answer = []
    for i in range(len(mylist)):
        answer.append([])

    for i in range(len(mylist)):
        for j in range(len(mylist[i])):
            answer[i].append(mylist[j][i])

    return answer
````

파이썬에서는 zip과 unpacking을 이용

````
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))
````

**zip 함수에 대해**
>zip(*iterables)는 각 iterables 의 요소들을 모으는 이터레이터를 만듭니다.
튜플의 이터레이터를 돌려주는데, i 번째 튜플은 각 인자로 전달된 시퀀스나 이터러블의 i 번째 요소를 포함합니다.

````
mylist = [1, 2, 3]
new_list = [40, 50, 60]
for i in zip(mylist, new_list):
    print (i)

(1, 40)
(2, 50)
(3, 60)
````

사용 예 1 - 여러 개의 iterable 동시 순회
````
list1 = [1, 2, 3, 4]
list2 = [100, 120, 30, 300]
list3 = [392, 2, 33, 1]
answer = []
for number1, number2, number3 in zip(list1, list2, list3):
   print(number1 + number2 + number3)
````

사용 예 2 - key 리스트와 value 리스트로 딕셔너리 생성
````
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds)) # {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}
````
