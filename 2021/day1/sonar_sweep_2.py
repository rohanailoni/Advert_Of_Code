arr=[]
while True:
    line = input()
    if line == '':
        break
    arr.append(int(line))

basesum=arr[0]+arr[1]+arr[2]
ans=0
ch=0
for i in range(3,len(arr)):
    ss=basesum-arr[ch]+arr[i]
    # print(ss,basesum,arr[ch],arr[i],ch)
    ch+=1
    if basesum<ss:
        ans+=1
    basesum=ss
print(ans)
