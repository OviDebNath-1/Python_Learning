# Example of for loop
# for i in range(5,51,5):
#     print(i)
# solved problem-1
# n=int(input("please tell your number: "))
# for i in range(n,n*10+1,n):
#     print(i)
# solved problem-2
# a="students"
# for i in a:
#     print(i)
# solved problem-3
# a="students"
# for i in range(len(a)):
#     print(f"{i} : {a[i]}")
# solved problem-4
# for i in range(1,11):
#     if i==6:
#         break
#     print(i)
# solved problem-5
# for i in range(1,11):
#     if i==4 or i==5 or i==6:
#         continue
#     print(i)
# solved problem-6
# for i in range(1,11):
#     if i==12:
#         break
#     print(i)
# else:
#     print("no break was encountered")
# solved problem-7
# for i in range(1,11):
#     if i==7:
#         break
#     print(i)
# else:
#     print("no break was encountered")
    
# solved problem-8
# n= int(input("please tell your number: "))

# for i in range(n):
#     print("Hello World")
# # solved problem-9
# n= int(input("please tell your number: "))
# for i in range(1,n+1):
#     print(i)
# solved problem-10
# n=int(input("please tell your number: "))
# for i in range (n,0,-1):
#     print(i)
# solved problem-11
# n=int(input("which table you want to print: "))
# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")
# solved problem-12
# n=int(input("please tell your number: "))
# sum=0
# for i in range(1,n+1):
#     sum +=i
#     print(f"the sum of first {i} natural numbers is {sum}")
# solved problem-13
# n=int(input("please tell your number: "))
# sum=0
# for i in range(1,n+1):
#     sum +=i
# print("the sum of first", n, "natural numbers is: ",sum)
# solved problem-14
# n=int(input("please tell your number: "))
# sum=0
# for i in range(n,0,-1):
#     sum +=i
# print("the sum of first", n, "natural numbers is: ",sum)
# solved problem-15
# n=int(input("please tell your number: "))
# fact=1
# for i in range(1,n+1):
#     fact *=i
# print(f"the factorial of {n} is: {fact}")
# solved problem-16
# n=int(input("please tell your number: "))
# odd_sum=0
# even_sum=0
# for i in range(1,n+1):
#     if i%2==0:
#         even_sum +=i
#     else:
#         odd_sum +=i
# print(f"the sum of odd numbers from 1 to {n} is: {odd_sum}")
# print(f"the sum of even numbers from 1 to {n} is: {even_sum}")
# solved problem-17
# n=int(input("please tell your number: "))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)
# print(f"the sum of factors of {n} is: {sum}")

# solved problem-18
# n=int(input("please tell your number: "))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         print(i)
#         sum +=i
# print(f"the sum of factors of {n} is: {sum}")
# if sum==n:
#     print(f"{n} is a perfect number")
# else:
#     print(f"{n} is not a perfect number")
# solved problem-19
# n=int(input("please tell your number: "))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count +=1
# if count==2:
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")
# solved problem-20
# a="python"
# rev=""
# for i in range(len(a)-1,-1,-1):
#     rev += a[i]
# print(rev)
# solved problem-21
# a=input("please tell your string: ")
# rev=""
# for i in range(len(a)-1,-1,-1):
#     rev += a[i]
# print(rev)
# if rev==a:
#     print(f"{a} is a palindrome")
# else:
#     print(f"{a} is not a palindrome")
# solved problem-22
# a="P@#yn26at^&i5ve"
# char=0
# sp_char=0
# digits=0
# for i in a:
#     if (ord(i)>=65 and  ord(i)<=90) or (ord(i)>=97 and  ord(i)<=122):
#         char +=1
#     elif ord(i)>=48 and ord(i)<=57:
#         digits +=1
#     else:
#         sp_char +=1
# print(f"Characters: {char}")
# print(f"Digits: {digits}")
# print(f"Special Characters: {sp_char}")
# or
# a="P@#yn26at^&i5ve"
# char=0
# sp_char=0
# digits=0
# for i in a:
#     if i.isalpha():
#         char +=1
#     elif i.isdigit():
#         digits +=1
#     else:
#         sp_char +=1
# print(f"Characters: {char}")
# print(f"Digits: {digits}")
# print(f"Special Characters: {sp_char}")