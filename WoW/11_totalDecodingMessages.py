#Author	:	Bhavya Singh
#Date	:	24-May-2020
#Name	:	Total Decoding Messages


#PROBLEM:

A top secret message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
You are an FBI agent. You have to determine the total number of ways that message can be decoded.
Note: An empty digit sequence is considered to have one decoding. It may be assumed that the input contains valid digits from 0 to 9 and If there are leading 0’s, extra trailing 0’s and two or more consecutive 0’s then it is an invalid string.

Example :
Given encoded message "123",  it could be decoded as "ABC" (1 2 3) or "LC" (12 3) or "AW"(1 23).
So total ways are 3.

Input:
First line contains the test cases T.  1<=T<=1000
Each test case have two lines
First is length of string N.  1<=N<=40
Second line is string S of digits from '0' to '9' of N length.

Example:
Input:
2
3
123
4
2563
Output:
3
2

#CODE

def decode(data, n):
    if n==0:
        return 1
    s = len(data) - n
    if data[s] == '0':
        return 0
    result = decode(data, n-1)
    if n>=2 and int(data[s:s+2])<=26:
        result += decode(data, n-2)
    return result
    
    
T = int(input())
for test in range(T):
    N = int(input())
    inp = input()
    print( decode(inp, N) )