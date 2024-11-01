# arr에 입력을 받으면 sort함 
# arr에서 가장 먼저 실행되는 작업 넣음 -> 그 뒤에 수행될 수 있는 작업들 append
# 수행된 작업들은 삭제
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[1], x[0]))

end= 0
cnt=0

for i,j in arr:
    if i>=end:
        cnt+=1
        end=j
print(cnt)