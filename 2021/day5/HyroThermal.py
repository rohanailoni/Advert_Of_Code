input='''\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
'''
class Node:
    def __init__(self,a,b) -> None:
        temp=a.split(",")
        self.startx=int(temp[0])
        self.starty=int(temp[1])
        temp=b.split(",")
        self.endx=int(temp[0])
        self.endy=int(temp[1])
    def __str__(self) -> str:
        return f'start-co {self.startx},{self.starty} and end-co {self.endx},{self.endy}'
    def max_all(self)-> int:
        return max(max(self.endx,self.endy),max(self.startx,self.starty))
all=[]
max_ele=-1
for i in input.split("\n"):
    if i!='':
        a,b=i.split("->")
        temp=Node(a,b)
        all.append(temp)
        max_ele=max(max_ele,temp.max_all())
max_ele+=1
board= [[0 for i in range(max_ele)] for i in range(max_ele)]

for i in all:
    
    if i.startx==i.endx:
        
        if i.starty>i.endy:
            for j in range(i.endy,i.starty+1):
                
                
                board[i.startx][j]+=1
                
            
        elif i.starty<i.endy:
            for j in range(i.starty,i.endy+1):
                board[i.startx][j]+=1

    elif i.starty==i.endy:
        
        if i.startx >i.endx:
            for j in range(i.endx,i.startx+1):
                board[j][i.starty]+=1
        if i.startx < i.endx:
            for j in range(i.startx,i.endx+1):
                board[j][i.starty]+=1
    

ans=0    
for i in range(max_ele):
    for j in range(max_ele):
        if board[i][j]>=2:
            ans+=1

print(ans)
