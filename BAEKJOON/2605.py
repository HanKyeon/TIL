'''
줄 세우기

1번 학생은 0을 받는다.
이후 0을 받으면 그대로
Truthy 값을 받으면 그 값만큼 앞으로.
'''
# 입력
n = int(input())
nl = [0] + list(map(int, input().split()))
# 
g = list(range(n+1))
s = list(range(n+1))
for i in range(1, n+1) :
    s = s[:i-nl[i]] + [i] + s[i-nl[i]:i]
s.remove(0)
print(*s)
