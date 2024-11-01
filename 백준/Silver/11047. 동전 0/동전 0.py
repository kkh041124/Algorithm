import sys 
input = sys.stdin.readline

n,k=map(int,input().split())
arr=[int(input()) for i in range(n)]
arr.sort(reverse=True)
weight = k
cnt=0
while weight > 0 and len(arr) > 0:
    if weight < arr[0]:
        del arr[0]
    else:
        weight-=arr[0]
        cnt+=1

print(cnt)