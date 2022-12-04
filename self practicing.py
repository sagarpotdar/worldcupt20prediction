# #palindrome
#
# def palind(n):
#
#     return n == n[::-1]
#
# n="sagas"
#
# ans=palind(n)
#
# if ans:
#     print("yes")
# else:
#     print("no")



#LARGEST  element

# array_try=[2,5,7,4,1,67]
#
# maximum = array_try[0]
#
# m=len(array_try)
#
# for i in range (1,m):
#
#     if(array_try[i]>maximum):
#
#
#         maximum=array_try[i]
#
# print(maximum)


# factorial

# def fact(n):
#     if (n==0 or n ==1):
#         return 1
#     else:
#         return n*fact(n-1)
#
#
# n=int(input("Enter number"))
#
# print("fact of number is", fact(n))

# fibonacci
def fact(n):
    if (n<=1):
        return n
    else:
        return fact(n-1)+fact(n-2)


n=int(input("Enter number"))

print("fact of number is")

for i in range(n):
    print(fact(i))
