from collections import deque

def reverse(q):
    s = len(q)
    ans = deque()
    for i in range(s):
        for j in range(s-1):
            x = q.popleft()
            q.appendleft(x)

        ans.appendleft(q.popleft())
    return ans

q = deque()

q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)

q = reverse(q)

while (len(q) > 0):
    print(q.popleft(), end = " ")
