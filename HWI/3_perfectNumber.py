#Author	:	Bhavya Singh
#Date	:	29-May-2020
#Name	:	Perfect Number

#THEORY:

A number is a perfect number if is equal to sum of its proper divisors, that is, sum of its positive divisors excluding the number itself. Write a function to check if a given number is perfect or not.

A Simple Solution is to go through every number from 1 to n-1 and check if it is a divisor. Maintain sum of all divisors. If sum becomes equal to n, then return true, else return false.

An Efficient Solution is to go through numbers till square root of n. If a number ‘i’ divides n, then add both ‘i’ and n/i to sum.

#PROBLEM:

Given a number N, check if a number is perfect or not. A number is said to be perfect if sum of all its factors excluding the number itself is equal to the number.

Input:
First line consists of T test cases. Then T test cases follow .Each test case consists of a number N.

Output:
For each testcase, in a new line, output in a single line 1 if a number is a perfect number else print 0.

Constraints:
1 <= T <= 300
1 <= N <= 1018

Example:
Input:
2
6
21
Output:
1
0

#CODE

def isPerfect(n):
    Sum = 1
    i = 2
    while i * i <= n: 
        if n % i == 0: 
            if i*i != n:
                Sum += i + n/i
            else:
                Sum += i
        i += 1
    if Sum == n:
        return True
    else:
        return False

T = int(input())
for test in range(T):
    N = int(input())
    result = isPerfect(N)
    if result:
        print("1")
    else:
        print("0")