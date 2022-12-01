count=False
while True:
    line=input();
    if line=='':
        break;
    if count==False:
        count=True
        arr_1=[0]*len(line)
        arr_0=[0]*len(line)
    for i in range(len(line)):
        if line[i]=="1":
            arr_1[i]+=1
        else:
            arr_0[i]+=1
epsilon=""
gamme=""
for i in range(len(arr_0)):
    if arr_0[i]>arr_1[i]:
        gamme+="0"
        epsilon+="1"
    else:
        gamme+="1"
        epsilon+="0"

print(int(epsilon,2)*int(gamme,2));
