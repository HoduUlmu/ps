# value 와 다음 Node 를 참조하는 Node 클래스
# next 는 python 내장 함수에 있기에 nxt 이름 변경
class Node:
    def __init__(self, val, nxt):
        self.val = val
        self.nxt = nxt


class Stack:
    # 첫 생성 시 현재 스택의 top 은 없기에 None
    def __init__(self):
        self.top = None

    # 새로운 value 를 push 할 시 새로운 Node 를 생성해 top을 바꿔줌
    # 이 떄 새로운 Node 이자 top 은 nxt 로 이전 top 을 가리킴
    def push(self, val):
        self.top = Node(val, self.top)

    # 가장 최근에 들어온 값을 삭제 하는 pop 함수 (LIFO)
    # 스택이 비었으면 None 리턴
    # 아니라면 현재 top 의 아이템을 변수에 할당 후 리턴
    # 현재 top 을 현재 top의 nxt로 바꿔줌
    def pop(self):
        if self.is_empty():
            return None
        else:
            top_node_item = self.top.val
            self.top = self.top.nxt
            return top_node_item

    # top 의 유무를 확인해 없으면 스택이 빈 것이니 True, 아니면 스택이 차있는 것이니 False
    def is_empty(self):
        return not self.top
