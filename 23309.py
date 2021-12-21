# 23309 철도 공사
# Python으로 구현하여 시간 초과 판정 받았으나 제시된 예시 정답에는 지장 없음을 확인하였다.


class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

class SinglyLinkedList(object):
  def __init__(self):
    self.head = None

  def length(self):
      if self.head == None:
        return 0
      else:
        curn = self.head
        cur_i = 0
        while curn.next:
          curn = curn.next
          cur_i += 1
        return cur_i + 1

  def append(self, node):
    if self.head == None:
      self.head = node
    else:
      curn = self.head
      while curn.next:
        curn = curn.next
      curn.next = node

  def getdataIndex(self, data):
    curn = self.head
    idx = 0
    while curn:
      if curn.data == data:
        return idx
      curn = curn.next
      idx += 1
    return -1

  def insertNodeAtIndex(self, idx, node):
    curn = self.head
    prevn = None
    cur_i= 0

    if idx == 0:
      if self.head:
        nextn = self.head
        self.head = node
        node.next = nextn
      else:
        self.head = node

    else:
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

  def insertNodeAtData(self, data, node):
    index = self.getdataIndex(data)
    if 0 <= index:
      self.insertNodeAtIndex(index,node)
    else:
      return -1

  def deleteAtIndex(self, idx):
    cur_i = 0
    prevn = None
    curn = self.head
    nextn = self.head.next
    if idx == 0:
      self.head = nextn
    else:
      while cur_i < idx:
        if curn.next:
          prevn = curn
          curn = nextn
          nextn = nextn.next
        else:
          break
        cur_i += 1
      if cur_i == idx:
        prevn.next = nextn
      else:
        return -1
    
  def clear(self):
    self.head = None
  
  def print(self, idx):
    curn = self.head
    cur_i = 0
    while cur_i < idx:
      curn = curn.next
      cur_i += 1
    print(curn.data)

if __name__ == "__main__":

  import sys
  input = sys.stdin.readline

  n,m = map(int, input().strip().split())
  sl_input= input().strip().split()
  sl = SinglyLinkedList()
  for i in range(len(sl_input)):
    sl.append(Node(sl_input[i]))

  for i in range(m):
    com = list(input().strip().split())
    if com[0] == "BN":
      idx = sl.getdataIndex(com[1])
      next_idx = (idx + 1) % sl.length()
      sl.print(next_idx)
      sl.insertNodeAtIndex(next_idx, Node(com[2]))
    elif com[0] == "BP":
      idx = sl.getdataIndex(com[1])
      if idx != 0:
        prev_idx = (idx - 1) % sl.length()
      else:
        prev_idx = sl.length() - 1
      sl.print(prev_idx)
      sl.insertNodeAtIndex(idx, Node(com[2]))
    elif com[0] == "CN":
      idx = sl.getdataIndex(com[1])
      next_idx = (idx + 1) % sl.length()
      sl.print(next_idx)
      sl.deleteAtIndex(next_idx)
    elif com[0] == "CP":
      idx = sl.getdataIndex(com[1])
      if idx != 0:
        prev_idx = (idx - 1) % sl.length()
      else:
        prev_idx = sl.length() - 1
      sl.print(prev_idx)
      sl.deleteAtIndex(prev_idx)
