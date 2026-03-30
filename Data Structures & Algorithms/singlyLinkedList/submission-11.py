class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def get(self, index: int) -> int:
        if index >= self.size or index <0:
            return -1

        tmp = self.head
        i = 0
        while tmp and i<=index:
            if i == index:
                return tmp.val
            else:
                tmp = tmp.next
                i += 1
        return -1

    def insertHead(self, val: int) -> None:
        n = Node(val)
        n.next = self.head
        self.head = n
        self.size +=1

    def insertTail(self, val: int) -> None:
        n = Node(val)
        if not self.head:
            self.head = n
            self.size +=1
        else:
            tmp = self.head
            while tmp.next:
                tmp = tmp.next
            tmp.next = n
            self.size +=1

    def remove(self, index: int) -> bool:
        if index >= self.size or index <0 or self.size == 0:
            return False
        if index == 0 and self.size >= 1:
            self.head = self.head.next
            self.size -= 1
            return True
        else:
            tmp = self.head
            prev = None
            i = 0
            while tmp and i < index:
                prev = tmp
                tmp = tmp.next
                i +=1
            if tmp:
                prev.next = tmp.next
            self.size -= 1
            return True

    def getValues(self) -> List[int]:
        arr = []
        tmp = self.head
        while tmp:
            arr.append(tmp.val)
            tmp = tmp.next
        return arr
    