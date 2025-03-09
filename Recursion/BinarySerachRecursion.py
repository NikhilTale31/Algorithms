//RECURSIVE APPROACH FOR BINARY SEARCH
def Binary_search(A,key,low,high):
    if low > high:
        print("Not Present")
    else:
        m = (low+high)//2
        if key == A[m]:
            print("Element is Present at index",m)
        elif key < A[m]:
            return Binary_search(A,key,low,m-1)
        else:
            return Binary_search(A,key,m+1,high)


A = []
while(1):
    print("\n1.Insert\t2.Search\t3.Exit\t4.Dispaly\n")
    ch = int(input("Entre Choice"))
    if ch == 3:
        break
    elif ch ==1:
        n = int(input("Entre Number in ASSENDING ORDER"))
        A.append(n)

    elif ch ==2:
        search = int(input("Enter Number to be searched"))
        Binary_search(A,search,0,len(A))

    elif ch == 4:
        for i in range(0,len(A)):
            print(A[i],end=" ")

    else:
        print("Invalid Option")
