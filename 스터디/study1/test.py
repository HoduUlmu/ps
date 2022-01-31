from 스터디.study1.stack import Stack


def test_stack():
    """
    스택은 3가지 기능을 요구
    1. push
    2. pop
    3. is_empty
    """
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    assert stack.pop() == 5
    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None
    assert stack.is_empty()


if __name__ == "__main__":
    test_stack()
