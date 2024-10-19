n=int(input())
target_pay = 1000-n
cnt=0
while(target_pay>=500):
    target_pay=target_pay-500
    cnt+=1
while(target_pay>=100):
    target_pay=target_pay-100
    cnt+=1
while(target_pay>=50):
    target_pay=target_pay-50
    cnt+=1
while(target_pay>=10):
    target_pay=target_pay-10
    cnt+=1
while(target_pay>=5):
    target_pay=target_pay-5
    cnt+=1
while(target_pay>=1):
    target_pay=target_pay-1
    cnt+=1

print(cnt)