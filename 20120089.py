import sys

chk = [0 for i in range(0,1001)]
ans = []

def DFS(here):
    
    global chk
    global ans
    
    chk[here] = 1
    ans.append(here)
    
    for i in range(0,len(d[here])):
        there = d[here][i]
        if chk[there] == 0: DFS(there)

def BFS(here):

    global chk
    global ans
    
    front = 0
    rear = -1

    q = []

    q.append(here)
    chk[here] = 1
    
    while front > rear:

        rear = rear + 1
        get = q[rear]
        
        ans.append(get)
        
        for there in d[get]:
            
            if chk[there] == 0:
                front = front + 1
                chk[there] = 1
                q.append(there)

    for i in ans:
        sys.stdout.write(str(i))
        sys.stdout.write(" ")
            
N,M,V = map(int,input().split())

d = [[] for i in range(0,1001)]

for i in range(0,M):
    A,B = map(int,input().split())
    d[A].append(B)
    d[B].append(A)
    
for i in range(1,N+1): d[i].sort()

DFS(V)
for i in ans:
    sys.stdout.write(str(i))
    sys.stdout.write(" ")

sys.stdout.write("\n")

ans = []
chk = [0 for i in range(0,1001)]

BFS(V)
