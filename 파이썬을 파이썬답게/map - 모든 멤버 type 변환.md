# 모든 멤버의 type 변환하기 - map

내 코드

````
def solution(mylist):
    answer = list(map(int, mylist))
    return answer
````
파이썬에서는 파이썬의 map을 사용하면 for 문을 사용하지 않고도 멤버의 타입을 일괄 변환할 수 있습니다.

리스트 각 요소의 길이로 변환
````
def solution(mylist):
    answer = list(map(len, mylist))
    return answer
````