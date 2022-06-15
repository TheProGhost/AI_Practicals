# pyramid pattern

num = int(input("Enter the deapth of pyramid: "))



for i in range(num):
    print("  "*(num-i),end="  ")
    n = 1
    tmp = 2*i+1
    for j in range(tmp):
        # print(" *",end="")
        if (i == 0 or j == 0):
            print(" 1",end="")
        elif(j<i):
            n+=1
            print(f" {n}",end="")
        elif(i == j):
            n+=1
            print(f" {n}",end="")
        else:
            n-=1
            print(f" {n}",end="")
           
    print()