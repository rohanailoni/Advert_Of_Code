
hos=0;
dep=0;
while True:
    line=input();
    if line=='':
        break
    command,pos=line.split(" ")
    if command=="forward":
        hos+=int(pos)
    elif command=="down":
        dep+=int(pos)
    elif command=="up":
        dep-=int(pos)
print(hos*dep)
