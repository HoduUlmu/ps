# 곱집합 구하기 - product

보통 언어의 코드

````
iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'

for value1 in iterable1:
    for value2 in iterable2:
        for value3 in iterable3:
            print(value1, value2, value3)
````

파이썬에서는

itertools.product를 사용

````
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
print(list(itertools.product(iterable1, iterable2, iterable3)))
````          

[itertools.product](https://docs.python.org/3/library/itertools.html#itertools.product)