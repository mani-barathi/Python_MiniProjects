class Queue:
  def __init__(self):
    self.queue = list()

  def isEmpty(self):
    if len(self.queue) == 0:
      return False
    return True

  def length(self):
    return len(self.queue)

  def enqueue(self,element):
    self.queue.append(element)

  def dequeue(self):
    if self.isEmpty():
      element = self.queue.pop(0)
      return element
    return 'Error'

q = Queue()

q.enqueue(10)
q.enqueue(20)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
  