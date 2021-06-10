def star(a):
    for i in range(0,a):
        for j in range(0, i+1):
            print("* ",end="")
        print("\r")
        
print('Enter the number of star rows you need: ')
k=int(input())
star(k)   