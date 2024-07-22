n,m=map(int,input().split())
mx1=[list(map(int,input().split())) for i in range(n)]
mx2=[list(map(int,input().split())) for i in range(n)]

arr= [[0 for i in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        arr[i][j]=mx1[i][j]+mx2[i][j]

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()
