def bubblesort(a,n):

    for i in range(0,n-1):
        flag =0


        for j in range(0,n-1-i):
            if a[j] > a[j+1]:
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t
                flag = 1

        if flag == 0:
            break

a = [2,5,7,77,34,-7,0]
n=len(a)
bubblesort(a,n)
print(a)
