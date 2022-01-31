from 스터디.study2.queue import Queue


def test_queue():
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.dequeue() == 4
    assert queue.dequeue() == 5
    assert queue.is_empty()


if __name__ == "__main__":
    test_queue()
