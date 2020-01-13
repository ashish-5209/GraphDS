from queue import deque
def stepnum(n, m):
        ans = [0]
        Q = deque()
        i = 1
        while i<=9:
            Q.append(i)
            while Q:
                val = Q.popleft()
                if n<=val<=m:
                    ans.append(val)
                d = val%10
                if d - 1 >= 0 and (val*10 + d - 1)<=m:
                    Q.append(val*10 + val%10 - 1)
                if d + 1 < 10 and (val*10 + d + 1)<=m:
                    Q.append(val*10 + val%10 + 1)
            i+=1
        ans.sort()
        return ans[1:]
print(stepnum(10, 20))
