#3d lists are basically a list inside of a list inside of a list

threeDlist = [
    [ [1.0, 1.5], [2.0, 2.5], [3.0, 3.5] ], # array inside of an array inside of an array
    [ [4.0, 4.5], [5.0, 5.5], [6.0, 6.5] ] #second first array
]
#To find a certain item in the list you use 3 digits like so:
print(threeDlist [0][2][1]) # this prints out the number from the first line of array in the 3rd array inside that and then finally the second number ion that final array

#this loop can be used to print out the entire list
for i in threeDlist:
    print(i)

#to append to a specific list inside of the 3d list you must index it first
threeDlist[0][2].append(4.0) #make sure you ponly add 2 indexes as you must ad it to the list not the object inside the list so you opnly go 2 lists deep
print(threeDlist)

threeDlist[0][2].remove(4.0)#removes the number from the list, using the same method as appending would
#to append a new list to the 3D list you can do
threeDlist.append([[10,12], [13,15], [16,17]])
print(threeDlist)