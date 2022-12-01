arr=[]
while True:
    line = input()
    if line == '':
        break
    arr.append(int(line))


base=arr[0];
ans=0
for i in range(1,len(arr)):
    if arr[i]>base:
        ans+=1;
    base=arr[i]
print(ans)
