bin = list(input())
bin = bin[::-1]
n = 3

arr = [bin[i*n:(i+1)*n] for i in range((len(bin) + n - 1) // n)]
arr = arr[::-1]

ans = []
for segment in arr:
    decimal_value = 0
    for j in range(len(segment)):
        decimal_value += int(segment[j]) * (2 ** j)
    ans.append(str(decimal_value))

ans_ = ''.join(ans)
print(ans_)
