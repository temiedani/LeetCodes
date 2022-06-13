from collections import deque
import threading
import time

qq = deque()

#  Queue works first in first out FIFO
qq.appendleft(1)
qq.appendleft(2)
qq.appendleft(3)

# use qq.appendleft() to add to the queue
# use qq.pop to remove the last element


class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


def place_orders(orders):
    for order in orders:
        print("Placing order for:", order)
        food_order_queue.enqueue(order)
        time.sleep(0.5)


def serve_orders():
    time.sleep(1)
    while food_order_queue.size() > 0:
        order = food_order_queue.dequeue()
        print("Now serving: ", order)
        time.sleep(2)


if __name__ == "__main__":
    pq = Queue()
    # add element to the que
    pq.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.01 AM',
        'price': 131.10
    })
    pq.enqueue({
        'company': 'Asda',
        'timestamp': '15 apr, 11.02 AM',
        'price': 132
    })
    pq.enqueue({
        'company': 'Tesco',
        'timestamp': '15 apr, 11.03 AM',
        'price': 135
    })
    # get size of the queue
    print(pq.size())
    # 3

    # remove from the queue
    print(pq.dequeue())
    # {'company': 'Wall Mart', 'timestamp': '15 apr, 11.01 AM', 'price': 131.1}

    # check is queue is empty
    print(pq.is_empty())
    # False

    food_order_queue = Queue()

    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    t1 = threading.Thread(target=place_orders, args=(orders,))
    t2 = threading.Thread(target=serve_orders)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done Serving")
