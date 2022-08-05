
hos=0;
dep=0;
aim=0;
while True:
    line=input();
    if line=='':
        break
    command,pos=line.split(" ")
    if command=="forward":
        hos+=int(pos)
        dep+=aim*int(pos)
    elif command=="down":
        aim+=int(pos)
    elif command=="up":
        aim-=int(pos)
print(hos*dep)

