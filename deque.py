class Deque:
    def __init__(self):
        self.stack = []

    def addFront(self, item):
        array = self.stack
        array.append(item)
        self.stack = array
    def addTail(self, item):
        a = []
        a.append(item)
        for i in self.stack:
            a.append(i)
        self.stack = a
    def removeFront(self):
        if len(self.stack) != 0:
            a = self.stack[len(self.stack)-1]
            del self.stack[len(self.stack)-1]
            return a
        else:
            return None # если очередь пуста
    def removeTail(self):
        # удаление из хвоста
        if len(self.stack) != 0:
            a = self.stack[0]
            del self.stack[0]
            return a
        else:
            return None # если очередь пуста
    def size(self):
        return len(self.stack) # размер очереди
def palindrom(str):
    deq = Deque()
    for i in str:
        deq.addFront(i)
    while deq.size() > 0:
        if  deq.removeFront() != deq.removeTail() and deq.size() !=1:
            return False
        elif deq.size() ==1:
            return True
    return True

deq = Deque()
deq.addFront("f1")
deq.addTail("t1")
deq.addFront("f2")
deq.addTail("t2")
while deq.size() > 0:
    print(deq.removeFront())
    print(deq.removeTail())
print(deq.size())