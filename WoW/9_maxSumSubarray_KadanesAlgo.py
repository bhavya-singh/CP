#Author	:	Bhavya Singh
#Date	:	24-May-2020
#Name	:	Maximum Sum Subarray / Kadane's Algorithm


#PROBLEM:

Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print the maximum sum of the contiguous sub-array in a separate line for each test case.

Constraints:
1 = T = 110
1 = N = 106
-107 = A[i] <= 107

Example:
Input
2
5
1 2 3 -2 5
4
-1 -2 -3 -4
Output
9
-1

Explanation:
Testcase 1: Max subarray sum is 9 of elements (1, 2, 3, -2, 5) which is a contiguous subarray.

#CODE

def max_sum_subarray(arr):

    max_so_far = arr[0]

    max_ending_here = arr[0]

    
    for i in range(1, len(arr)):

        max_ending_here = max(arr[i], max_ending_here+arr[i])

        max_so_far = max(max_so_far, max_ending_here)

    
    return max_so_far



T = int(input())

for _ in range(T):

    N = int(input())

    inp = list(map(int, input().split()))

    print( max_sum_subarray(inp) )


#TO PRINT MAX SUM SUBARRAY

from sys import maxsize
def maxSubArraySum(a,size): 
  
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
  
    for i in range(0,size): 
  
        max_ending_here += a[i] 
  
        if max_so_far < max_ending_here: 
            max_so_far = max_ending_here 
            start = s 
            end = i 
  
        if max_ending_here < 0: 
            max_ending_here = 0
            s = i+1
  
    print ("Maximum contiguous sum is %d"%(max_so_far)) 
    print ("Starting Index %d"%(start)) 
    print ("Ending Index %d"%(end))