#Author	:	Bhavya Singh
#Date	:	30-May-2020
#Name	:	Lcuky Number

#PROBLEM:

You are given two numbers L and R. You are required to find the total number of lucky numbers present in between L and R(inclusive).

Note: A number is said to be lucky if the factors of that number are not repeated (power to the factors can only be 1).

Input format:

The first line of the input contains an integer T denoting the number of test cases.
Each test case is described by a line containing two space - separated integers L and R
Output format:

Print the answer for each test case in a new line.

Sample Input:

1
2 4
Sample output:

2
Explanation:

In the sample case, 2 and 3 are prime itself and so are lucky numbers, Prime factorization of 4 is 22 and since 2 is repeated it is not a lucky number. So the number of lucky numbers is 2.

#CODE

def islucky(n):
    for i in range(2,n):
        if(n%(i*i)==0):
            return 0
    return 1

tc=int(input())
for i in range(tc):
    l,r=list(map(int,input().split()))
    lucky_count=0
    for i in range(l,r+1):
        lucky_count+=islucky(i)
    print(lucky_count)