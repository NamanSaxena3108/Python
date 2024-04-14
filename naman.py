import array as arr
arr=[]
#for i in range(0,10):
 c=int(input("enter the element to be added:"))
  arr.insert(i,c)
 print ("the elements are", arr)
l=int(input("enter the length of array"))
a=int(input("enter the index to be inserted"))
for i in range(0,l):
    if i==a:
        b=int(input("enter the value to be inserted"))
        arr.insert(a,b)
    else:
        v=int(input("enter the element to be added"))
        arr.insert(i,v)
print("the modified array is ",arr)