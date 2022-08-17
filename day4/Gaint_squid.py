input="""\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
2  0 12  3  7
"""
class Board:
    
    def __init__(self,arr) -> None:
        self.left={}
        self.ints=[]
        
        for i in arr:
            
            self.left[i]=True
        
        self.ints=arr;
    def __str__(self) -> str:
        return 'left{} and ints {}'.format(self.left,self.ints)
    def haswon(self) -> bool:
        for i in range(5):
            for j in range(5):
                if self.ints[i*5+j] in self.left:
                    break
            else:
                return True
            for j in range(5):
                if self.ints[i+5*j] in self.left:
                    break
            else:
                return True
        return False
    def check(self,i)->None:
        if self.left.get(i)!=None:
            self.left.pop(i)
            return None
        return None
        
def parse(l):
    return list(map(int,l.split()))


first,*rest=input.split('\n\n')

whole=[]

for i in rest:
    temp=parse(i)
    
    whole.append(Board(temp))
    

first=list(map(int,first.split(",")))
check=False
for i in first:
    for j in whole:
        j.check(i)
        if j.haswon():
            ans=0
            #print(j.left)
            for k in j.left:
                ans+=k
            print(ans*i)
            check=True
            break
    if check:
        break     