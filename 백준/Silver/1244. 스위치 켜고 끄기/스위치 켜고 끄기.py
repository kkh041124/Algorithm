def male(n, num, arr):
    for i in range(num-1, n, num):
        arr[i] = 1 - arr[i]
    return arr
def female(n,num,arr):
    arr[num] = 1 - arr[num]
    for i in range(1,n):
        if num + i < n and num - i >= 0 and arr[num + i] == arr[num - i]:
            arr[num+i]=1-arr[num+i]
            arr[num-i]=1-arr[num-i]
        else:
            break
    return arr
n=int(input())
arr=list(map(int,input().split(" ")))
k=int(input())
std=[list(map(int,input().split(" "))) for i in range(k)]
# arr=male(n,std[0][1],arr)

for g, num in std:
    if g==1:
        arr=male(n,num,arr)
    else:
        arr=female(n,num-1,arr)
for i in range(n):
    print(arr[i], end=" ")
    if (i + 1) % 20 == 0:
        print()
if n % 20 != 0:
    print()