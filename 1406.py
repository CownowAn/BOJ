# 1406 에디터
# 2개의 스택을 이용하여 구현한다. 커서를 기준으로 문자열을 담는 스택이 2개로 나뉘어져 있다고 생각하면 된다.
import sys
input = sys.stdin.readline

s1 = list(input().strip())
s2 = []
m = int(input())
n = len(s1)

for i in range(m):
  com = input().strip()
  if com[0] == "P":
    s1.append(com[2])
  elif com[0] == "L" and s1 != []:
    s2.append(s1.pop())
  elif com[0] == "D" and s2 != []:
    s1.append(s2.pop())
  elif com[0] == "B" and s1 != []:
    s1.pop()

print("".join(s1 + list(reversed(s2))))
