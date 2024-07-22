t=int(input())


for i in range(t):
    n=int(input())
    arr=[]
    index = 0

    while n>0:
        arr.append(n%2)
        n//=2
    for i in range(len(arr)):
        if(arr[i]==1):
            print(i, end=" ")
    print()