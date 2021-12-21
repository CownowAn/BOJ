# 5397 키로거
import sys
input = sys.stdin.readline
for _ in range(int(input().strip())):
  s1=[]
  s2=[]
  com = input().strip()
  for i in range(len(com)):
    if com[i] == "<" and s1 != []:
      s2.append(s1.pop())
    elif com[i] == ">" and s2 != []:
      s1.append(s2.pop())
    elif com[i].isalpha() or com[i].isdigit():
      s1.append(com[i])
    elif com[i] == "-" and s1 != []:
      s1.pop()

  print("".join(s1+list(reversed(s2))))
