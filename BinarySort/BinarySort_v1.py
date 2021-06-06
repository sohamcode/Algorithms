#li = [5,4,3,2,1,10,9,8,7,6]
#li = [10,30, 21, 54, 2,1]
#li = [71, 6, 35, 24, 61, 82, 27, 1, 17, 83]
li = [7,3,10,2,5,4,6,8,12]
##li = [3, 100, 47, 5, 13, 76, 44, 61, 15, 28,
##      77, 56, 33, 45, 31, 58, 11, 8, 90, 16,
##      78, 57, 84, 87, 24, 27, 55, 97, 1, 94,
##      88, 37, 46, 6, 51, 49, 10, 98, 7, 38,
##      39, 42, 99, 12, 23, 26, 66, 20, 54, 41]

# Below two list stores the location of an entry in the list greater or smaller than the value at current location.
li_left = [-1]*len(li)
li_right = [-1]*len(li)

#Below function recursively creates the Sorted Binary Tree
def insert(x, curr_loc, parrent_loc):
    if x < li[parrent_loc]: # Check if the 
        if li_left[parrent_loc] == -1:
            li_left[parrent_loc] = curr_loc
        else:
            insert(x, curr_loc, li_left[parrent_loc]) # Recursion
    else:
        if li_right[parrent_loc] == -1:
            li_right[parrent_loc] = curr_loc
        else:
            insert(x, curr_loc, li_right[parrent_loc]) # Recursion

# Below function prints the Binary tree in sorted format
def pop(cur_loc):
    # Below flag will turn false when the current node is printed.
    printFlag = True
    
    # Check if left child is present
    if li_left[cur_loc] > -1:
        pop(li_left[cur_loc])
        if printFlag:
            printFlag = False
            print(li[cur_loc], end=", ")
    elif li_left[cur_loc] == -1:
        if printFlag:
            printFlag = False
            print(li[cur_loc], end=", ")
    
    # check if right child is present
    if li_right[cur_loc] > -1:
        if printFlag:
            printFlag = False
            print(li[cur_loc], end=", ")
        pop(li_right[cur_loc])

# Below loop creates the binary tree of the list.
# NOTE: It starts from 2nd entry in the list as 1st entry forms the parent of complete binary tree.
for i in range(1,len(li)):
    insert(li[i], i, 0)

#print(li_left)
#print(li_right)

print ('Before :', li)
print ('After Sorting : ', end=" ")
pop(0)
