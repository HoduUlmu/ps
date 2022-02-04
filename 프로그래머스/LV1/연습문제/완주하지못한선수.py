import collections


def solution(participant, completion):
    counter = collections.Counter(participant)
    counter.subtract(completion)
    return counter.most_common(1)[0][0]


solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])

#import collections
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]
