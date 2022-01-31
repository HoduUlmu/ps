# i번째 원소와 i+1번째 원소 - zip

내 코드
````
def solution(mylist):
    answer = []
    for i in range(len(mylist) - 1):
        answer.append(abs(mylist[i] - mylist[i + 1]))
    return answer
````

파이썬의 zip을 이용하면 index 사용하지 않아도됨

````
def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
    return answer

if __name__ == '__main__':
    mylist = [83, 48, 13, 4, 71, 11]    
    print(solution(mylist))
````

**주의**

zip 함수에 서로 길이가 다른 리스트가 인자로 들어오는 경우에는 길이가 짧은 쪽 까지만 이터레이션이 이루어집니다

[zip 공식 레퍼런스](https://docs.python.org/3/library/functions.html?highlight=built%20function#zip)