"""
Your task is to slightly extend the Queue class' capabilities. We want 
it to have a parameterless method that returns True if the queue is 
empty and False otherwise.

Expected output

1
dog
False
Queue empty

"""

class QueueError(IndexError):  # Choose base class for the new exception.
    def __init__(self):
        IndexError.__init__(self)


class Queue:
    def __init__(self):
        self.elements = []

    def put(self, elem):
        self.elements.insert(0, elem)

    def get(self):
        try:
            elem = self.elements[-1]
            del self.elements[-1]
        except:
            raise QueueError
        return elem


class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
    
    def isempty(self):
        if len(self.elements) == 0:
            return True
        else:
            return False


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")