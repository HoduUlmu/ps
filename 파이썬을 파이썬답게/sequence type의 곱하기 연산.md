# sequece type의 * 연산

내 코드
````
n = int(input().strip())
for i in range(n):
    print('*' * (i + 1))
````

보통 언어에서의 코드
````
answer = ''
n = 어쩌고
for _ in range(n):
    answer += 'abc'
````

파이썬에서는

파이썬에서는 *연산자를 사용해 코드를 획기적으로 줄일 수 있습니다.

````
n = 어쩌고
answer = 'abc' * n
````

또, * 연산자를 이용하면 [123, 456, 123, 456, 123 ...] 과같이 123, 456이 n번 반복되는 리스트를 만들 수 있습니다.

````
n = 어쩌고
answer= [123, 456] * n
````