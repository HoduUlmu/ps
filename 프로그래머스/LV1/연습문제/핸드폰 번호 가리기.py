import string


def solution(phone_number: str) -> str:
    return '*' * len(phone_number[:-4]) + phone_number[-4:]


solution('01033334444')