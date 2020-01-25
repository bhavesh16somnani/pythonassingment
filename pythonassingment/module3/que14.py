c=int(input("enter the no of rows"))
for i in range(1,c+1):
    print(" "*(c-i),"*"*(i*2-1))
for i in range(c-1,0,-1):
    print(" "*(c-i),"*"*(i*2-1))