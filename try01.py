#find largest value in array


# ar=[3,1,6,7,2]
#
# max=ar[0]
#
# m=len(ar)
#
# for i in range (1,m):
#     if ar[i]>max:
#         max=ar[i]
#
#
# print(max)
#


#check prime or not in given series


# a = int(input("Enter Range"))
#
#
# for i in range(2,a+1):
#     k=0
#
#     for j in range(2,i//2+1):
#         if(i%j==0):
#             k=k+1
#     if(k<=0):
#         print(i)


# Fibonacci of number

# def fact(n):
#     return 1 if (n==0 or n==1) else n*fact(n-1)
#
# num=int(input("enter"))
#
# print("factorial is",fact(num))

#factorial
# def fib(n):
#     return n if (n<=1) else fib(n-1)+fib(n-2)
#
# num=int(input("enter"))
#
# print("factorial is")
#
# for i in range(2,num):
#     print(fib(i))

# Delete nth occurence

# mylist=["kantara","is a GOOD MOVIE","kantara"]
#
# n=2
# count=0
# word= "kantara"
# for i in range(0,len(mylist)):
#     if(mylist[i]==word):
#         count=count+1
#         if(count==n):
#             del mylist[i]
# print("updated new list",mylist)


 # Reverse word in string

a="hey this is safar"

b=a.split(" ")

b= b[-1::-1]

print(b)


sub="safar"

print(a.find(sub))

if(a.find(sub)==-1):
    print("mot found")
else:
    print("found")