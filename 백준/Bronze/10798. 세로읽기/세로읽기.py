arr=[input().strip() for i in range(5)]
lene = [len(word) for word in arr]

ans=[]
max_len = max(lene)
for i in range(max_len):
    for j in range(5):
        if i < lene[j]:
            ans.append(arr[j][i])
print("".join(ans))