# sequence 멤버를 하나로 이어붙이기

내 코드
````
def solution(mylist):
    answer = list(map(len, mylist))
    return answer
````
파이썬에서는

파이썬의 str.join(iterable)을 사용하면 이 코드를 두 줄로 줄일 수 있습니다.


보통 언어에서의 코드
````
my_list = ['1', '100', '33']
answer = ''
for value in my_list:
    answer += value
````