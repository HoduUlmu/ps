# for문과 if문을 한번에 - list comprehension의 if문

내 코드
````
def solution(mylist):
    answer = [element**2 for element in mylist if element % 2 == 0]
    return answer
````

보통 언어의 코드
for 문 안의 조건문을 사용해 2-depth 블록

````
mylist = [3, 2, 6, 7]
answer = []
for number in mylist:
    if number % 2 == 0:
        answer.append(number**2) # 들여쓰기를 두 번 함
````

파이썬에서는

파이썬의 list comprehension을 사용하면 한 줄 안에 for 문과 if 문을 한 번에 처리할 수 있습니다.

````
mylist = [3, 2, 6, 7]
answer = [number**2 for number in mylist if number % 2 == 0]
````

[list compre hension syntax1](https://docs.python.org/3/reference/expressions.html?highlight=list%20comprehension#displays-for-lists-sets-and-dictionaries)
