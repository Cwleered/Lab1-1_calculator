def bubbleSort(list):
    n=len(list)

    for i in range(n): #n-1번 반복

        for j in range(0,n-i-1):

            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]

list=[64,34,25,12,22,11,90]

print("original list=%s" %list)

bubbleSort(list)

print("Sorted by bubbleSort")
print(list)