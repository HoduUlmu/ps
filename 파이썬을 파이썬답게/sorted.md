# sorted

원본을 유지한채, 정렬된 리스트 구학

보통 deep copy와 sort 사용
````
list1 = [3, 2, 5, 1]
list2 = [i for i in list1]
list2.sort()
````

파이썬에서는 sorted 사용
````
list1 = [3, 2, 5, 1]
list2 = sorted(list1)
````

