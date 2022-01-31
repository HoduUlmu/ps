import collections
import itertools


def solution(id_list, report, k):
    reported_dic = collections.defaultdict(list)
    for case in set(report):
        who_report, who_reported = case.split()
        reported_dic[who_reported].append(who_report)

    mail_list = list(itertools.chain(*(x for x in reported_dic.values() if len(x) >= k)))
    counter = collections.Counter(mail_list)
    result = [counter.get(_id) if counter.get(_id) else 0 for _id in id_list]
    return result

# 테스트 1 〉	통과 (0.03ms, 10.2MB)
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (152.88ms, 46.7MB)
# 테스트 4 〉	통과 (0.07ms, 10.3MB)
# 테스트 5 〉	통과 (0.05ms, 10.3MB)
# 테스트 6 〉	통과 (0.75ms, 10.4MB)
# 테스트 7 〉	통과 (1.21ms, 10.8MB)
# 테스트 8 〉	통과 (1.62ms, 11.2MB)
# 테스트 9 〉	통과 (56.75ms, 27MB)
# 테스트 10 〉	통과 (45.76ms, 27MB)
# 테스트 11 〉	통과 (129.49ms, 46.5MB)
# 테스트 12 〉	통과 (0.24ms, 10.3MB)
# 테스트 13 〉	통과 (0.20ms, 10.3MB)
# 테스트 14 〉	통과 (44.42ms, 24.3MB)
# 테스트 15 〉	통과 (80.38ms, 36.8MB)
# 테스트 16 〉	통과 (0.15ms, 10.3MB)
# 테스트 17 〉	통과 (0.20ms, 10.3MB)
# 테스트 18 〉	통과 (0.39ms, 10.4MB)
# 테스트 19 〉	통과 (0.53ms, 10.4MB)
# 테스트 20 〉	통과 (41.13ms, 24.2MB)
# 테스트 21 〉	통과 (81.56ms, 36.7MB)
# 테스트 22 〉	통과 (0.03ms, 10.1MB)
# 테스트 23 〉	통과 (0.03ms, 10.2MB)
# 테스트 24 〉	통과 (0.03ms, 10.3MB)