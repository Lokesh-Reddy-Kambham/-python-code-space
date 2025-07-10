 
"""1.Positive or Negative Number"""

# num = int(input("Enter Number:"))
# print("+VE Number" if num>=0 else "-VE Number")

'''2.Even or Odd Number'''

# num = int(input("Enter Number:"))
# print("EVEN Number" if num%2==0 else "ODD Number")

'''3.Sum of first N natural Numbers'''

# num = int(input("Enter Number:"))
# result = sum(range(0,num+1))
# print(f"Sum of  first {num} Natural Numbers: {result}")

'''4.Greatest of 2 numbers'''

# num1 = int(input("Enter Number:"))
# num2 = int(input("Enter Number:"))
# print("Greatest Number is:",max(num1,num2))

'''5.Greatest of 3 numbers'''

# num1 = int(input("Enter Number:"))
# num2 = int(input("Enter Number:"))
# num3 = int(input("Enter Number:"))
# print("Greatest Number is:",max(num1,num2,num3))

'''6.Leap year or not'''

# def isLeapYear(year:int):
#     if (year%400==0) or (year%4==0 and not year%100==0):
#         return "Leap Year"
#     else:
#         return "Not a Leap Year"
# year = int(input("Enter Year:"))
# print(isLeapYear(year))

'''7.Prime Number or not'''

# def isPrime(number:int):
#     if number<=1:
#         return False
#     for i in range(2,int(number**0.5)+1):
#         if number%i==0:
#             return False
#     return True
#
# value = int(input("Enter Number:"))
# print(isPrime(value))

'''8.Prime numbers within a given range'''

# def primeList(num1:int,num2:int):
#     prime = []
#     for i in range(num1,num2+1):
#         for j in range(2,int(i**0.5)+1):
#             if i%j==0:
#                 break
#         else:
#             prime.append(i)
#     return prime
#
# num1 = int(input("Enter Number:"))
# num2 = int(input("Enter Number:"))
# print(primeList(num1,num2))

'''9.Sum of digits of a number'''

# num = int(input("Enter Number:"))
# remainder = 0
# digitSum = 0
# while num>0:
#     remainder = num%10
#     digitSum += remainder
#     num = num//10
# print(digitSum)

'''10.1 Reverse a Number'''

# num = int(input("Enter Number:"))
# remainder = 0
# reverse = str()
# while num>0:
#     remainder = num%10
#     num = num//10
#     reverse += str(remainder)
# print(reverse)

'''10.2 Reverse a Number'''

# num = int(input("Enter Number:"))
# reverse = 0
# while num > 0:
#     remainder = num % 10
#     reverse = (reverse * 10) + remainder
#     num = num // 10
# print(reverse)

'''11.Palindrome Number'''

# num = int(input("Enter  Number:"))
# original = num
# reverse = 0
# while num > 0:
#     remainder = num % 10
#     reverse = (reverse * 10) + remainder
#     num = num // 10
# print("It's Palindrome number" if original == reverse else  "it's not a palindrome")

'''12.1 Armstrong Number'''

# num = int(input("Enter a number: "))
# result = sum(int(digit)**len(str(num)) for digit in str(num))
# print("Armstrong" if num==result else "Not Armstrong")

'''12.2 Armstrong number'''

# num = int(input("Enter Number:"))
# original = num
# power = len(str(num))
# result = 0
# while num>0:
#     remainder = num % 10
#     num = num // 10
#     result += remainder ** power
# print(result)
# print("Armstrong" if original ==result else "Not Armstrong")

'''13.1.Armstrong number in a given range '''

# num1 = int(input("Enter First Range:"))
# num2 = int(input("Enter Second Range:"))
# armstrong_series = []
# for i in range(num1,num2+1):
#     armstrong = sum(int(digit)**len(str(i)) for digit in str(i))
#     if armstrong == i:
#         armstrong_series.append(i)
# print(f"Armstrong Series from {num1} to {num2}:",armstrong_series)

'''13.2. Armstrong number in a given range '''

# num1 = int(input("Enter First Range:"))
# num2 = int(input("Enter Second Range:"))
# armstrong_series = [i for i in range(num1,num2)
#                     if i == sum(int(digit)**len(str(i)) for digit in str(i))]
# print(f"Armstrong Series from {num1} to {num2}:",armstrong_series)

'''14.Fibonacci Series upto nth term'''

# num = int(input("Enter Number Range :"))
# n1 , n2 = 0,1
# for i in range(num+1):
#     print(n1,end=" ")
#     n1 ,n2 = n2 ,(n1+n2)

'''15.Find the Nth Term of the Fibonacci Series'''

# nth = int(input("Enter Nth term :"))
# n1,n2 = 0,1
# fibonacci_series = []
# for i in range(nth+1):
#     fibonacci_series.append(n1)
#     n1 ,n2 = n2 ,(n1+n2)
# print(fibonacci_series[nth])

'''16.Factorial of a number'''

# def factorial(number:int):
#     fact = 1
#     for i in range(1,number+1):
#         fact *= i
#     return fact
# num = int(input("Enter Number:"))
# print(factorial(num))

'''17.Power of a number'''

# num1 = int(input("Enter base value:"))
# num2 = int(input("Enter power value:"))
# print(num1**num2)

'''18.Factors of a number '''

# num = int(input("Enter Number:"))

# def factors(number:int):
#     factorlist= [factor for factor in range(1,num+1) if num%factor==0]
#     return factorlist
# print(f"factors of a {num}:",factors(num))

'''19.Finding Prime Factors of a number'''

# num = int(input("Enter Number:"))
#
# def isPrime(number:int):
#     if number<=1:
#         return False
#     for i in range(2,int(number**0.5)+1):
#         if number%i==0:
#             return False
#     return True
#
# primeFactorList = [factor for factor in range(1,num+1) if num%factor==0 and isPrime(factor)]
# print(f"prime factors of a {num}:",primeFactorList)

'''20.Strong number'''

# num = int(input("Enter Number:"))
#
# def factorial(number:int):
#     fact: int = 1
#     for i in range(1,number+1):
#         fact *= i
#     return fact
# result = sum(factorial(int(digit)) for digit in str(num))
# print("Strong Number" if num == result else "Not a strong Number" )

'''21.Perfect number'''

# num = int(input("Enter Number:"))
# result = sum(factor for factor in range(1,num) if num%factor==0)
# print("Perfect Number" if num == result else "Not a Perfect number")

'''22.Perfect Square '''

# num = int(input("Enter Number:"))
# sqrt = int(num**0.5)
# print("Perfect Square" if sqrt**2 == num else "Not Perfect Square")

'''23.Automorphic number '''
# num = int(input("Enter Number:"))
# def square(number:int):
#     return number**2
# print("AutoMorphic" if str(square(num)).endswith(str(num)) else 'Non AutoMorphic')

'''23.2 AutoMorphic Number'''

num = int(input("Enter Number:"))
square = num * num
temp = num
while temp > 0:
    if square % 10 != temp % 10:
        print("Non AutoMorphic")
        break
    square //= 10
    temp //= 10
else:
    print("AutoMorphic")

'''24.Harshad number'''
#
# num = int(input("Enter Number:"))
# def digitSum(number:int):
#     remainder = 0
#     sum = 0
#     while num>0:
#         remainder = num%10
#         sum += remainder
#         num = num//10
#         return digitSum




