# 225.用队列实现栈
"""
请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。

实现 MyStack 类：

void push(int x) 将元素 x 压入栈顶。
int pop() 移除并返回栈顶元素。
int top() 返回栈顶元素。
boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。

注意：
你只能使用队列的标准操作 —— 也就是 push to back、peek/pop from front、size 和 is empty 这些操作。
你所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
"""

from collections import deque

class MyStack:

    def __init__(self):
        # 使用两个队列实现栈，其中一个队列用来备份，一个队列用来实现进出
        self.curQueue = deque()
        self.backUpQueue = deque()

    def push(self, x: int) -> None:
        self.curQueue.append(x)

    def pop(self) -> int:
        if self.empty():
          return None
        
        while len(self.curQueue) > 1:
          self.backUpQueue.append(self.curQueue.popleft())
        
        res = self.curQueue.popleft()
        while self.backUpQueue:
          self.curQueue.append(self.backUpQueue.popleft())
        return res

    def top(self) -> int:
        res = self.pop()
        self.curQueue.append(res)
        return res

    def empty(self) -> bool:
        return len(self.curQueue) <= 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()