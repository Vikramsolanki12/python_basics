list1=[1,2,3,2,1]
copy_list1=list1.copy()
copy_list1.reverse()

list2=[1,"abc","abc",1]
copy_list2=list2.copy()
copy_list2.reverse()

if(copy_list1==list1):
    print("palindrome")
else:
    print("not palindrome")


if(copy_list2==list2):
    print("palindrome")
else:
    print("not palindrome")
