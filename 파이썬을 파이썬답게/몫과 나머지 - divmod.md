# 몫과 나머지

## divmod
```
a = 7
b = 5
print(a // b, a % b)
```
파이썬에서는 divmod와 unpacking 이용해 다음과 같이 가능
````
a = 7
b = 5
print(*divmod(a,b))
````

**주의점**

무조건 divmod를 사용하는 게 좋은 방법은 아닙니다.

가독성이나, 팀의 코드 스타일에 따라서, a//b, a%b와 같이 쓸 때가 더 좋을 수도 있습니다.

또한, divmod는 작은 숫자를 다룰 때는 a//b, a%b 보다 느립니다. 대신, 큰 숫자를 다룰 때는 전자가 후자보다 더 빠르지요.

[stackoverflow 질문](https://stackoverflow.com/questions/30079879/is-divmod-faster-than-using-the-and-operators)