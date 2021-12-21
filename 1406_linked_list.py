"""
Linked list로 구현했을 때, 채점이 되다가 시간 초과 판정을 받느 것으로 보아(+ 백준 예시 case는 모두 정답 확인), 
코드에 오류는 없으나 O(N) 의 time comlexity로 실패 판정
"""

# Node class 선언
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly linked list class 선언
class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0
    
    # Return the length of linked list
    def length(self):
      if self.head == None:
        return -1
      else:
        cur = self.head
        cur_i = 0
        while cur.next != None:
          cur = cur.next
          cur_i += 1
        return cur_i + 1

    # Add new node at the end of the linked list
    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    # Return first index of data in the linked list
    def getdataIndex(self, data):
        curn = self.head
        idx = 0
        while curn:
            if curn.data == data:
                return idx
            curn = curn.next
            idx += 1
        return -1

    # Add new node at the given index
    def insertNodeAtIndex(self, idx, node):
        """
    A node can be added in three ways
    1) At the front of the linked list
    2) At a given index
    3)At the end of the linked list
    """
        curn = self.head
        prevn = None
        cur_i = 0

        # 1) Add 0 index
        if idx == 0:
            if self.head:
                nextn = self.head
                self.head = node
                self.head.next = nextn
            else:
                self.head = node
        else:
            # 2) Add at given index
            # 3) At the end of the linked list
            while cur_i < idx:
                if curn:
                    prevn = curn
                    curn = curn.next
                else:
                    break
                cur_i += 1
            if cur_i == idx:
                node.next = curn
                prevn.next = node
            else:
                return -1

    # Add new node before the given deta
    def insertNodeAtData(self, data, node):
        index = self.getdataIndex(data)
        if 0 <= index:
            self.insertNodeAtIndex(index, node)
        else:
            return -1


    # Delete data at given index
    def deleteAtIndex(self, idx):
      curn_i = 0
      curn = self.head
      prevn = None
      nextn = self.head.next
      if idx == 0:
          self.head = nextn
      else:
          while curn_i < idx:
              if curn.next:
                  prevn = curn
                  curn = nextn
                  nextn = nextn.next
              else:
                  break
              curn_i += 1
          if curn_i == idx:
              prevn.next = nextn
          else:
              return -1

    # Empty linked list
    def clear(self):
        self.head = None

    # 출력
    def print(self):
        curn = self.head
        string = ""
        while curn:
            string += str(curn.data)
            # if curn.next:
            #     string += "->"
            curn = curn.next
        print(string)

if __name__ == "__main__":
  sl_input= input()
  sl = SinglyLinkedList()
  for i in range(len(sl_input)):
    sl.append(Node(sl_input[i]))

  idx = len(sl_input)
  order_num = int(input())
  for _ in range(order_num):
    order_str = input()
    if order_str[0] == "L":
      if idx != 0: idx -= 1
    elif order_str[0] == "D":
      if idx != sl.length(): idx += 1
    elif order_str[0] == "B":
      if idx != 0:
        sl.deleteAtIndex(idx-1)
        idx -= 1
    elif order_str[0] == "P":
      sl.insertNodeAtIndex(idx, Node(order_str[2]))
      idx += 1
    # print()
    # sl.print()
    # print("index:", str(idx))
    

  sl.print()
