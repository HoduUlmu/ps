import collections


def solution(id_list, report, k):
    reported_dic = collections.defaultdict(set)
    for case in report:
        who_report, who_reported = case.split()
        reported_dic[who_reported].add(who_report)

    mail_list = []
    for val in reported_dic.values():
        if len(val) >= k:
            val = list(val)
            for x in val:
                mail_list.append(x)

    mail_list_counter = collections.Counter(mail_list)

    result = []
    for id in id_list:
        mail_num = mail_list_counter.get(id)
        if mail_num is None:
            result.append(0)
        else:
            result.append(mail_num)
    return result

# 테스트 1 〉	통과 (0.03ms, 10.3MB)
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (130.78ms, 45.5MB)
# 테스트 4 〉	통과 (0.08ms, 10.1MB)
# 테스트 5 〉	통과 (0.05ms, 10.3MB)
# 테스트 6 〉	통과 (0.78ms, 10.5MB)
# 테스트 7 〉	통과 (1.75ms, 10.7MB)
# 테스트 8 〉	통과 (3.16ms, 10.9MB)
# 테스트 9 〉	통과 (65.54ms, 27.1MB)
# 테스트 10 〉	통과 (44.47ms, 26.2MB)
# 테스트 11 〉	통과 (99.48ms, 44.8MB)
# 테스트 12 〉	통과 (0.26ms, 10.3MB)
# 테스트 13 〉	통과 (0.35ms, 10.3MB)
# 테스트 14 〉	통과 (52.23ms, 23.9MB)
# 테스트 15 〉	통과 (89.04ms, 38.6MB)
# 테스트 16 〉	통과 (0.16ms, 10.3MB)
# 테스트 17 〉	통과 (0.20ms, 10.3MB)
# 테스트 18 〉	통과 (0.38ms, 10.4MB)
# 테스트 19 〉	통과 (0.60ms, 10.5MB)
# 테스트 20 〉	통과 (49.54ms, 24MB)
# 테스트 21 〉	통과 (101.43ms, 39.3MB)
# 테스트 22 〉	통과 (0.04ms, 10.1MB)
# 테스트 23 〉	통과 (0.03ms, 10.2MB)
# 테스트 24 〉	통과 (0.03ms, 10.2MB)