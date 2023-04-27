
for row in range(5):
    for col in range(5):
        if (col==0) or (col==4) or (row ==2):
            print("*",end="")
        else:
            print(" ",end="")
    print()

for row in range(5):
    for col in range(5):
        if (col == 0) or (row % 2==0):
           print("*",end="")
        else:
            print(" ",end="")
    print()

