import threading 
#import random
import time

unsorted_list = []

#for i in range (50):                                          
#  unsorted_list.append((random.randint(0,100)))  

size = int(input("Enter length of Array and then the Values: "))

for i in range (0, size):
  elements = int(input())
  unsorted_list.append(elements)

print("Unsorted List: \n" + str(unsorted_list) + "\n")

def merge(first_half, second_half):
    i = j = 0
    len_f = len(first_half)
    len_s = len(second_half)

    sorted_list = []

    while i<len_f and j<len_s:
        if first_half[i]<second_half[j]:
            sorted_list.append(first_half[i])
            i+=1
        else:
            sorted_list.append(second_half[j])
            j+=1

    while i<=len_f-1:
        sorted_list.append(first_half[i])
        i += 1
    while j<=len_s-1:
        sorted_list.append(second_half[j])
        j += 1

    return sorted_list

def merge_sort(listx):
    if len(listx) > 1:

        mid = len(listx)//2
        left_side = listx[:mid]
        right_side = listx[mid:]

        x = merge_sort(left_side)
        y = merge_sort(right_side)

        t1 = threading.Thread(target = x)
        t2 = threading.Thread(target = y)

        t1.start()                                                                     
        t2.start()
        time.sleep(1.0)                                       
        t1.join()                                         
        t2.join()

        return merge(x, y)

    return listx

finished_list = merge_sort(unsorted_list)
print("Sorted List Using Multithreaded MergeSort: \n" + str(finished_list))
