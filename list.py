
# kuch bhi mix kar sakte hain
ex = [10 , "loji" , True]
print(ex[2])
marks = [2 , 13 , 45]
# 0 based indexing
print(marks[0])
# we can use negetive index too bss -1 se chalu karo 
# -i = n - i 
print(marks[-1])
# print range
print(marks[1:3])  #this means 1th index se 2th index tak include karenge
# 3 not included

# to print all elements
for score in marks :
    print(score)

marks.append(99) # to insert new element in list at last
marks.insert(0 , 77) # to insert new element in last at preferred index

print(77 in marks) # true if 77 is present in marks
print(len(marks)) # number of elements in list marks
marks.clear() # sari ki sari list khali hojayegi

