li = ['3', '30', '300', '34', '5', '9', '905']
li.sort(reverse=True)
print(li)
i = 1
while i < len(li):
    if li[i - 1] + li[i] < li[i] + li[i - 1]:
        li[i - 1], li[i] = li[i], li[i - 1]

    if int(li[i]) % 10 == 0 and li[i][0] == li[i + 1][0]:
        start = i
        ans = []
        while i < len(li) - 1 and li[i][0] == li[i + 1][0]:
            ans.append(li[i])
            i += 1
        ans.append(li[i])
        end = i
        ans.sort(key=len)
        li = li[:start] + li[]

    i += 1
print(li)
